import random

numero_secreto = random.randint(1, 10)

print('Estou pensando em um numero entre 1 e 10. Voce consegue advinhar?')
palpite = int(input('Insira seu palpite: '))

if palpite == numero_secreto:
    print(f'Parabens! O numero que pensei foi {numero_secreto} e o seu palpite era {palpite}, entao voce venceu!')
elif palpite == numero_secreto + 1:
    print(f'Foi quase! O numero que pensei eh {numero_secreto}')
elif palpite == numero_secreto - 1:
    print(f'Foi quase! O numero que pensei eh {numero_secreto}')
else:
    print(f'O seu palpite foi {palpite} e o numero que pensei foi {numero_secreto}, entao voce perdeu...')