from datetime import datetime
import mysql.connector

# Estilizando
print("=" * 70)
print("Sistema de Monitoramento de Sustentabilidade Pessoal".center(70))
print("=" * 70)

# Conectando ao banco de dados MySQL
def conectar_banco():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Mb570619@@@",
        database="sustentabilidade"
    )

# Função para validar e formatar a data de entrada
def validar_data():
    while True:
        data = input("Qual é a data? (DD-MM-AAAA) ")
        try:
            data_formatada = datetime.strptime(data, "%d-%m-%Y")
            return data_formatada
        except ValueError:
            print("Data inválida! Certifique-se de digitar no formato DD-MM-AAAA.")

# Função para validar entradas numéricas
def obter_numero(mensagem):
    while True:
        entrada = input(mensagem).replace(",", ".")
        try:
            valor = float(entrada)
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número válido.")



# Função para validar a escolha do meio de transporte
def obter_transporte():
    transportes = []
    while True:
        

        try:
            opcao = int(input("Qual o meio de transporte você usou hoje?\n"
                              "1. Transporte público (ônibus, metrô, trem)\n"
                              "2. Bicicleta\n"
                              "3. Caminhada\n"
                              "4. Carro (combustível fóssil)\n"
                              "5. Carro elétrico\n"
                              "6. Carona compartilhada\n"
                              "Escolha uma das opções acima: "))
            if 1 <= opcao <= 6:
                transportes.append(opcao)
            else:
                print("Opção inválida! Escolha um número entre 1 e 6.")
            #pergunta ao usuario se ele usou outro metodo de transporte

            outro_transporte = input ("Você utilizou outro meio de transporte hoje: (sim/não) ").strip().lower()

            if outro_transporte != "sim":
                break
            else:
                print("Opção inválida! Escolha um número entre 1 e 6.")

        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            
    return transportes

