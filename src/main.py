from bar import bar_1
from bar import bar_2

from foo import foo_1
from foo import foo_2

def main():
    bar_1.print_bar_1()
    bar_2.print_bar_2()

    foo_1.print_foo_1()
    foo_2.print_foo_2()

if __name__ == '__main__':
    main()
