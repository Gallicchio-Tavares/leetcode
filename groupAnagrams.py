from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        dict = defaultdict(list) # criar um mapa (dicionario) de listas
        for word in strs:
            sorted_word = ''.join(sorted(word)) # eat -> aet
            dict[sorted_word].append(word) # a palavra ordenada é a chave, o valor é a palavra em questão.
            # desse jeito, dá pra mapear todas as palavras "iguais" pra termos elas divididas
        
        return list(dict.values())
    
palavras = ["eat","tea","tan","ate","nat","bat"]

solution = Solution()
print(solution.groupAnagrams(palavras))
