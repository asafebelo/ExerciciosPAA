def somarSubconjunto(array, alvo, soma, indice, subconjuntoAtual):
  # Se a soma for igual ao alvo, imprime o subconjunto
  if soma == alvo:
    print(subconjuntoAtual)
    return
    
  # Se a soma for maior que alvo, ou o conjunto tiver acabado, volte
  if (soma > alvo) or (indice == len(array)):
    return
    
  somarSubconjunto(array, alvo, soma + array[indice], indice + 1, subconjuntoAtual + [array[indice]]) # Nova combinação

  somarSubconjunto(array, alvo, soma, indice + 1, subconjuntoAtual) # Combinação atual

# Entrada do usuário
array = list(map(int, input("Digite os elementos do array separados por espaço: ").split()))
alvo = int(input("Digite o valor do alvo: "))
print("Subsconjuntos que são iguais ao alvo: ")
somarSubconjunto(array, alvo, 0, 0, [])