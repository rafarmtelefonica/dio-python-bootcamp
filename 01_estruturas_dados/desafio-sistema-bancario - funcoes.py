menu = """

[iu] Inserir novo usuário
[cc] Cadastrar conta
[lc] Listar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

LIMITE_SAQUES = 3
AGENCIA = "0001"
limite = 500

saldo = 0
extrato = ""
numero_saques = 0

usuarios = []
contas = []

def adicionar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    if(filtrar_usuario(cpf, usuarios)):
        print("Usuário já cadastrado.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")

    print("Agora vamos ao endereço.\n")
    rua = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")

    endereco = f"{rua}, {numero}, {bairro}, {cidade}/{uf}"

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if(usuario):
        print(f"Conta {numero_conta} criada com sucesso.")
        return {"agencia": agencia, "conta": numero_conta, "usuario": usuario}
    
    print(f"Usuário não encontrado. Cadastre o usuário com cpf {cpf} primeiro.")

def saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def deposito(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def listar_contas(contas):

    if(len(contas) == 0):
        print("Nenhuma conta cadastrada!\n")
        return

    for conta in contas:
        linha = f"""
            Agência: {conta["agencia"]}
            Conta: {conta["conta"]}
            Titular: {conta["usuario"]["nome"]}
        """
        print("#" * 30)
        print(linha)

while True:
            
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato = saque(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
    elif opcao == "e":
        imprimir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    elif opcao == "iu":
        adicionar_usuario(usuarios)

    elif opcao == "cc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
    
    elif opcao == "lc":
        listar_contas(contas)

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")