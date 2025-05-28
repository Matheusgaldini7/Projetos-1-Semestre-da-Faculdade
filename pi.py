def cadastro_data():
    while True:
        try:
            data = input("Digite a data de hoje (DD/MM/YYYY): ")

            if not all(caractere.isdigit() or caractere == "/" for caractere in data):
                print("A data deve conter somente números. Tente novamente.")
                continue

            data = data.replace("/", "")

            if len(data) != 8:
                print("A data deve ter somente 8 dígitos numéricos, tente novamente.")
                continue

            dia, mes, ano = int(data[:2]), int(data[2:4]), int(data[4:])

            if dia < 1 or dia > 31:
                print("Digite um dia válido, entre 01 e 31.")
                continue

            if mes < 1 or mes > 12:
                print("Digite um mês válido, o mês deve estar entre 01 e 12.")
                continue

            if mes == 2 and dia > 28:
                print("O mês de fevereiro tem somente até o dia 28.")
                print("Digite outro dia, entre 01 e 28.")
                continue

            break

        except ValueError:
            print("A data deve conter somente números. Tente novamente.")  

    return f"{dia:02d}/{mes:02d}/{ano}"

data = cadastro_data()
print(f"Data cadastrada: {data}")



while True:
    try:
        consumo_agua = float(input("Digite quanto você consumiu de água hoje (em litros): "))
        if consumo_agua < 0:
            print("O consumo de água não pode ser negativo. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print(f"Consumo de água registrado: {consumo_agua} litros")

while True:
    try:
        consumo_kWh = float(input("Quantos kWh você consumiu de energia elétrica hoje: "))
        if consumo_kWh < 0:
            print("O consumo de energia não pode ser negativo. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print(f"Consumo de energia elétrica registrado: {consumo_kWh} kWh")

while True:
    try:
        consumo_residuos = float(input("Quantos kg de resíduos não recicláveis você gerou hoje: "))
        if consumo_residuos < 0:
            print("A quantidade de resíduos não pode ser negativa. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print(f"Consumo de resíduos não recicláveis registrado: {consumo_residuos} kg")

while True:
    try:
        consumo_reciclado = float(input("Qual a porcentagem de resíduos reciclados no total (em %): "))
        if not 0 <= consumo_reciclado <= 100:
            print("A porcentagem deve estar entre 0 e 100. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print(f"Consumo de resíduos reciclados registrado: {consumo_reciclado}%")

def meio_tranportes():

    list_opcoes = [
        "1. Transpotes públicos(Metro, Trem, Ônibus)",
        "2. Bicicleta",
        "3. Caminhada",
        "4. Carro",
        "5. Carro elétrico",
        "6. Carona compartilhada",
    ]
    while True:
        print("Qual opção de Transporte voce utilizou hoje: ")
        for opção in list_opcoes:
            print(opção)
        try:
            transporte = int(input("Selecione qual opção de transporte voce utilizou hoje: "))
            if transporte < 1 or transporte > 6:
                print("Opção inválida. Por favor, escolha um número entre 1 e 6.")
                continue

            print(f"Você escolheu a opção de transporte: {list_opcoes[transporte - 1]}")
            return list_opcoes[transporte - 1]
        
        except ValueError:
            print("Entrada inválida! Digite uma opção numérica entre 1 e 6.")

transporte = meio_tranportes()
print(f"Transporte escolhido: {transporte}")

sustentabilidade = "Sustentabilidade" 
if consumo_agua < 150:
    sustentabilidade += " Consumo de água: Alta Sustentabilidade."
elif 150 <= consumo_agua <= 200:
    sustentabilidade += "Consumo de água: Moderada Sustentabilidade."
else:
    sustentabilidade += "Consumo de água: Baixa Sustentabilidade."

if consumo_kWh < 5:
    sustentabilidade += "Consumo de energia: Alta Sustentabilidade."
elif 5 <= consumo_kWh <= 10:
    sustentabilidade += " Consumo de energia: Moderada Sustentabilidade."
else:
    sustentabilidade += " Consumo de energia: Baixa Sustentabilidade."

if consumo_reciclado > 50:
    sustentabilidade += "Geração de Resíduos Não Recicláveis: Alta Sustentabilidade."
elif 20 <= consumo_reciclado <= 50:
    sustentabilidade += "Geração de Resíduos Não Recicláveis: Moderada Sustentabilidade."
else:
    sustentabilidade += " Geração de Resíduos Não Recicláveis: Baixa Sustentabilidade."

if transporte in ["2. Bicicleta", "3. Caminhada", "5. Carro elétrico", "1. Transportes públicos (Metrô, Trem, Ônibus)"]:
    sustentabilidade += "Uso de Transporte: Alta Sustentabilidade."
else:
    sustentabilidade += "Uso de Transporte: Moderada Sustentabilidade."

print(sustentabilidade)