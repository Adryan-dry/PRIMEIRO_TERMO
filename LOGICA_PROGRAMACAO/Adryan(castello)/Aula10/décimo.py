# Tratamento de Erros e Depuração
#try e except são usados para lidar como erros de forma controlada, evitando que o programa quebre. O código dentro do bloco try é  executado  normalmente, mas se ocorrer um erro, o controle é passado para o bloco except, onde podemos lidar com a situação de forma apropriada.

# try:
#     numero = int(input("Digite um número")) 
#     resultado = 10/ numero 
#     print("O resultado é:", resultado)
# except ValueError:
#     print("Erro: Você deve digitar um número válido.")

#  except ZeroDivisionError:
#       print("Erro: Não possível dividir por zero.")

# except KeyboardInterrupt:
#     print("/n Programa interrompido")

# except TypeError:
#     print("Erro: Tipo de dado inválido")

# except Exception as erro:
#     print("Erro inesperado:" erro)

#Exercício 1
#Escreva um programa que solicite ao usuário calcule a média de três números. O programa  deve lidar com possíveis erros, como a entrada de valores não numéricos ou a divisão por zero.

# try:
#    n1 = int(input("Qual o primeiro valor?"))
#    n2 = int(input("Qual o segundo valor?"))
#    n3 = int(input("Qual o terceiro valor?"))
#    media = (n1 + n2 + n3 / 3)
#    print("A media é:",media)
# except  ValueError:
#      print("Por favor, digite somente números inteiros")
     
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero")

# # finally:
#     media = n1 + n2 + n3 /3


#Explicação de def: A palavra-chave "def" é usada para definir uma funçaõ em Python. Uma função é um bloco de código reutilizável que realiza uma tarefa específica.
#return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a função foi chamada.
# O valor retornado pode ser usado posteriormente no código.

# #def nome_da_função(parametro1, parametro2):
#     Corpo da função (código que será)
#resultado = parametro1 + parametro2
#return resultado
#Exemplo 1 
#def saudacao(nome, idade):
#     return f"Olá, {nome},{idade}!"
# print(saudacao("Bruno", "36 anos"))
# print(saudacao("Adryan","16 anos"))

#Exemplo 2
def calcular_media(num1, num2, num3):
    try:
        media = (num1 + num2 + num3) /3
        return media
    except TypeError:
        return "Erro : Todos os valores devem ser números."
    except ZeroDivisionError:
     return "Erro: Não é possível dividir por zero."
print(calcular_media(10, 20,30))
