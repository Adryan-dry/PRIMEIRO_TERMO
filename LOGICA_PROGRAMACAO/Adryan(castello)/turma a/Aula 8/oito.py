#Tratamento de Erros e Exceções
# print("Cálculo de divisões")
# valor1 = int(input("Digite o primeiro valor"))
# valor2 = int(input("Digite o primeiro valor"))
# resultado = valor1 / valor2
# print(f"O resultado da divisão é: {resultado}")


# O código acima pode gerar um erro de divisão por zero se o usuário digitar 0 para o segundo valor. Para tratar esse erro, podemos usar um bloco try-except:
#Exemplo 1 : Tratamento de divisão por zero

# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")

# #Exemplo 2: Tratamento de entrada inválida 
# try:
#     valor1 = int(input("Digite o primeiro valor"))
#     valor2 = int(input("Digite o segundo valor"))
#     resultado = valor1 / valor2 
#     print(f"O resultado da divisão é: {resultado}")
# except ValueError:
#     print("Erro de valor: Por favor, digite um número inteiro válido")
# except ZeroDivisionError: 
#     print("Não é possível dividir por zero")

# # Exemplo 3: Tratamento de múltiplas exceções
# try:
#     valor1 = int(input("Digite o primeiro valor"))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de valor: Por favor, digite um número inteiro válido. {e} ou Erro: Não é possível dividir por zero. {e}")
# finally:
#     print("Bloco finally executado.")

# Exemplo 4: Uso do bloco finally
# try:
#     valor1 = int(input("Digite o primeiro valor"))
#     valor2 = int(input("Digite o segundo valor"))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de value: Por favor, digite um número inteiro válido. {e} ou Erro: Não é possível dividir por zero. {e}")
# finally:
#     print("Bloco finally executado.")

#Exemplo 5: TypeError
# try:
#     resultado = "5" + 10
# except TypeError as e:
#     print("Erro de tipo: {e}")

               #PROJETO
#Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
#Toda entrada e saída será sinalizada 
#Valores para entrada e permanência do veículo deverá ser perguntado 
#As entradas deverão ser registradas por placas.
#Passo 1: Ao parar na cancela é necessário um sensor para ler as tags no vidro.
#Passo 1:
# -Quando o veículo chegar o sensor de presença no solo ou em forma de câmera, deve ser ativado e emitir um som: Bem-Vindo ao SmartParking.
# -Um outro sensor automaticamente lê as taggy do vidro.
#Passo 2:
# -Caso o motorista não tenha a taggy, ele precisa pressionar o botão do Totem.
# -Ao pressionar, diga: Retire seu ticket, automaticamente a cancela levanta para o veículo passar.
#Perguntar as informações sobre o veículo ou forma de acesso
# Pressionar o botão para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário
#
#Passo 2:
# Verificar tempo de permanência 
# Valor a ser cobrado
#  
#Passo 3:
# Saída como será?
#Se for taggy gerar na fatura da taggy 
#Pagar ticket
#Devolver ticket na saída 
#Passo 4
#Gerar relatorio de entradas e saidas
#Tratamento de Erros
#Revisão do código
#
#
# if veiculo tem tag