def inserir_registro():
    data = validar_data()
    litros_agua = obter_numero("Quantos litros de água você consumiu hoje? (Aprox. em litros): ")
    energia_eletrica = obter_numero("Quantos kWh de energia elétrica você consumiu hoje? ")
    r_nao_reciclaveis = obter_numero("Quantos kg de resíduos não recicláveis você gerou hoje? ")
    residuos_reciclados = obter_numero("Qual a porcentagem de resíduos reciclados no total (em %)? ")
    meio_transporte = obter_transporte()

    print("=" * 70)
    if litros_agua < 150:
        print("Consumo de água: Alta Sustentabilidade")
    elif 150 <= litros_agua <= 200:
        print("Consumo de água: Moderada Sustentabilidade")
    else:
        print("Consumo de água: Baixa Sustentabilidade")

    if energia_eletrica < 5:
        print("Consumo de energia: Alta Sustentabilidade")
    elif 5 <= energia_eletrica <= 10:
        print("Consumo de energia: Moderada Sustentabilidade")
    else:
        print("Consumo de energia: Baixa Sustentabilidade")

    if residuos_reciclados > 50:
        print("Geração de Resíduos Não Recicláveis: Alta Sustentabilidade")
    elif 20 <= residuos_reciclados <= 50:
        print("Geração de Resíduos Não Recicláveis: Moderada Sustentabilidade")
    else:
        print("Geração de Resíduos Não Recicláveis: Baixa Sustentabilidade")

    if meio_transporte in [1, 2, 3, 5]:
        print("Uso de Transporte: Alta Sustentabilidade")
    elif meio_transporte == 6:
        print("Uso de Transporte: Moderada Sustentabilidade")
    else:
        print("Uso de Transporte: Baixa Sustentabilidade")

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        comando = """
            INSERT INTO registros 
            (data_registro, litros_agua, energia_kwh, residuos_nao_reciclaveis, percentual_reciclado, meio_transporte)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            data.date(), litros_agua, energia_eletrica,
            r_nao_reciclaveis, residuos_reciclados, meio_transporte
        )

        cursor.execute(comando, valores)
        conexao.commit()
        print("Dados inseridos com sucesso no banco de dados.")

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ou inserir dados no banco: {erro}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

# Função para listar registros
def listar_registros():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, data_registro FROM registros ORDER BY data_registro DESC")
        resultados = cursor.fetchall()

        print("\nRegistros disponíveis:")
        for row in resultados:
            print(f"ID: {row[0]} | Data: {row[1].strftime('%d-%m-%Y')}")

        return resultados

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar registros: {erro}")
        return []

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

# Função para atualizar um registro
def atualizar_registro():
    registros = listar_registros()
    if not registros:
        print("Nenhum registro para atualizar.")
        return

    try:
        id_escolhido = int(input("Digite o ID do registro que deseja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    print("\nInforme os novos dados para o registro:")
    nova_data = validar_data()
    novo_consumo_agua = obter_numero("Novo consumo de água (litros): ")
    nova_energia = obter_numero("Novo consumo de energia elétrica (kWh): ")
    novos_residuos = obter_numero("Nova quantidade de resíduos não recicláveis (kg): ")
    novo_percentual = obter_numero("Nova porcentagem de resíduos reciclados (%): ")
    novo_transporte = obter_transporte()

    print("=" * 70)
    if novo_consumo_agua < 150:
        print("Consumo de água: Alta Sustentabilidade")
    elif 150 <= novo_consumo_agua <= 200:
        print("Consumo de água: Moderada Sustentabilidade")
    else:
        print("Consumo de água: Baixa Sustentabilidade")

    if nova_energia < 5:
        print("Consumo de energia: Alta Sustentabilidade")
    elif 5 <= nova_energia <= 10:
        print("Consumo de energia: Moderada Sustentabilidade")
    else:
        print("Consumo de energia: Baixa Sustentabilidade")

    if novo_percentual > 50:
        print("Geração de Resíduos Não Recicláveis: Alta Sustentabilidade")
    elif 20 <= novo_percentual <= 50:
        print("Geração de Resíduos Não Recicláveis: Moderada Sustentabilidade")
    else:
        print("Geração de Resíduos Não Recicláveis: Baixa Sustentabilidade")

    if novo_transporte in [1, 2, 3, 5]:
        print("Uso de Transporte: Alta Sustentabilidade")
    elif novo_transporte == 6:
        print("Uso de Transporte: Moderada Sustentabilidade")
    else:
        print("Uso de Transporte: Baixa Sustentabilidade")

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        comando = """
            UPDATE registros
            SET data_registro = %s,
                litros_agua = %s,
                energia_kwh = %s,
                residuos_nao_reciclaveis = %s,
                percentual_reciclado = %s,
                meio_transporte = %s
            WHERE id = %s
        """
        valores = (
            nova_data.date(),
            novo_consumo_agua,
            nova_energia,
            novos_residuos,
            novo_percentual,
            novo_transporte,
            id_escolhido
        )

        cursor.execute(comando, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Registro atualizado com sucesso.")
        else:
            print("Nenhum registro encontrado com esse ID.")

    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar dados: {erro}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

# Função para excluir um registro
def excluir_registro():
    registros = listar_registros()
    if not registros:
        print("Nenhum registro para excluir.")
        return

    try:
        id_escolhido = int(input("Digite o ID do registro que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        comando = """
            DELETE FROM registros
            WHERE id = %s
        """
        cursor.execute(comando, (id_escolhido,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Registro excluído com sucesso.")
        else:
            print("Nenhum registro encontrado com esse ID.")

    except mysql.connector.Error as erro:
        print(f"Erro ao excluir dados: {erro}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()


def listar_e_classificar_monitoramentos():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM registros ORDER BY data_registro DESC")
        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhum registro encontrado.")
            return

        print("\nMonitoramentos cadastrados e classificações:")
        for registro in resultados:
            print(f"\nID: {registro['id']} | Data: {registro['data_registro'].strftime('%d-%m-%Y')}")

            # Consumo de água
            if registro['litros_agua'] < 150:
                print("  Consumo de água: Alta Sustentabilidade")
            elif 150 <= registro['litros_agua'] <= 200:
                print("  Consumo de água: Moderada Sustentabilidade")
            else:
                print("  Consumo de água: Baixa Sustentabilidade")

            # Consumo de energia
            if registro['energia_kwh'] < 5:
                print("  Consumo de energia: Alta Sustentabilidade")
            elif 5 <= registro['energia_kwh'] <= 10:
                print("  Consumo de energia: Moderada Sustentabilidade")
            else:
                print("  Consumo de energia: Baixa Sustentabilidade")

            # Resíduos reciclados
            if registro['percentual_reciclado'] > 50:
                print("  Resíduos reciclados: Alta Sustentabilidade")
            elif 20 <= registro['percentual_reciclado'] <= 50:
                print("  Resíduos reciclados: Moderada Sustentabilidade")
            else:
                print("  Resíduos reciclados: Baixa Sustentabilidade")

            # Transporte
            transporte = registro['meio_transporte']
            if transporte in [1, 2, 3, 5]:
                print("  Transporte: Alta Sustentabilidade")
            elif transporte == 6:
                print("  Transporte: Moderada Sustentabilidade")
            else:
                print("  Transporte: Baixa Sustentabilidade")

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar registros: {erro}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()


def calcular_medias_e_classificar():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM registros")
        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhum registro encontrado.")
            return

        total_registros = len(resultados)

        soma_agua = sum(r['litros_agua'] for r in resultados)
        soma_energia = sum(r['energia_kwh'] for r in resultados)
        soma_residuos = sum(r['percentual_reciclado'] for r in resultados)

        media_agua = soma_agua / total_registros
        media_energia = soma_energia / total_registros
        media_residuos = soma_residuos / total_registros

        print("\nMÉDIAS DOS PARÂMETROS:")

        # Classificação água
        if media_agua < 150:
            print(f"  Média consumo água: {media_agua:.2f}L - Alta Sustentabilidade")
        elif 150 <= media_agua <= 200:
            print(f"  Média consumo água: {media_agua:.2f}L - Moderada Sustentabilidade")
        else:
            print(f"  Média consumo água: {media_agua:.2f}L - Baixa Sustentabilidade")

        # Classificação energia
        if media_energia < 5:
            print(f"  Média consumo energia: {media_energia:.2f}kWh - Alta Sustentabilidade")
        elif 5 <= media_energia <= 10:
            print(f"  Média consumo energia: {media_energia:.2f}kWh - Moderada Sustentabilidade")
        else:
            print(f"  Média consumo energia: {media_energia:.2f}kWh - Baixa Sustentabilidade")

        # Classificação resíduos
        if media_residuos > 50:
            print(f"  Média resíduos reciclados: {media_residuos:.2f}% - Alta Sustentabilidade")
        elif 20 <= media_residuos <= 50:
            print(f"  Média resíduos reciclados: {media_residuos:.2f}% - Moderada Sustentabilidade")
        else:
            print(f"  Média resíduos reciclados: {media_residuos:.2f}% - Baixa Sustentabilidade")

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar registros: {erro}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()








# Função do menu principal
# Função do menu principal
def menu():
    while True:
        print("\nO que você deseja fazer?")
        print("1. Inserir novo registro")
        print("2. Atualizar um registro existente")
        print("3. Listar um registro existente")
        print("4. Visualizar a média dos registros")
        print("5. Excluir um registro")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_registro()
        elif opcao == '2':
            atualizar_registro()
        elif opcao == '3':
            listar_e_classificar_monitoramentos()  
        elif opcao == '4':
            calcular_medias_e_classificar()
        elif opcao == '5':
            excluir_registro()
        elif opcao == '6':
            print("Encerrando o programa. Até logo.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()