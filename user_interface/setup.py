import tkinter as tk
from user_interface.event import get_match_wrapper, get_problem_wrapper, get_file_wrapper, answer_wrapper, predict_wrapper


def setup(app, functions, model_name):
    app.title("procon33")
    app.geometry("1200x800")

    frameMatchId = tk.Frame(app, width=150, height=20)
    frameMatchId.place(x=10, y=10)
    labelMatchId = tk.Label(frameMatchId, text='match id')
    textMatchId = tk.Entry(frameMatchId)
    labelMatchId.place(x=0, y=0)
    textMatchId.place(x=60, y=0)

    frameMatch = tk.Frame(app, width=300, height=300)
    frameMatch.place(x=10, y=60)
    labelMatch = tk.Label(frameMatch, text='match response', pady=8)
    frameMatchResponses = tk.Frame(frameMatch)
    frameMatchResponse = {}
    labelMatchResponse = {}
    textMatchResponse = {}
    matchResponseNames = ['problems', 'bonus_factor', 'penalty']
    for name in matchResponseNames:
        frameMatchResponse[name] = tk.Frame(frameMatchResponses, width=300, height=20, pady=2)
        labelMatchResponse[name] = tk.Label(frameMatchResponse[name], text=name)
        textMatchResponse[name] = tk.Text(frameMatchResponse[name], width=20, height=1)
        labelMatchResponse[name].place(x=0, y=0)
        textMatchResponse[name].place(x=100, y=0)
        frameMatchResponse[name].pack(anchor=tk.W)
    frameMatchResponse['failure'] = tk.Frame(frameMatchResponses, width=300, height=100, pady=2)
    labelMatchResponse['failure'] = tk.Label(frameMatchResponse['failure'], text='failure')
    textMatchResponse['failure'] = tk.Text(frameMatchResponse['failure'], width=20, height=5)
    labelMatchResponse['failure'].place(x=0, y=0)
    textMatchResponse['failure'].place(x=100, y=0)
    frameMatchResponse['failure'].pack(anchor=tk.W)
    buttonMatch = tk.Button(
        frameMatch,
        text='get match',
        command=get_match_wrapper(functions['get match'], textMatchResponse),
        width=10,
        height=1
    )
    buttonMatch.pack(anchor=tk.W)
    labelMatch.pack(anchor=tk.W)
    frameMatchResponses.pack(anchor=tk.W)

    frameProblem = tk.Frame(app, width=300, height=300)
    frameProblem.place(x=310, y=60)
    labelProblem = tk.Label(frameProblem, text='problem response', pady=8)
    frameProblemResponses = tk.Frame(frameProblem)
    frameProblemResponse = {}
    labelProblemResponse = {}
    textProblemResponse = {}
    problemResponseNames = ['id', 'chunks', 'start_at', 'time_limit', 'data']
    for name in problemResponseNames:
        frameProblemResponse[name] = tk.Frame(frameProblemResponses, width=300, height=20, pady=2)
        labelProblemResponse[name] = tk.Label(frameProblemResponse[name], text=name)
        textProblemResponse[name] = tk.Text(frameProblemResponse[name], width=20, height=1)
        labelProblemResponse[name].place(x=0, y=0)
        textProblemResponse[name].place(x=100, y=0)
        frameProblemResponse[name].pack(anchor=tk.W)
    frameProblemResponse['failure'] = tk.Frame(frameProblemResponses, width=300, height=100, pady=2)
    labelProblemResponse['failure'] = tk.Label(frameProblemResponse['failure'], text='failure')
    textProblemResponse['failure'] = tk.Text(frameProblemResponse['failure'], width=20, height=5)
    labelProblemResponse['failure'].place(x=0, y=0)
    textProblemResponse['failure'].place(x=100, y=0)
    frameProblemResponse['failure'].pack(anchor=tk.W)
    buttonProblem = tk.Button(
        frameProblem,
        text='get problem',
        command=get_problem_wrapper(functions['get problem'], textProblemResponse),
        width=10,
        height=1
    )
    buttonProblem.pack(anchor=tk.W)
    labelProblem.pack(anchor=tk.W)
    frameProblemResponses.pack(anchor=tk.W)

    frameChunk = tk.Frame(app, width=200, height=30)
    frameChunk.place(x=10, y=330)
    labelChunk = tk.Label(frameChunk, text='取得するデータ数')
    textChunk = tk.Entry(frameChunk)
    labelChunk.pack(anchor=tk.W)
    textChunk.pack(anchor=tk.W)

    frameChunk = tk.Frame(app, width=300, height=300)
    frameChunk.place(x=160, y=330)
    labelChunk = tk.Label(frameChunk, text='chunk response')
    textChunkResponse = tk.Text(frameChunk, width=30, height=8)
    labelChunk.pack(anchor=tk.W)
    textChunkResponse.pack(anchor=tk.W)

    frameFile = tk.Frame(app, width=300, height=300)
    frameFile.place(x=380, y=330)
    labelFile = tk.Label(frameFile, text='file response')
    textFileResponse = tk.Text(frameFile, width=30, height=8)
    labelFile.pack(anchor=tk.W)
    textFileResponse.pack(anchor=tk.W)

    buttonFile = tk.Button(
        app,
        text='get files',
        command=get_file_wrapper(functions['get chunk'], functions['get file'], textChunk, textMatchId, textProblemResponse['id'], textChunkResponse, textFileResponse),
        width=10,
        height=1
    )
    buttonFile.place(x=10, y=400)

    frameAnswer = tk.Frame(app, width=300, height=300)
    frameAnswer.place(x=10, y=520)
    labelAnswer = tk.Label(frameAnswer, text='answer')
    textAnswer = tk.Text(frameAnswer, width=30, height=8)
    labelAnswer.pack(anchor=tk.W)
    textAnswer.pack(anchor=tk.W)

    frameSubmit = tk.Frame(app, width=300, height=300)
    frameSubmit.place(x=310, y=520)
    labelSubmit = tk.Label(frameSubmit, text='submit response', pady=8)
    frameSubmitResponses = tk.Frame(frameSubmit)
    frameSubmitResponse = {}
    labelSubmitResponse = {}
    textSubmitResponse = {}
    submitResponseNames = ['problem_id', 'answers', 'accepted_at']
    for name in submitResponseNames:
        frameSubmitResponse[name] = tk.Frame(frameSubmitResponses, width=300, height=20, pady=2)
        labelSubmitResponse[name] = tk.Label(frameSubmitResponse[name], text=name)
        textSubmitResponse[name] = tk.Text(frameSubmitResponse[name], width=20, height=1)
        labelSubmitResponse[name].place(x=0, y=0)
        textSubmitResponse[name].place(x=100, y=0)
        frameSubmitResponse[name].pack(anchor=tk.W)
    frameSubmitResponse['failure'] = tk.Frame(frameSubmitResponses, width=300, height=100, pady=2)
    labelSubmitResponse['failure'] = tk.Label(frameSubmitResponse['failure'], text='failure')
    textSubmitResponse['failure'] = tk.Text(frameSubmitResponse['failure'], width=20, height=5)
    labelSubmitResponse['failure'].place(x=0, y=0)
    textSubmitResponse['failure'].place(x=100, y=0)
    frameSubmitResponse['failure'].pack(anchor=tk.W)
    buttonSubmit = tk.Button(
        frameSubmit,
        text='submit',
        command=answer_wrapper(functions['submit answer'], textProblemResponse['id'], textAnswer, textSubmitResponse),
        width=10,
        height=1
    )
    buttonSubmit.pack(anchor=tk.W)
    labelSubmit.pack(anchor=tk.W)
    frameSubmitResponses.pack(anchor=tk.W)

    frameResult = tk.Frame(app, width=300, height=300)
    frameResult.place(x=800, y=50)
    labelResult = tk.Label(frameResult, text='result')
    textResult = tk.Text(frameResult, width=30, height=8)
    labelResult.pack(anchor=tk.W)
    textResult.pack(anchor=tk.W)

    buttonPredict = tk.Button(
        app,
        text='predict',
        command=predict_wrapper(functions['predict'], model_name, textMatchId, textProblemResponse['id'], textProblemResponse['chunks'], textResult),
        width=10,
        height=1
    )
    buttonPredict.place(x=700, y=50)
