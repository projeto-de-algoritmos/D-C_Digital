from typing import List
class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numeros_do_array = self.mergesort(nums)
        numeros_do_array.reverse()
        return numeros_do_array[k-1]
        
    #divide o array ao meio
    def mergesort(self, nums):
        if len(nums) == 1:
            return nums
        meio = len(nums)//2

     #seleciona cada meta, esquerda e direita   
        esquerdo = nums[:meio]
        direito = nums[meio:]
        
    #chama a funcao recursiva
        esquerdo = self.mergesort(esquerdo)
        direito = self.mergesort(direito)
        
        nums = self.merge(esquerdo, direito)
        return nums
    #da merge nos itens que foram divididos do array original
    def merge(self, esquerdo, direito):
        if len(esquerdo) == 0:
            return direito
        elif len(direito) == 0:
            return esquerdo
            
     # caso existam numeros que sobrarem, ele reorganiza   
        array = []
        aux, axu2 = 0, 0
        while aux < len(esquerdo) and axu2 < len(direito):
            if esquerdo[aux] < direito[axu2]:
                array.append(esquerdo[aux])
                aux += 1
            else:
                array.append(direito[axu2])
                axu2 += 1
        
        while aux < len(esquerdo):
            array.append(esquerdo[aux])
            aux += 1
        
        while axu2 < len(direito):
            array.append(direito[axu2])
            axu2 += 1
        return array