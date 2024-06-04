
def validacao_cpf(cpf):
    
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf)!= 11:
        return False

    sum = 0
    valor = 10
    for n in range(9):
        sum = sum + int(cpf[n]) * valor
        valor = valor - 1
    verificando_digito = (sum * 10) % 11
    if verificando_digito == 10:
        verificando_digito = 0
    if cpf[9]!= str(verificando_digito):
        return False

    sum = 0
    valor = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * valor
        valor = valor - 1
    verificando_digito = (sum * 10) % 11
    if verificando_digito == 10:
        verificando_digito = 0
    if cpf[10]!= str(verificando_digito):
        return False

    return True

cpf = input("Digite um CPF: ")
if validacao_cpf(cpf):
    print("CPF valido!")
else:
    print("CPF invalido!")
    