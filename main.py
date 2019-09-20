from tkinter import *
from operacoes import *

janela = Tk()
janela.geometry("780x380")
janela.title("Manipulação de Imagens")
heading = Label(text = "Manipulação de Imagens", bg = "#cee5eb", fg = "black",
                width = "500", height = "3")
heading.pack()

normal = Button(janela, text = "Imagem Normal", width = "30", height = "2", command = img_normal, bg = "#7dc7dc")
normal.place(x = 70, y = 70)

espelhar = Button(janela, text = "Espelhar Vertical", width = "30", height = "2", command = espelhar, bg = "#7dc7dc")
espelhar.place(x = 70, y = 120)

espelhar_vertical = Button(janela, text = "Espelhar Horizontal", width = "30", height = "2", command = espelhar_vertical, bg = "#7dc7dc")
espelhar_vertical.place(x = 70, y = 170)

es_vh = Button(janela, text = "Espelhar Vetical e Horizontal", width = "30", height = "2", command = espelhar_vert_hori, bg = "#7dc7dc")
es_vh.place(x = 70, y = 220)

texto = Button(janela, text = "Por Texto na Imagem", width = "30", height = "2", command = texto, bg = "#7dc7dc")
texto.place(x = 70, y = 270)

girar_2 = Button(janela, text = "Girar Direita 30º", width = "30", height = "2", command = girar_2, bg = "#7dc7dc")
girar_2.place(x = 300, y = 70)

girar_1 = Button(janela, text = "Girar Esquerda 30º", width = "30", height = "2", command = girar_1, bg = "#7dc7dc")
girar_1.place(x = 300, y = 120)

Slicing = Button(janela, text = "Redimensionar Slicing", width = "30", height = "2", command = redim_slicing, bg = "#7dc7dc")
Slicing.place(x = 300, y = 170)

redi = Button(janela, text = "Redimensionar Pequeno", width = "30", height = "2", command = redimensionar, bg = "#7dc7dc")
redi.place(x = 300, y = 220)


redimensionar2 = Button(janela, text = "Redimensionar Médio", width = "30", height = "2", command = redimensionar2, bg = "#7dc7dc")
redimensionar2.place(x = 300, y = 270)



histograma = Button(janela, text = "Histograma", width = "30", height = "2", command = histo, bg = "#7dc7dc")
histograma.place(x = 530, y = 70)

sobel = Button(janela, text = "Sobel", width = "30", height = "2", command = sobel, bg = "#7dc7dc")
sobel.place(x = 530, y = 120)

bordas = Button(janela, text = "Detectar Bordas", width = "30", height = "2", command = bordas, bg = "#7dc7dc")
bordas.place(x = 530, y = 170)

lim = Button(janela, text = "Limiarização", width = "30", height = "2", command = limiar, bg = "#7dc7dc")
lim.place(x = 530, y = 220)

histograma = Button(janela, text = "0000", width = "30", height = "2", command = histo, bg = "#7dc7dc")
histograma.place(x = 530, y = 270)

lb = Label(janela, text = "STATUS", bg = "#cee5eb")
lb.place(x = 435, y = 315)
lb11 = Label(janela, text = "DICA: Use Tab para navegar!", bg = "#cee5eb")
lb11.place(x = 90, y = 315)

janela.mainloop()