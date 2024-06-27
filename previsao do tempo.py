import requests
from tkinter import *

API_KEY = "ba7283eeaae1db8437785f7ea257dee1"

def VerClima():
    cidade = entrada_cidade.get()  
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    if requisicao.status_code == 200:
        descricao = requisicao_dic['weather'][0]['description']
        temperatura_atual = requisicao_dic['main']['temp'] - 273.15  
        temperatura_minima = requisicao_dic['main']['temp_min'] - 273.15  
        temperatura_maxima = requisicao_dic['main']['temp_max'] - 273.15  

        resultado.config(text=f"Descrição do clima: {descricao}\n"
                              f"Temperatura Atual: {temperatura_atual:.2f}°C\n"
                              f"Temperatura Mínima: {temperatura_minima:.2f}°C\n"
                              f"Temperatura Máxima: {temperatura_maxima:.2f}°C")
    else:
        resultado.config(text="Cidade não encontrada. Verifique o nome e tente novamente.")


janela = Tk()
janela.title('Previsão do Tempo')

#
largura_janela = 400
altura_janela = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2
janela.geometry(f'{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}')


texto = Label(janela, text='Digite o nome da cidade para saber o clima:')
texto.pack(pady=10)


entrada_cidade = Entry(janela, width=30)
entrada_cidade.pack()


botao = Button(janela, text="Obter Previsão", command=VerClima)
botao.pack(pady=10)

resultado = Label(janela, text="", wraplength=300, justify="left")
resultado.pack(pady=10)

janela.mainloop()