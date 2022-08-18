import sys
sys.path.append('path_to_root_directory_of_this_project')
import librosa

from model.dataset.utility import to_file_name


def readdata_length_write() -> None:
    """読み札のサンプル数を書き出す
    """

    with open('./readdata_length.txt', 'w', encoding='utf-8') as f:
        for i in range(1, 89):
            speech_number = i
            speech_name = to_file_name(speech_number)
            file, sr = librosa.load(r'./src/' + speech_name, sr=None)
            f.write(str(len(file)) + '\n')


if __name__ == '__main__':
    readdata_length_write()
