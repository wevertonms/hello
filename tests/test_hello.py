from hello import __version__
from hello import hello


def test_version():
    assert __version__ == "0.1.0"


def test_say_hello():
    assert hello.say_hello("Weverton") == "Hello, Weverton!"
