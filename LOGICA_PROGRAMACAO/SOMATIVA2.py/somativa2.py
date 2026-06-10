#1.Registro de Operador: Peça o nome do operador e o turno(A,B ou C). Exiba: "Operador [nome] registrado no turno [turno]. Boa jornada!". 

# import tkinter as tk
# from tkinter import messagebox, ttk

# def registrodeoperador():
# nome_operador = operador_nome.get()
# turno_operador = operador_turno.get()

#     if nome_operador == "" and turno_operador == "":
#         messagebox.showwarning("Aviso", "Por favor digite seu nome e turno :)")
#     else:
#         messagebox.showinfo(
#             "Sucesso",
#             f"Operador {nome_operador} registrado no turno {turno_operador}. Boa jornada!" )

# janela_registrodeoperador = tk.Tk()
# janela_registrodeoperador.title("Registro de Operador")
# janela_registrodeoperador.geometry("600x400")

# lbl_mensagem_operador = tk.Label(janela_registrodeoperador, text="Digite o nome do operador:")
# lbl_mensagem_operador.grid(row=0, column=0, pady=10, padx=10)

# lbl_mensagem_turno = tk.Label(janela_registrodeoperador, text="Digite seu turno:")
# lbl_mensagem_turno.grid(row=2, column=0, pady=10, padx=10)

# operador_nome = tk.Entry(janela_registrodeoperador, font= ("Arial",16), width=20)
# operador_nome.grid(row=0, column=1, pady=10, padx=10)
# operador_turno = tk.Entry(janela_registrodeoperador, font=("Arial", 16), width=20)
# operador_turno.grid(row=2, column=1, pady=10, padx=10)

# btn_registrar_operador = tk.Button(janela_registrodeoperador, text="Registra operário", command=registrodeoperador)
# btn_enviar_mensagem = tk.Button(janela_registrodeoperador, text="Enviar Mensagem", command=registrodeoperador, bg = "#9E2D11", fg="white", bd= 6, font=("Arial", 10, "bold"), width=14)
# btn_enviar_mensagem.grid(row=7, column=1, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela_registrodeoperador, text="Sair", command=janela_registrodeoperador.destroy, bg = "#000000" , fg="white", font=("Arial", 10, "bold"), width=14)
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)
# janela_registrodeoperador.mainloop()








#2.Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule eexiba quantas peças serão produzidas em um turno de 8 horas.
# import tkinter as tk
# from tkinter import messagebox, ttk

# def calcular_producao():
#     quantidade_pecas = int(input("Digite a quantidade de peças produzidas em 1 hora: "))
#     producao_turno = quantidade_pecas * 8
#     print(f"Em um turno de 8 horas, serão produzidas {producao_turno} peças.")
# if calcular_producao == "":
#     messagebox.showwarning("Aviso", "Por favor, digite a quantidade de peças produzidas em 1 hora.")
# else:
#     calcular_producao() 


# janela_calcular_producao.mainloop()







#3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar = 14.5PSI) e exiba com duas casas decimais.
# import tkinter as tk
# from tkinter import messagebox, ttk
# def Conversor_de_unidade():
#     if entry_bar.get() == "":
#         messagebox.showwarning( "Por favor, digite a pressão em Bar.")
#     else:
#         bar = float(entry_bar.get())
#         psi = bar * 14.5
#         messagebox.showinfo("Resultado", f"{bar} Bar é igual a {psi:.2f} PSI.")

# janela_conversor = tk.Tk()
# janela_conversor.title("Conversor de Unidade")
# janela_conversor.geometry("600x380")

# lbl_bar = tk.Label(janela_conversor, text="Digite a pressão em Bar:")
# lbl_bar.grid(row=0, column=0, pady=10, padx=10)
# entry_bar = tk.Entry(janela_conversor, font=("Arial", 12), width=20)
# entry_bar.grid(row=0, column=1, pady=10, padx=10)
# btn_converter = tk.Button(janela_conversor, text="Converter", command=Conversor_de_unidade, bg="#0B6C85", fg="white", font=("Dancing Script", 10, "bold"), width=14)
# btn_converter.grid(row=3, column=1, pady=10, padx=10)
# btn_fechar = tk.Button(janela_conversor, text="Fechar Programa", command=janela_conversor.destroy, bg="#000000", fg="white", font=("Dancing Script", 10, "bold"), width=14)
# btn_fechar.grid(row=3, column=0, pady=10, padx=10)
# janela_conversor.mainloop()






# #4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média aritmética simples delas.
# import tkiter as tk
# from tkinter import messagebox
# def Média de qualidade 





#5. Termostato Inteligente: Peça a temperatura de um motor.
# Abaixo de 40°C: "Baixa carga".
# Entre 40°C e 70°C: "Normal".
# Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox, ttk

# def temperatura():
#     temperatura_motor = motor_temperatura.get()

#     if temperatura_motor <= "40°C":
#         messagebox.showinfo("Aviso!", "Baixa Carga!")

#     elif temperatura_motor > "40°C" and temperatura_motor < "70°C":
#         messagebox.showinfo("Aviso", "Carga Normal!")

#     else:
#         messagebox.showinfo("Cuidado!",  "Resfriamento Ativado!")

# janela_temperatura = tk.Tk()
# janela_temperatura.title("Termostato Inteligente")
# janela_temperatura.geometry("600x450")

# lbl_mensagem_temp = tk.Label(janela_temperatura, text="Qual a temperatura atual? ")
# lbl_mensagem_temp.grid(row=1, column=1, pady=10, padx=10)
# motor_temperatura = tk.Entry(janela_temperatura, font= ("Arial", 12), width=25)
# motor_temperatura.grid(row=2, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_temperatura, text="Enviar", command=temperatura, bg = "#470B3F", fg= "white", font=("Arial", 10, "bold"), width=14)
# btn_enviar_mensagem.grid(row=6, column=1, pady=10, padx=10)

# btn_clicar_fechar = tk.Button(janela_temperatura, text="Fechar Programa", command=janela_temperatura.destroy, bg = "#000000", fg = "white", font=("Arial", 10, "bold"), width=14)
# btn_clicar_fechar.grid(row=7, column=1, pady=10, padx=10)

# janela_temperatura.mainloop()