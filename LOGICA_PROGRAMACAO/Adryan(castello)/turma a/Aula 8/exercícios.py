#Exercício 1
#Crie um algoritmo que pergunte o seu nome e trate erro ao inserir valores incorretos
# try:
#     nome = input("Digite seu nome")
# except NameError:
#     print("Erro, nome inválido")
# finally:
#     print("Nome correto")
primeiro_nome = int(input("Digite seu primeiro nome: "))
sobrenome = input("Digite seu sobrenome: ")
try:
    nome_completo = f"{primeiro_nome} {sobrenome}"
    print(f"Olá, {nome_completo}!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
