import sys
import hello

for name in sys.argv[1:]:
    print(hello.say_hello(name))
