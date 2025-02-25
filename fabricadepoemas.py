import random

substantivos_masculinos = ['céu', 'menino', 'elefante']
substantivos_femininos = ['chuva', 'menina', 'girafa']
verbos = ['andou', 'voou', 'chorou']
adjetivos_masculinos = ['lindo', 'forte', 'feio']
adjetivos_femininos = ['maravilhosa', 'fedorenta', 'babilônica']

verso_atual = 1
verso_atual_escrito = ''
numero_de_estrofes = 4
estrofe_completa_masc = ''
estrofe_completa_fem = ''

while verso_atual <= numero_de_estrofes:
    verso_atual_escrito = f'O {random.choice(substantivos_masculinos)} {random.choice(adjetivos_masculinos)} {random.choice(verbos)}'
    estrofe_completa_masc += verso_atual_escrito + '\n'

    verso_atual_escrito = f'A {random.choice(substantivos_femininos)} {random.choice(adjetivos_femininos)} {random.choice(verbos)}'
    estrofe_completa_fem += verso_atual_escrito + '\n'

    verso_atual +=1

print(estrofe_completa_masc + '\n' + estrofe_completa_fem)