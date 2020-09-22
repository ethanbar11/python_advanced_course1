import sys

print('woho')
sys.stdout.write('Woho #2\n')
raise Exception()
x = sys.stdin.readline()
sys.stderr.write(x)

# Printing the string, and then accepting input from the user
# and returns it.
def my_input(string_to_print):
    pass

# same as print, with enter in the end.
def my_print(to_print):
    pass
