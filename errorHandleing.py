def spam(divideBy):
    return 42 / divideBy

try:
    print('42/2 = ' +str(spam(2)))
    print('42/12 = ' +str(+spam(12)))
    print('42/1 = ' +str(spam(1)))
    print('42/0 = ' +str(spam(0)))
except ZeroDivisionError:
    print('Error: Invalid argument.')