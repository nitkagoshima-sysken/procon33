import tkinter

from model.predict import predict as predict_by_cnn
from model.correlation.predict import predict as predict_by_raw_sound_correlation
from user_interface.setup import setup
from network_interface.functions import async_runner, get_match, get_problem, get_chunk, get_file, answer, get_test


class App:
    def __init__(self):
        self.app = tkinter.Tk()

        functions = {
            'get match': async_runner(get_match),
            'get problem': async_runner(get_problem),
            'get chunk': async_runner(get_chunk),
            'get file': async_runner(get_file),
            'submit answer': async_runner(answer),
            'get test': async_runner(get_test),
            'predict': predict_by_raw_sound_correlation
        }
        setup(self.app, functions, 'solver')

    def run(self):
        self.app.mainloop()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()

