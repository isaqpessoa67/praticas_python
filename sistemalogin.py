usuarios = {
    "joaopedro": "123456",
    "mariacosta": "abcdef",
    "pedropascal": "ghijkl",
    "ispessoa": "10102020"
}

boas_vindas = input('Boas vindas ao programa! Já tem uma conta? \n [1] sim \n [2] não ')
if boas_vindas not in ['1', '2']:
    print("Opção inválida! Por favor, digite 1 ou 2.")
    
if boas_vindas == '1':
    pedido_usuario = input('Usuário: ')
    if pedido_usuario == "":
        print("Usuário não pode ser vazio!")

    pedido_senha = input('Senha: ')
    if pedido_senha == "":
        print("Senha não pode ser vazia!")   

    if pedido_usuario in usuarios and usuarios[pedido_usuario] == pedido_senha:
        print(f'Seja bem vindo(a) ao programa, {pedido_usuario}!')
        opcoes_programa = input('O que deseja fazer?\n 1. Deletar conta\n 2. Mudar usuário ')
        if opcoes_programa == '1':
            if pedido_usuario in usuarios:
                del usuarios[pedido_usuario]
                print('Sua conta foi deletada com sucesso!')
                print(f'(ADM, essas são as contas em atividade: {usuarios})')
            else:
                print("Usuário não encontrado!")
            
        if opcoes_programa == '2':
            usuario_modificado = input('Digite seu novo usuário: ')
            if pedido_usuario in usuarios:
                usuarios[usuario_modificado] = usuarios.pop(pedido_usuario)
                print(f'Seu usuário foi atualizado com sucesso!\n Usuário anterior: {pedido_usuario}\n Novo usuário: {usuario_modificado}\n (ADM, esses são os usuários em atividade {usuarios})')
            else:
                print('Não foi possível modificar seu usúario porque seu usuário não existe.')

    else: 
        print('Usuário ou senha incorreto(s)')
elif boas_vindas == '2':
    novo_usuario = input('Insira seu novo usuário: ')
    nova_senha = input('Insira sua nova senha: ')
    if novo_usuario or nova_senha == '':
        print('Usuário e senha não podem estar vazios.')
    else:   
        usuarios[novo_usuario] = nova_senha
        print(f'(ADM, esses são os usuários em atividade {usuarios})')