class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        soma = nums1 + nums2
        soma.sort()

        if len(soma) % 2 == 0:
            indice_meio = len(soma) // 2
            return (soma[indice_meio - 1] + soma[indice_meio]) / 2
        else:
            indice_meio = len(soma) // 2
            return soma[indice_meio]
