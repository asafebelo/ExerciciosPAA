def backtracking(array, combinacaoAtual, indice):
  # Se chegar no final do arrau, retorna ele todo
  if indice == len(array):
    if combinacaoAtual:
      print("".join(combinacaoAtual))
    return
    
  backtracking(array, combinacaoAtual, indice + 1) # Combinação atual
    
  backtracking(array, combinacaoAtual + [array[indice]], indice + 1) # Nova combinação

# Entrada do usuário
array = input("Digite os elementos do array separados por espaço: ").split()
print("As combinações possíveis são:")
backtracking(array, [], 0)

