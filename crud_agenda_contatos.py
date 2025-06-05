'''
Implementar a opções do menu, sempre cuidando de validar os inputs do
usuário.
Usar, sempre que cabível, as funções prontas no código.

Fazer o trabalho em duplas e entregar duas semanas, ou seja, NÃO na
próxima aula, na seguinte.
Substituir, na função apresenteSe, o texto:
"Profs André Carvalho & J.G.Pícolo"
por um texto contendo os nomes e RAs dos alunos da dupla.
Também substituir o texto:
"Versão 1.0 de 12/maio/2025"
por
"Versão 2.0 de dd/mm/aaaa"
sendo dd/mm/aaaa a data que que a dupla concluiu seu trabalho.

A entrega será na forma de demonstração ao professor; os dois da dupla
deverão estar presentes na entrega e serão questionados pelo professor
sobre o programa que apresentam.
IMPORTANTE: este questionamento poderá resultar em notas diferentes para
os alunos da dupla, ou até em uma nota bem baixa para um programa que
funciona perfeitamente (basta estar perdido na demonstração).
'''




def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Aluno Matheus Galdini   R.A 25003297                        |')
    print('|                                                             |')
    print('| Versão 2.0 de 12/maio/2025                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)





def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1
    while inicio <= final:
        meio = (inicio + final) // 2
        if agd[meio][0] == nom:
            return [True, meio]
        elif agd[meio][0] > nom:
            final = meio - 1
        else:
            inicio = meio + 1
    return [False, inicio]

import re

def cadastrar(agd):
    while True:
        # Validação do nome
        nome = input("Digite seu Nome e Sobrenome (para cancelar digite 'cancelar'): ").lower()
        if nome == 'cancelar':
            print("Cadastro cancelado.")
            return
        if not re.match(r'^[a-zA-Z]+\s[a-zA-Z]+$', nome):
            print("Nome inválido. Deve conter apenas nome e sobrenome, com letras e espaço.")
            continue

        pos = ondeEsta(nome, agd)
        if pos[0]:
            print("Esse nome já está cadastrado.")
            return

        # Validação do aniversário
        while True:
            aniversario = input("Digite a data de aniversário DD/MM/AAAA (para cancelar digite 'cancelar'): ")
            if aniversario == 'cancelar':
                print("Cadastro cancelado.")
                return
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', aniversario):
                print("Data inválida. Use o formato DD/MM/AAAA.")
                continue
            dia, mes, ano = map(int, aniversario.split('/'))
            if dia < 1 or dia > 31 or mes < 1 or mes > 12:
                print("Dia ou mês inválido.")
                continue
            if mes == 2 and dia > 29:
                print("Fevereiro só vai até 29.")
                continue
            if ano < 1900 or ano > 2025:
                print("Ano inválido")
                continue
            break

        # Validação do endereço
        while True:
            endereco = input("Digite o endereço (para cancelar digite 'cancelar'): ").strip()
            if endereco == 'cancelar':
                print("Cadastro cancelado.")
                return
            if len(endereco.split()) < 2:
                print("O endereço deve conter pelo menos rua e número.")
                continue
            if not re.search(r'[A-Za-z]', endereco) or not re.search(r'\d', endereco):
                print("O endereço deve conter letras e números.")
                continue
            break

        
        while True:
            telefone = input("Digite o telefone fixo (para cancelar digite 'cancelar'): ").strip()
            if telefone.lower() == 'cancelar':
                print("Cadastro cancelado.")
                return
            telefone_limpo = re.sub(r'\D', '', telefone)  
            if len(telefone_limpo) != 10:
                print("Telefone fixo inválido. Deve conter DDD + número (total 10 dígitos).")
                continue
        
            telefone_formatado = f"({telefone_limpo[:2]}) {telefone_limpo[2:6]}-{telefone_limpo[6:]}"
            break

        
        while True:
            celular = input("Digite o celular (11 dígitos, para cancelar digite 'cancelar'): ").strip()
            if celular.lower() == 'cancelar':
                print("Cadastro cancelado.")
                return
            celular_limpo = re.sub(r'\D', '', celular)  
            if len(celular_limpo) != 11:
                print("Celular inválido. Deve conter DDD + número (total 11 dígitos).")
                continue
            
            celular_formatado = f"({celular_limpo[:2]}) {celular_limpo[2:7]}-{celular_limpo[7:]}"
            break
      

        # Validação do email
        while True:
            email = input("Digite o email (para cancelar digite 'cancelar'): ").strip()
            if email == 'cancelar':
                print("Cadastro cancelado.")
                return
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                print("Email inválido.")
                continue
            break

        # Cadastro
        contato = [nome, aniversario, endereco, telefone, celular, email]
        agd.insert(pos[1], contato)

        print("Contato cadastrado com sucesso.")
        break


def procurar(agd):
    while True:
        nome_procurar = input("Digite o nome que deseja procurar (ou 'cancela' para sair): ").lower()
        if nome_procurar == 'cancela':
            print("Busca cancelada.")
            return

        nome_encontrado = False
        for contato in agd:
            if contato[0] == nome_procurar:
                print("Dados encontrados:")
                for dado in contato:
                    print(dado)
                nome_encontrado = True
                break

        if nome_encontrado:
            break
        else:
            print("Contato não encontrado. Tente novamente ou digite 'cancela'.")

def atualizar(agd):
    while True:
        nome_procurar = input("Digite o nome e sobrenome que deseja atualizar (ou 'cancelar' para sair): ").lower()
        if nome_procurar == 'cancelar':
            print("Atualização cancelada.")
            return

        indice = -1
        for i in range(len(agd)):
            if agd[i][0] == nome_procurar:
                indice = i
                break

        if indice == -1:
            print("Contato não encontrado. Tente novamente ou digite 'cancelar'.")
            continue

        menu = ['Atualizar Endereço',
                'Atualizar Aniversário',
                'Atualizar Telefone Fixo',
                'Atualizar Celular',
                'Atualizar Email',
                'Finalizar Atualizações']

        while True:
            print("\nO que você deseja atualizar?")
            opcao = int(opcaoEscolhida(menu))

            if opcao == 1:
                novo_endereco = input("Digite o novo endereço: ")
                agd[indice][2] = novo_endereco
                print("Endereço atualizado com sucesso!")
            elif opcao == 2:
                novo_aniversario = input("Digite o novo aniversário: ")
                agd[indice][1] = novo_aniversario
                print("Aniversário atualizado com sucesso!")
            elif opcao == 3:
                novo_telefone = input("Digite o novo telefone fixo: ")
                agd[indice][3] = novo_telefone
                print("Telefone fixo atualizado com sucesso!")
            elif opcao == 4:
                novo_celular = input("Digite o novo celular: ")
                agd[indice][4] = novo_celular
                print("Celular atualizado com sucesso!")
            elif opcao == 5:
                novo_email = input("Digite o novo email: ")
                agd[indice][5] = novo_email
                print("Email atualizado com sucesso!")
            elif opcao == 6:
                print("Atualizações finalizadas.")
                break
            else:
                print("Opção inválida. Tente novamente.")

        break


def listar(agd):
    if not agd:
        print("Não há contatos cadastrados.")
        return
    print("Lista de Contatos:")
    for contato in agd:
        print("-" * 30)
        for dado in contato:
            print(dado)

def excluir(agd):
    while True:
        nome_excluir = input("Digite o nome que deseja excluir (ou 'cancela' para sair): ").lower()
        if nome_excluir == 'cancela':
            print("Exclusão cancelada.")
            return

        indice = -1
        for i in range(len(agd)):
            if agd[i][0] == nome_excluir:
                indice = i
                break

        if indice == -1:
            print("Contato não encontrado. Tente novamente ou digite 'cancela'.")
            continue

        print("Contato encontrado:")
        for dado in agd[indice]:
            print(dado)

        confirmacao = input("Tem certeza que deseja excluir? (s/n): ").lower()
        if confirmacao == 's':
            agd.pop(indice)
            print("Contato excluído com sucesso!")
        else:
            print("Exclusão não realizada.")
        break


    
    
# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa
# (nosso CRUD, C=create(cadastrar), R=read(recuperar),
# U=update(atualizar), D=delete(remover,apagar)




apresenteSe()

agenda=[] # essa é a listona que deverá conter listinhas

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: 
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')
