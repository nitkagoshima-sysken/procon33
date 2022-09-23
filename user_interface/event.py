import os
from datetime import datetime, timezone, timedelta
import librosa


def get_match_wrapper(fn, textBoxes):
    def wrapper():
        success, data = fn()
        for key in textBoxes:
            textBoxes[key]['state'] = 'normal'
            textBoxes[key].delete('1.0', 'end')

        if not success:
            textBoxes['failure'].insert(1.0, data)
        else:
            textBoxes['problems'].insert(1.0, str(data['problems']))
            textBoxes['bonus_factor'].insert(1.0, str(data['bonus_factor']))
            textBoxes['penalty'].insert(1.0, str(data['penalty']))

        for key in textBoxes:
            textBoxes[key]['state'] = 'disabled'
        
    return wrapper


def get_problem_wrapper(fn, textBoxes):
    def wrapper():
        success, data = fn()
        for key in textBoxes:
            textBoxes[key]['state'] = 'normal'
            textBoxes[key].delete('1.0', 'end')
        
        if not success:
            textBoxes['failure'].insert(1.0, data)
        else:
            textBoxes['id'].insert(1.0, str(data['id']))
            textBoxes['chunks'].insert(1.0, str(data['chunks']))
            # unixtimeを日本時間に変換
            JST = timezone(timedelta(hours=+9), 'JST')
            start_at = datetime.fromtimestamp(data['starts_at']).replace(tzinfo=timezone.utc).astimezone(tz=JST)
            textBoxes['start_at'].insert(1.0, start_at.strftime('%H:%M:%S'))
            textBoxes['time_limit'].insert(1.0, str(data['time_limit']) + '秒')
            textBoxes['data'].insert(1.0, str(data['data']))
        
        for key in textBoxes:
            textBoxes[key]['state'] = 'disabled'
        
    return wrapper


def get_file_wrapper(get_chunk, get_file, n_chunk_text, match_id_text, problem_id_text, chunk_response_text, file_response_text):
    def wrapper():
        n_chunk = int(n_chunk_text.get().replace('\n', ''))
        chunk_success, chunk_data = get_chunk(n_chunk)

        chunk_response_text['state'] = 'normal'
        file_response_text['state'] = 'normal'
        chunk_response_text.delete(1.0, 'end')
        file_response_text.delete(1.0, 'end')

        if not chunk_success:
            chunk_response_text.insert(1.0, str(chunk_data) + '\n')
        else:
            chunk_response_text.insert(1.0, 'success\n')

            match_id = match_id_text.get()
            problem_id = problem_id_text.get('1.0', 'end').replace('\n', '')
            save_path = r'./problems/match' + match_id + r'/problem_' + problem_id + r'/'
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            for file_name in chunk_data['chunks']:
                file_success, file_data = get_file(file_name, save_path)
                if not file_success:
                    file_response_text.insert(1.0, str(file_data) + '\n')
                else:
                    file_response_text.insert(1.0, 'success\n')
        
        chunk_response_text['state'] = 'disabled'
        file_response_text['state'] = 'disabled'
        
    return wrapper


def answer_wrapper(fn, problem_id_text, answers_text, textBoxes):
    def wrapper():
        problem_id = problem_id_text.get('1.0', 'end').replace('\n', '')
        answers = answers_text.get('1.0', 'end').replace('\n', '')[1:-1].split(', ')
        for i in range(len(answers)):
            answers[i] = answers[i].zfill(2)
        success, data = fn(problem_id, answers)
        print(answers)

        for key in textBoxes:
            textBoxes[key]['state'] = 'normal'
            textBoxes[key].delete('1.0', 'end')

        if not success:
            textBoxes['failure'].insert(1.0, data)
        else:
            textBoxes['problem_id'].insert(1.0, str(data['problem_id']))
            textBoxes['answers'].insert(1.0, str(data['answers']))
            # unixtimeを日本時間に変換
            JST = timezone(timedelta(hours=+9), 'JST')
            start_at = datetime.fromtimestamp(data['accepted_at']).replace(tzinfo=timezone.utc).astimezone(tz=JST)
            textBoxes['accepted_at'].insert(1.0, start_at.strftime('%H:%M:%S'))

        for key in textBoxes:
            textBoxes[key]['state'] = 'disabled'

    return wrapper

def predict_wrapper(predict, model_name, match_id_text, problem_id_text, nsplit_text, result_text):
    def wrapper():
        nsplit = int(nsplit_text.get('1.0', 'end').replace('\n', ''))
        match_id = match_id_text.get()
        problem_id = problem_id_text.get('1.0', 'end').replace('\n', '')
        save_path = r'./problems/match' + match_id + r'/problem_' + problem_id + r'/'
        directory_list = os.listdir(save_path)
        directory_list.sort()
        problem = []
        for file_name in directory_list:
            file_number = int(file_name[7])
            file_data, sr = librosa.load(save_path + file_name)
            print(file_number, len(file_data))
            problem.append((file_number, file_data))
        result = predict(model_name, problem, nsplit)

        result_text['state'] = 'normal'
        result_text.delete('1.0', 'end')
        result_text.insert('1.0', str(result))
        result_text['state'] = 'disabled'

    return wrapper
