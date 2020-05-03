from hello import __version__
from hello import greetings


def test_version():
    assert __version__ == "0.1.1"


def test_say_hello():
    assert greetings.say_hello("Weverton") == "Hello, Weverton!"
