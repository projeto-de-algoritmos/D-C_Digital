from typing import List
class Solution:
    
	def findPeakGrid(self, mat: List[List[int]]) -> List[int]:  

		def findPeakElement(numeros: List[int]) -> int:
			direita = len(numeros) -1
			esquerda = 0

            #encontramos horizontalmente os indices com valores máximos em todas as linhas
			while esquerda < direita:

				metade =  esquerda + int((direita-esquerda)/2)

				if numeros[metade] < numeros[metade + 1]: # numero peak a direita
					esquerda = metade + 1
				else:
					direita = metade
			return esquerda
            
        #achado esses valores maximos de cada linha, expandimos agora verticalmente
		def condition(mat, i, j):

			if j + 1 > len(mat[0]) - 1:
				if mat[i][j] > mat[i][j - 1]:
					return True

			elif j - 1 < 0:
				if mat[i][j] > mat[i][j + 1]:
					return True

			else:
				if mat[i][j + 1] < mat[i][j] > mat[i][j - 1]:
					return True

        #aqui ele garante a condicao de que o numero peak é maior que todos os seus vizinhos
		for idex in range(len(mat)):
			# encontra o valor maximo de cada fila         
			temporario = 0

			for j in range(len(mat[idex])):
				if mat[idex][j] >= mat[idex][temporario]:
					temporario = j

			numeros = [mat[i][temporario] for i in range(len(mat))]
			index = findPeakElement(numeros)

			if condition(mat,  index, temporario):
				return [index, temporario]
