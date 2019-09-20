from tkinter import *
from operacoes import *

janela = Tk()
janela.geometry("950x380")
janela.title("Manipulação de Imagens")
heading = Label(text = "Manipulação de Imagens", bg = "#cee5eb", fg = "black",
                width = "500", height = "3")
heading.pack()

analize= Button(janela, text = "Analize Cor", width = "10", height = "2", command = analize, bg = "#7dc7dc")
analize.place(x = 20, y = 120)

Aterar_cor = Button(janela, text = "Aterar cor", width = "10", height = "2", command = aterar_cor, bg = "#7dc7dc")
Aterar_cor.place(x = 20, y = 170)

normal = Button(janela, text = "Imagem Normal", width = "25", height = "2", command = img_normal, bg = "#7dc7dc")
normal.place(x = 110, y = 70)

espelhar = Button(janela, text = "Espelhar Vertical", width = "25", height = "2", command = espelhar, bg = "#7dc7dc")
espelhar.place(x = 110, y = 120)

espelhar_vertical = Button(janela, text = "Espelhar Horizontal", width = "25", height = "2", command = espelhar_vertical, bg = "#7dc7dc")
espelhar_vertical.place(x = 110, y = 170)

es_vh = Button(janela, text = "Espelhar Vetical e Horizontal", width = "25", height = "2", command = espelhar_vert_hori, bg = "#7dc7dc")
es_vh.place(x = 110, y = 220)

texto = Button(janela, text = "Por Texto na Imagem", width = "25", height = "2", command = texto, bg = "#7dc7dc")
texto.place(x = 110, y = 270)

girar_2 = Button(janela, text = "Girar Direita 30º", width = "25", height = "2", command = girar_2, bg = "#7dc7dc")
girar_2.place(x = 300, y = 70)

girar_1 = Button(janela, text = "Girar Esquerda 30º", width = "25", height = "2", command = girar_1, bg = "#7dc7dc")
girar_1.place(x = 300, y = 120)

Slicing = Button(janela, text = "Redimensionar Slicing", width = "25", height = "2", command = redim_slicing, bg = "#7dc7dc")
Slicing.place(x = 300, y = 170)

redi = Button(janela, text = "Redimensionar Pequeno", width = "25", height = "2", command = redimensionar, bg = "#7dc7dc")
redi.place(x = 300, y = 220)

redimensionar2 = Button(janela, text = "Redimensionar Médio", width = "25", height = "2", command = redimensionar2, bg = "#7dc7dc")
redimensionar2.place(x = 300, y = 270)

blur = Button(janela, text = "Blur", width = "25", height = "2", command = blur, bg = "#7dc7dc")
blur.place(x = 490, y = 70)

sobel = Button(janela, text = "Sobel", width = "25", height = "2", command = sobel, bg = "#7dc7dc")
sobel.place(x = 490, y = 120)

bordas = Button(janela, text = "Detectar Bordas", width = "25", height = "2", command = bordas, bg = "#7dc7dc")
bordas.place(x = 490, y = 170)

lim = Button(janela, text = "Limiarização", width = "25", height = "2", command = limiar, bg = "#7dc7dc")
lim.place(x = 490, y = 220)

color = Button(janela, text = "Cor Solida", width = "25", height = "2", command = colorir, bg = "#7dc7dc")
color.place(x = 490, y = 270)

dif = Button(janela, text = "Difusão", width = "25", height = "2", command = difusao, bg = "#7dc7dc")
dif.place(x = 680, y = 70)

pontos = Button(janela, text = "Pontos", width = "25", height = "2", command = pontos, bg = "#7dc7dc")
pontos.place(x = 680, y = 120)

fatiar = Button(janela, text = "Fatiar", width = "25", height = "2", command = fatiar, bg = "#7dc7dc")
fatiar.place(x = 680, y = 170)

filtro_cor = Button(janela, text = "Filtro Colorido", width = "25", height = "2", command = filtro_cor, bg = "#7dc7dc")
filtro_cor.place(x = 680, y = 220)

histograma = Button(janela, text = "Histograma", width = "25", height = "2", command = histo, bg = "#7dc7dc")
histograma.place(x = 680, y = 270)

lb11 = Label(janela, text = "DICA: Use Tab para navegar, espaço para selecionar. Alt F4 para fechar!", bg = "#cee5eb")
lb11.place(x = 110, y = 335)

janela.mainloop()