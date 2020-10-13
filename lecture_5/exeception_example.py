def b():
    return 5 / 0


def a():
    # print(b())
    raise Exception("Hello Hello")


try:
    print(a())
    print('Just going with the flow')
except TypeError:
    print('ggg')
except ZeroDivisionError:
    print('There was a problem!')
except Exception as e:
    print(e)
else:
    print('There was no problem!')
