import random

random_number = random.randint(1, 100)
palpite = int(input('Escolha um número de 1 a 100:'))

if palpite > random_number:
    print('Muito alto!')
elif palpite < random_number:
    print('Muito baixo!')
elif palpite == random_number:
    print('Vitória!!')