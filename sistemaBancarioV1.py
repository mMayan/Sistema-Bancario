deposito_cliente = 0
saque_cliente = 0
quant_saque = 3
extrato_lista =[]

def deposito():
    global deposito_cliente
    deposito_cliente = float(input("digite a quantidade em R$ que você quer depositar: "))

    if deposito_cliente < 0:
        deposito_cliente = float(input("digite um valor positivo: "))

    print('\n')
    print('###############################\n'
          f'o valor depositado foi: R$ {deposito_cliente}\n'
          '###############################\n')


def saque():
    global saque_cliente, quant_saque, deposito_cliente, extrato_lista
    if quant_saque == 0:
        print("############################\n"
            "quantidade de saques excedida!\n"
            "############################")
        return
    
    print("quantidade máxima de saques: R$ 500,00")
    print(f'você tem disponível para saque: R$ {deposito_cliente}')
    saque_cliente = float(input("digite a quantidade em R$ que você quer sacar: "))
    print('\n')
        
    if saque_cliente <= deposito_cliente and saque_cliente <= 500:
        deposito_cliente -= saque_cliente
        print('###############################\n'
          f'o valor sacado foi: {saque_cliente}\n'
          '###############################\n')
        quant_saque -= 1
        extrato_lista.append(saque_cliente)
        
    else:
        print("###############################################\n"
            "saldo insuficiente ou quantidade fora do limite\n"
            "################################################\n")    
    
def verifica_saldo():
    global deposito_cliente
    print('###########################\n'
          f'o saldo atual é: R$ {deposito_cliente:.2f}\n'
          '###########################\n'
          '\n')
    
def extrato(): 
    global extrato_lista, deposito_cliente

    if len(extrato_lista) != 0:
        extrato_lista.reverse()
        ordenando_lista = ", ".join([str(elemento) for elemento in extrato_lista])
    
        print('#################\n'
          '------- valor de depósito restante -------\n'
          f'                 R$ {deposito_cliente:.2f}\n'
          '------------------------------------------\n'
          'a ordem é do saque mais recente ao mais antigo\n'
          '----------------------\n'
          f'{ordenando_lista}\n'
          '----------------------\n'
          '#################\n')
    else:
        print("não foram realizadas movimentações!")

def main():
    deposito()
    while True:
        operacao = str(input("digite qual operação você quer realizar\n"
                         "(S) - Saque\n"
                         "(V) - Verificar saldo\n"
                         "(Q) - Sair\n")).lower()

        if operacao == 's':
            saque()

        elif operacao == 'v':
            verifica_saldo()

        elif operacao == 'q':
            extrato()
            break
        else:
            print("entrada inválida, por favor digite novamente!")

main()