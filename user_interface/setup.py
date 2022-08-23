import tkinter


def get_match_wrapper(fn):
    def wrapper():
        text = fn()
        # TODO: update text
    return wrapper


def get_problem_wrapper(fn):
    def wrapper():
        text = fn()
        # TODO: update text
    return wrapper


def get_chunk_wrapper(fn):
    def wrapper(*args, **kwargs):
        text = fn(*args, **kwargs)  # TODO: add texts to arguments
        # TODO: update text
    return wrapper


def get_file_wrapper(fn):
    def wrapper():
        text = fn()  # TODO: add texts to arguments
        # TODO: update text
    return wrapper


def answer_wrapper(fn):
    def wrapper():
        text = fn()  # TODO: add texts to arguments
        # TODO: update text
    return wrapper


def setup(app, functions):
    # アプリの画面設定
    app.geometry(
        "600x400"
    )
    app.title(
        "test"
    )

    # TODO: add textboxes to io

    handlers = []
    handlers.append({'name':'get match', 'handler': get_match_wrapper(functions['get match'])})
    handlers.append({'name': 'get problem', 'handler': get_problem_wrapper(functions['get problem'])})
    handlers.append({'name': 'get chunk', 'handler': get_chunk_wrapper(functions['get chunk'])})
    handlers.append({'name': 'get file', 'handler': get_file_wrapper(functions['get file'])})
    handlers.append({'name': 'submit answer', 'handler': answer_wrapper(functions['submit answer'])})

    buttons = []
    button_width = 10
    button_height = 2
    for value in handlers:
        button = tkinter.Button(
            app,
            text=value['name'],
            command=value['handler'],
            width=button_width,
            height=button_height
        )
        buttons.append(button)

    for button in buttons:# zip でテキストボックスと一緒に並べる
        button.pack(padx=10, pady=10)
