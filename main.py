equacao1 = str(input("Insira uma equação simples: "))


def limpeza(equacao):
    return equacao.replace(" ", "")


def ponteiro(equacao):
    for item, letra in enumerate(equacao):
        if not letra.isalnum():
            return item


def operacao(num_1, num_2, operador):
    match operador:
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "*":
            return num_1 * num_2
        case "/":
            return num_1 / num_2


def calculadora(equacao_suja):
    equacao_limpa = limpeza(equacao_suja)
    ponteiro_1 = ponteiro(equacao_limpa)
    parte_1 = ""
    for item in range(0, ponteiro_1):
        parte_1 += equacao_limpa[item]
    numeros_parte_1 = int(parte_1)
    parte_2 = ""
    for item in range(ponteiro_1 + 1, len(equacao_limpa)):
        parte_2 += equacao_limpa[item]
    numeros_parte_2 = int(parte_2)
    sinal = equacao_limpa[ponteiro_1]
    return operacao(numeros_parte_1, numeros_parte_2, sinal)


print(calculadora(equacao1))
