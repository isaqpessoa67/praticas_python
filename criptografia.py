print('Seja bem vindo ao codificador de textos. Sinta-se a vontade.')
text = input('Escreva o texto que deve ser criptografado. ')
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = (index + shift) % 26
    encrypted_text += alphabet[new_index]

print('Esse eh o seu texto criptografado:', encrypted_text)