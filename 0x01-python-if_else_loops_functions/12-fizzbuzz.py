#!/usr/bin/python3
def fizzbuzz():
    i = range(1, 101)
    for c in i:
        if c % 3 == 0 and c % 5 == 0:
            print('FizzBuzz')
        elif c % 3 == 0 and c % 5 != 0:
            print('Fizz')
        elif c % 3 != 0 and c % 5 == 0:
            print('Buzz')
        elif c % 3 != 0 and c % 5 != 0:
            print(f'{c}')
