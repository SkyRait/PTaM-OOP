from libr.Worker.Worker import Worker
import os
from sys import argv


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def run(args: list) -> None:
    """
    This function runs the program
    :param args: command line arguments
    :return: None
    """
    worker = Worker()

    file_in, file_out = args[1:]
    worker.run(file_in, file_out)


if __name__ == '__main__':
    run(argv)
