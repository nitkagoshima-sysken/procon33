def get_match_wrapper(fn,textbox):
    def wrapper():
        text = fn()
        # TODO: update textボックスに表示
    return wrapper


def get_problem_wrapper(fn,textbox):
    def wrapper():
        text = fn()
        # TODO: update text
    return wrapper


def get_chunk_wrapper(fn,textbox):
    def wrapper(*args, **kwargs):
        text = fn(*args, **kwargs)  # TODO: add texts to arguments
        # TODO: update text
    return wrapper


def get_file_wrapper(fn):
    def wrapper():
        text = fn()  # TODO: add texts to arguments
        # TODO: update text
    return wrapper


def answer_wrapper(fn,textAnswer,textSubmit):
    def wrapper():
        text = fn()  # TODO: add texts to arguments
        # TODO: update text
    return wrapper