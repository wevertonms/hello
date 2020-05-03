__version__ = "0.1.1"

import sys

from hello import greetings


def main():
    for name in sys.argv[1:]:
        print(greetings.say_hello(name))
