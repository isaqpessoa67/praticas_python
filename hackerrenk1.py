def fizzBuzz(n):
    for i in n:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        if i % 3 == 0:
            print('Fizz')
        if i % 5 == 0:
            print('Buzz')
        else:
            print(i)
            
fizzBuzz((10, 13, 20, 27, 30, 38, 40, 47, 50, 60, 70, 80))