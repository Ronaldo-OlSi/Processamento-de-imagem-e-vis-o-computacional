# Bibliotecas
import cv2
from matplotlib import pyplot as plt
import numpy as np
#import mahotas
import imutils

imagem = cv2.imread('entrada.pgm')
(b, g, r) = imagem[0, 0]
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)


def img_normal():
    # Leitura da imagem com a função imread()
    imagem = cv2.imread('entrada.pgm')

    print('Largura em pixels: ', end='')
    print(imagem.shape[1])  # largura da imagem
    print('Altura em pixels: ', end='')
    print(imagem.shape[0])  # altura da imagem
    print('Qtde de canais: ', end='')
    print(imagem.shape[2])
    cv2.imwrite("saida.jpg", imagem)
    # Mostra a imagem com a função imshow
    cv2.imshow("Amostra", imagem)
    cv2.waitKey(0)  # espera pressionar qualquer tecla
    # Salvar a imagem no disco com função imwrite()

def texto():

    imagem = cv2.imread('entrada.pgm')
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(imagem, 'Meu Texto!!!', (15, 65), fonte,
                2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imwrite("saida.jpg", imagem)
    cv2.imshow("Com Texto", imagem)
    cv2.waitKey(0)

def espelhar():

    img = cv2.imread('entrada.pgm')
    flip_horizontal = img[::-1, :]
    cv2.imwrite("saida.jpg", flip_horizontal)
    cv2.imshow("Flip Horizontal", flip_horizontal)

def espelhar_vertical():

    img = cv2.imread('entrada.pgm')
    flip_vertical = img[:, ::-1]
    cv2.imwrite("saida.jpg", flip_vertical)
    cv2.imshow("Flip Vertical", flip_vertical)

def espelhar_vert_hori():

    img = cv2.imread('entrada.pgm')
    flip_hv = cv2.flip(img, -1)
    cv2.imwrite("saida.jpg", flip_hv)
    cv2.imshow("Flip Horizontal e Vertical", flip_hv)
    cv2.waitKey(0)

def girar_1():

    # Girar a imagem
    img = cv2.imread('entrada.pgm')
    (alt, lar) = img.shape[:2]  # captura altura e largura
    centro = (lar // 2, alt // 2)  # acha o centro
    M = cv2.getRotationMatrix2D(centro, 30, 1.0)  # 30 graus
    img_rotacionada = cv2.warpAffine(img, M, (lar, alt))
    cv2.imwrite("saida.jpg", img_rotacionada)
    cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)
    cv2.waitKey(0)

def girar_2():

    # Girar a imagem
    img = cv2.imread('entrada.pgm')
    (alt, lar) = img.shape[:2]  # captura altura e largura
    centro = (lar // 2, alt // 2)  # acha o centro
    M = cv2.getRotationMatrix2D(centro, -30, 1.0)  # 30 graus
    img_rotacionada = cv2.warpAffine(img, M, (lar, alt))
    cv2.imwrite("saida.jpg", img_rotacionada)
    cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)
    cv2.waitKey(0)

def redimensionar():

    # Redimensiona a entrada
    img = cv2.imread('entrada.pgm')
    cv2.imshow("Original", img)
    proporcao = 100.0 / img.shape[1]
    tamanho_novo = (100, int(img.shape[0] * proporcao))
    img_redimensionada = cv2.resize(img, tamanho_novo,
                                    interpolation=cv2.INTER_AREA)
    cv2.imwrite("saida.jpg", img_redimensionada)
    cv2.imshow("Imagem redimensionada Pequena", img_redimensionada)
    cv2.waitKey(0)

def redimensionar2():

    # Redimensiona a entrada
    img = cv2.imread('entrada.pgm')
    cv2.imshow("Original", img)
    proporcao = 400.0 / img.shape[1]
    tamanho_novo = (400, int(img.shape[0] * proporcao))
    img_redimensionada = cv2.resize(img, tamanho_novo,
                                    interpolation=cv2.INTER_AREA)
    cv2.imwrite("saida.jpg", img_redimensionada)
    cv2.imshow("Imagem redimensionada Media", img_redimensionada)
    cv2.waitKey(0)

def redim_slicing():

    # Metodo Slicing de redimencionamento
    img = cv2.imread('entrada.pgm')
    cv2.imshow("Original", img)
    img_redimensionada = img[::2, ::2]
    cv2.imwrite("saida.jpg", img_redimensionada)
    cv2.imshow("Imagem redimensionada Slicing", img_redimensionada)
    cv2.waitKey(0)

def histo():

    img = cv2.imread('saida.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte P&B
    #Função calcular o hisograma da imagem
    h = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.figure()
    plt.title("Histograma")
    plt.xlabel("Intensidade")
    plt.ylabel("Qtde de Pixels")
    #plt.plot(h)
    #plt.xlim([0, 256])
    #plt.show()
    #cv2.waitKey(0)

    plt.hist(img.ravel(),256,[0,256])
    plt.show()
    #cv2.imwrite("Histograma.jpg", 0000)

def limiar():

    img = cv2.imread('entrada.pgm')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(img, (7, 7), 0)  # aplica blur
    (T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
    (T, binI) = cv2.threshold(suave, 160, 255,
                              cv2.THRESH_BINARY_INV)
    resultado = np.vstack([
        np.hstack([suave, bin]),
        np.hstack([binI, cv2.bitwise_and(img, img, mask=binI)])
    ])
    cv2.imwrite("saida.jpg", resultado)
    cv2.imshow("Binarização da imagem", resultado)
    cv2.waitKey(0)

def sobel():

    img = cv2.imread('entrada.pgm')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobel = cv2.bitwise_or(sobelX, sobelY)
    resultado = np.vstack([
    np.hstack([img, sobelX]),
    np.hstack([sobelY, sobel])
    ])
    cv2.imwrite("saida.jpg", resultado)
    cv2.imshow("Sobel", resultado)
    cv2.waitKey(0)

def bordas():

    img = cv2.imread('entrada.pgm')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(img, (7, 7), 0)
    canny1 = cv2.Canny(suave, 20, 120)
    canny2 = cv2.Canny(suave, 70, 200)
    resultado = np.vstack([
        np.hstack([img, suave]),
        np.hstack([canny1, canny2])
    ])
    cv2.imwrite("saida.jpg", resultado)
    cv2.imshow("Detector de Bordas Canny", resultado)
    cv2.waitKey(0)

'''
def reconhecimento():
    # Função para facilitar a escrita nas imagem
    def escreve(img, texto, cor=(255, 0, 0)):
        fonte = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(img, texto, (10, 20), fonte, 0.5, cor, 0,
                cv2.LINE_AA)
    imgColorida = cv2.imread('dados.jpg')  # Carregamento da imagem
    # Se necessário o redimensioamento da imagem pode vir aqui.
    # Passo 1: Conversão para tons de cinza
    img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)
    # Passo 2: Blur/Suavização da imagem
    suave = cv2.blur(img, (7, 7))
    # Passo 3: Binarização resultando em pixels brancos e pretos
    T = mahotas.thresholding.otsu(suave)
    bin = suave.copy()
    bin[bin > T] = 255
    bin[bin < 255] = 0
    bin = cv2.bitwise_not(bin)
    # Passo 4: Detecção de bordas com Canny
    bordas = cv2.Canny(bin, 70, 150)
    # Passo 5: Identificação e contagem dos contornos da imagem
    # cv2.RETR_EXTERNAL = conta apenas os contornos externos
    (lx, objetos, lx) = cv2.findContours(bordas.copy(),
                                         cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # A variável lx (lixo) recebe dados que não são utilizados
    escreve(img, "Imagem em tons de cinza", 0)
    escreve(suave, "Suavizacao com Blur", 0)
    escreve(bin, "Binarizacao com Metodo Otsu", 255)
    escreve(bordas, "Detector de bordas Canny", 255)
    temp = np.vstack([
        np.hstack([img, suave]),
        np.hstack([bin, bordas])
    ])
    cv2.imshow("Quantidade de objetos: " + str(len(objetos)), temp)
    cv2.waitKey(0)
    imgC2 = imgColorida.copy()
    cv2.imshow("Imagem Original", imgColorida)
    cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)
    escreve(imgC2, str(len(objetos)) + " objetos encontrados!")
    cv2.imshow("Resultado", imgC2)
    cv2.waitKey(0)
    cv2.imwrite("saida.jpg", img)'''