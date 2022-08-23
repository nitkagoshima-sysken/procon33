import tkinter

from user_interface.setup import setup
from network_interface.functions import async_runner, get_match, get_problem, get_chunk, get_file, answer


class App:
    def __init__(self):
        self.app = tkinter.Tk()

        functions = {
            'get match': async_runner(get_match),
            'get problem': async_runner(get_problem),
            'get chunk': async_runner(get_chunk),
            'get file': async_runner(get_file),
            'submit answer': async_runner(answer)
        }
        setup(self.app, functions)

    def run(self):
        self.app.mainloop()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
