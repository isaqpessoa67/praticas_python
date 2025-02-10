pontuação_do_jogador = 50

print('Voce entrou no labirinto. Sua pontuacao atual eh', pontuação_do_jogador, end='.')

escolha_encruzilhada = int(input('Voce deu de cara com uma encruzilhada e agora deve decidir entre direita e esquerda! Digite 1 para esquerda ou 2 para direita.'))
escolha_tesouro = int(input('Voce acaba de encontrar um bau misterioso! Digite 1 se voce quer abrir ou 2 se voce quiser ignorar.'))
escolha_guardiao = int(input('Voce ve uma criatura descendo. Eh o guardiao do labirinto! Ele afirma que a Letrux é a maior artista do Brasil. Digite 1 se voce concorda ou 2 se voce discorda.'))

if escolha_encruzilhada == 1: 
    pontuação_do_jogador = pontuação_do_jogador + 10
elif escolha_encruzilhada == 2:
    pontuação_do_jogador = pontuação_do_jogador - 20

if escolha_tesouro == 1:
    pontuação_do_jogador = pontuação_do_jogador * 2
elif escolha_tesouro == 2:
    pontuação_do_jogador = pontuação_do_jogador - 5

if escolha_guardiao == 1:
    pontuação_do_jogador = pontuação_do_jogador + 50
elif escolha_guardiao == 2 :
    pontuação_do_jogador = pontuação_do_jogador / 2

if pontuação_do_jogador >= 100:
    print('Parabens! Sua pontuacao foi', pontuação_do_jogador, 'e voce venceu o labirinto!')
elif 50 <= pontuação_do_jogador < 100:
    print('Parabens! Voce venceu o labirinto, mas foi por pouco. Sua pontuacao foi', pontuação_do_jogador, end='.')
else:
    print('Voce foi derrotado no labirinto.Sua pontuacao foi', pontuação_do_jogador, end='.')