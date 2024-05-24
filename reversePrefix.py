class Solution:
  def reversePrefix(self, word: str, ch: str) -> str:
    if ch not in word: return word
    index = word.find(ch) # devolve a primeira ocorrencia, ok
    aux = word[:index+1]
    aux = aux[::-1] #inverter
    word = aux + word[index+1:]
    return word
