import tkinter as tk
from user_interface.event import get_match_wrapper, get_problem_wrapper, get_chunk_wrapper, get_file_wrapper, answer_wrapper


def setup(app, functions):
    app.title("Title")
    app.geometry("1200x1200")

    labelMatch=tk.Label(text='match response')
    labelMatch.place(x=0,y=25)
    labelPro=tk.Label(text='problem response')
    labelPro.place(x=350,y=25)

    frameMatch = tk.Frame()
    frameMatch.place(x=0,y=50,width=300,height=150)
    framePro = tk.Frame()
    framePro.place(x=350,y=50,width=300,height=150)

    txtMatch=tk.Text(frameMatch)
    txtPro=tk.Text(framePro)
    scrollMatch = tk.Scrollbar(frameMatch, orient=tk.VERTICAL, command=txtMatch.yview)
    scrollMatch.pack(side=tk.RIGHT, fill="x")
    scrollPro = tk.Scrollbar(framePro, orient=tk.VERTICAL, command=txtPro.yview)
    scrollPro.pack(side=tk.RIGHT, fill="x")
    txtMatch["yscrollcommand"] = scrollMatch.set
    txtPro["yscrollcommand"] = scrollPro.set
    txtMatch.pack()
    txtPro.pack()

    """ txtMatch.configure(state='normal')
    txtMatch.insert(tk.END,a)
    txtMatch.configure(state='disabled')"""

    buttonMatch = tk.Button(
        app,
        text='get match',
        command=get_match_wrapper(functions['get match'],txtMatch),
        width=10,
        height=1
    )
    buttonMatch.place(x=0,y=0)
    buttonPro = tk.Button(
        app,
        text='get problem',
        command=get_problem_wrapper(functions['get problem'],txtPro),
        width=10,
        height=1
    )
    buttonPro.place(x=350,y=0)

    labelData=tk.Label(text='習得するデータ数')
    labelData.place(x=0,y=200)
    txtData=tk.Entry()
    txtData.place(x=0,y=225,width=200,height=30)

    labelChunk=tk.Label(text='chunk response')
    labelChunk.place(x=0,y=280)
    frameChunk = tk.Frame()
    frameChunk.place(x=0,y=300,width=300,height=150)
    txtChunk=tk.Text(frameChunk)
    scrollChunk = tk.Scrollbar(frameChunk, orient=tk.VERTICAL, command=txtChunk.yview)
    scrollChunk.pack(side=tk.RIGHT, fill="x")
    txtChunk["yscrollcommand"] = scrollChunk.set
    txtChunk.pack()
    buttonChunk = tk.Button(
        app,
        text='get chunk',
        command=get_chunk_wrapper(functions['get chunk'],txtChunk),
        width=10,
        height=1
    )
    buttonChunk.place(x=0,y=260)

    labelAnswer=tk.Label(text='回答')
    labelAnswer.place(x=0,y=450)
    frameAnswer = tk.Frame()
    frameAnswer.place(x=0,y=470,width=300,height=150)
    txtAnswer=tk.Text(frameAnswer)
    scrollAnswer = tk.Scrollbar(frameAnswer, orient=tk.VERTICAL, command=txtAnswer.yview)
    scrollAnswer.pack(side=tk.RIGHT, fill="x")
    txtAnswer["yscrollcommand"] = scrollAnswer.set
    txtAnswer.pack()

    labelSubmit=tk.Label(text='submit response')
    labelSubmit.place(x=0,y=645)
    frameSubmit = tk.Frame()
    frameSubmit.place(x=0,y=665,width=300,height=150)
    txtSubmit=tk.Text(frameSubmit)
    scrollSubmit = tk.Scrollbar(frameSubmit, orient=tk.VERTICAL, command=txtSubmit.yview)
    scrollSubmit.pack(side=tk.RIGHT, fill="x")
    txtSubmit["yscrollcommand"] = scrollSubmit.set
    txtSubmit.pack()

    buttonAnswer = tk.Button(
        app,
        text='submit answer',
        command=answer_wrapper(functions['submit answer'],txtAnswer,txtSubmit),
        width=10,
        height=1
    )
    buttonAnswer.place(x=0,y=620)
