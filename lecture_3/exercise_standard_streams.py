import sys
import colorama


def my_input():
    sys.stdout.write("Please enter a string")
    string = sys.stdin.readline()
    return string


def my_output(string):
    if not string.strip():
        sys.stderr.write(colorama.Fore.BLUE+"There's nothing to output.")
    else:
        sys.stdout.write(string)


new_string = my_input()
my_output(new_string)
