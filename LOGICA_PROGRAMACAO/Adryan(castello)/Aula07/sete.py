# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O jogador [nick] está no nível [nível] e pronto para a partida!"
# print ("Perfil de Gamer - Seja bem-vindo Jogador!")
# nome_jogador = input("Qual é o nick do Jogador:? ")
# nivel_jogador = input ("Qual é o nível do Jogador:?")
# print(f"O jogador {nome_jogador} está no nível {nivel_jogador} e pronto para a partida!")
 
#2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e multiplique por 4 para mostrar quanto ele terá no final do mês.
# print("Calculadora de Mesada")
# valor_semana = float(input("Qual o valor que você recebeu?"))
# total_mes = valor_semana *4
# print(f"Sua mesada no final do mês será de... {total_mes}")

#Manipulação de arquivos e texto
# manipular_texto = "Python é Muito legal"
# print(manipular_texto.strip().upper()) #"Python"
# print(manipular_texto.strip().lower()) #"Python"
# print(manipular_texto.strip().startswith("A"))#"Começar com Letra Inicial"
# print(manipular_texto.strip().capitalize()) #"Letras Inicial"
# print(manipular_texto.strip().title())#"Título"
# print(manipular_texto.strip().replace(" "," ")) #"Preencher vazios"
# print(manipular_texto.strip().split()) #"Separar palavras"

#Exercício 1:
#Crie um programa que peça ao usuário para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
# - Deixe o texto em letra minúsculas.
# frase_usuario = input("Digite uma frase: ")
# print(frase_usuario.strip().lower())

#Manipular arquivos:
#Escrevendo
# with open ("notas.txt", "w", encoding="utf-8") as texto:
#     texto.write("Estudar Python hoje")
#     texto.write("/nLer sobre Clean Code.")
#     texto.write("/nEstamos evoluindo")
 
# #Lendo
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)

# #Exemplo 1
# #Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo. Exiba o resultado para o usuário.
# print("Contagem de palavras em arquivo")
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("PYTHON")#Contar a palavra "Python"
#     contagem = conteudo.lower().count("python")
#     CONT = conteudo.upper().count("Python") #Contar a palavra"Python
#     print(f"A contagem de palavras {contagem} é de...")


# Interação com o sistema operacional
import os # importa o módulo os para interagir com o sistema operacional

# Onde estou?
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C:/Users"))


# Criar pastas

# os.mkdir("Adryan")
# Criar arquivos

# Renomear pastas
# os.rename("Adryan", "Minha_Pasta")

# # Apagar pastas
# os.rmdir("Minha_Pasta")

# Complemento de comandos uteis