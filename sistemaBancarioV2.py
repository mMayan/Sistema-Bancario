dict_de_usuarios = {}
num_conta = 0

def cadastrar_usuario():
    global dict_de_usuarios

    cpf_user = str(input("digite o cpf titular da conta: "))
    if cpf_user in dict_de_usuarios:
        print("======================\n"
              "usuário já cadastrado!\n"
              "tente novamente.\n"
              "======================\n")
        return
    
    nome_user = str(input("digite o nome do titular: "))
    date_user = str(input("digite a data de nascimento do titular: "))
    address_user = str(input("modelo padrão: 'logradouro, num - bairro - cidade/sigla estado\n"
                            "digite o endereço do titular: "))

    dict_de_usuarios.update({cpf_user: {"nome": nome_user, "data de nascimento": date_user, 
                                        "endereço": address_user}})
    dict_de_usuarios[cpf_user]["limite saque"] = 3

def criar_conta_corrente():
    global dict_de_usuarios, num_conta

    cpf_user = str(input("digite o cpf cadastrado do usuário: "))
    if cpf_user not in dict_de_usuarios:
        print("\n========================================\n"
            "usuário não encontrado no banco de dados!\n"
            "=========================================\n")
        return

    AGENCIA_CONTA = "0001"
    num_conta += 1

    if "conta corrente" not in dict_de_usuarios[cpf_user]:
        dict_de_usuarios[cpf_user].update({"conta corrente": [{"agência": AGENCIA_CONTA, 
                                            "número da conta": num_conta}]})
        print("\n=======================\n"
            "conta corrente criada!\n"
            "=======================\n")
    else:
        dict_de_usuarios[cpf_user]["conta corrente"].append({"agência": AGENCIA_CONTA, 
                                                            "número da conta": num_conta})
        print("conta corrente criada!\n")

def verifica_info_usuario():
    global dict_de_usuarios

    cpf_user = str(input("digite o cpf do titular para visualizar as informações da conta: "))

    #--developer only--#
    if cpf_user == 'p':
        print(dict_de_usuarios)
    #--developer only--#
    
    elif cpf_user not in dict_de_usuarios:
        print("\n========================================\n"
            "usuário não encontrado no banco de dados!\n"
            "=========================================\n")
        return
    
    else:
        print("---------------------")
        for i in dict_de_usuarios[cpf_user].items():
            print(i)
        print("---------------------\n")
        
    
# todas as operações abaixo desse comentário 
# só podem ser realizadas caso o usuário já tenha criado uma conta corrente

def deposito():
    global dict_de_usuarios

    cpf_user = str(input("digite o cpf do titular para realizar o depósito: "))
    if cpf_user not in dict_de_usuarios:
        print("\n=========================================\n"
            "usuário não encontrado no banco de dados!\n"
            "=========================================\n")
        return
    if "conta corrente" not in dict_de_usuarios[cpf_user]:
        print("\n========================================\n"
            "usuário não possui conta corrente!\n"
            "=========================================\n")
        return
    
    if "movimentações" not in dict_de_usuarios[cpf_user]:
        deposito_user = float(input("digite a quantidade para depositar: "))
        if deposito_user <= 0:
            print("\n========================================\n"
            "por favor, digitar apenas valores positivos!\n"
            "=========================================\n")
            return
        dict_de_usuarios[cpf_user].update({"movimentações": deposito_user})
    else:
        deposito_user = float(input("digite a quantidade para depositar novamente: "))
        if deposito_user <= 0:
            print("\n========================================\n"
            "por favor, digitar apenas valores positivos!\n"
            "=========================================\n")
            return
        dict_de_usuarios[cpf_user]["movimentações"] += deposito_user
        

def saque():
    global dict_de_usuarios
    
    cpf_user = str(input("digite o cpf do titular para realizar o depósito: "))
    #depois do cpf_user, verificar se a conta do titular ainda tem disponibilidade de saque
    if cpf_user not in dict_de_usuarios:
        print("\n=========================================\n"
            "usuário não encontrado no banco de dados!\n"
            "=========================================\n")
        return
    if "conta corrente" not in dict_de_usuarios[cpf_user]:
        print("\n========================================\n"
            "usuário não possui conta corrente!\n"
            "=========================================\n")
        return
    #número de saques 3 por dia
    deposito_user = float(input("digite o quanto você quer sacar: "))
    if deposito_user <= 0:
            print("\n========================================\n"
            "por favor, digitar apenas valores positivos!\n"
            "=========================================\n")
            return
    elif deposito_user <= dict_de_usuarios[cpf_user]["movimentações"] and deposito_user <= 500:
        dict_de_usuarios[cpf_user]["movimentações"] -= deposito_user
    else:
        print("\nparece que você tentou sacar mais do que 500 reais\n")

    # pela peculiaridade de ser por usuário, talvez eu não precise da função extrato
    # eu posso registrar a movimentação direto na função de saque
def extrato():
    pass

def main():
    while True:
        op = str(input('--------- MENU ---------\n'
                       '(U) - cadastrar usuário\n'
                       '(C) - criar conta corrente\n'
                       '(V) - verificar informação do usuário\n'
                       '(D) - depósito\n'
                       '(S) - saque\n'
                       '(E) - extrato\n'
                       '(Q) - sair: ')).lower()
        if op == 'u':
            cadastrar_usuario()
        elif op == 'c':
            criar_conta_corrente()
        elif op == 'v':
            verifica_info_usuario()
        elif op == 'd':
            deposito()
        elif op == 's':
            saque()
        elif op == 'e':
            extrato()
        elif op == 'q':
            break
        else: 
            print("\nentrada inválida!\n")

main()

# a função de cadastro está completa? R: sim!
# a função de conta corrente está completa? R: sim!
# a função de verificar dados está completa? R: sim!
# a função depósito está completa? R: sim, com algumas funcionalidades extras e com os requisitos do github!
# todos os prints estão completos? R: os principais estão!