text = 'mrttaqrhknsw ih puggrur' # texto codificado
custom_key = 'happycoding'# chave para codificação

def vigenere(message, key, direction=1): 
    key_index = 0 # controle de index que sera percorrido, começando no 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # alfabeto
    final_message = '' # mensagem que será exibida ao final 

    for char in message.lower(): # percorre cada letra do valor da variavel message

        if not char.isalpha():
            final_message += char # se algum caractere nao for letra, essa será adicionada no fim da mensagem final
        else:        
            key_char = key[key_index % len(key)]
            # aqui, garantimos que o indice não irá ultrapassar o comprimento da chave
            key_index += 1 # faz com que a chave inteira seja percorrida caractere por caractere
            
            
            offset = alphabet.index(key_char)
            # aqui está sendo procurado no alfabeto o indice do caractere da chave
            index = alphabet.find(char)
            # está pegando o caractere percorrido atualmente e procurando seu indice no alfabeto
            new_index = (index + offset*direction) % len(alphabet)
            # novo indice, usando modulo pra garantir que nao ultrapasse o comprimento do alfabeto
            final_message += alphabet[new_index]
            # mensagem final, sendo adicionado todos os indices atualizados.
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')