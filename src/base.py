import os
import cv2

imagem_dataset = cv2.imread("SOCOFing/Altered/Altered-Hard/150__M_Right_index_finger_Obl.BMP")

melhor_pontuacao = 0
nomearquivo = None
image = None

# Chaves compara
chave1, chave2, mp = None, None, None

contador = 0

# Cria os pares de pontos
for file in [file for file in os.listdir("SOCOFing/Real")][:1000]:

	imagem_digital = cv2.imread("SOCOFing/Real/" + file)
	sift = cv2.SIFT_create()

	pontochave_1, descriptors_1 = sift.detectAndCompute(imagem_dataset, None)
	pontochave_2, descriptors_2 = sift.detectAndCompute(imagem_digital, None)


	compara = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10},
									{}).knnMatch(descriptors_1, descriptors_2, k=2)


	verifica_pontos = []

