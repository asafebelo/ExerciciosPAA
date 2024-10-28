def maximoArray(array, inicio, fim):
  if inicio == fim: # Se o array só tem um elemento, logo ele é o máximo
    return array[inicio]
    
  meio = int((inicio + fim) / 2)
  # Dividindo e conquistando aqui
  maximoEsquerda = maximoArray(array, inicio, meio) # Encontrar o máximo da esquerda
  maximoDireita = maximoArray(array, meio + 1, fim) # Encontrar o máximo da direita
  maximoGlobal = max(maximoEsquerda, maximoDireita) # Retornar o maior valor entre as duas metades
  return maximoGlobal # Retornar o maior valor entre as duas metades


tamanhoArray = int(input("Digite o tamanho do vetor: ")) # Guarde o tamanho do array
fim = int(tamanhoArray - 1)

# Usuário passando os dados do array
array = []
for i in range(tamanhoArray):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    array.append(elemento)

resultado = maximoArray(array, 0, fim)

if tamanhoArray > 1:
  meio = int((tamanhoArray - 1) / 2)
  esquerda = maximoArray(array, 0, meio)
  direita = maximoArray(array, meio + 1, fim)
  print("Máximo da esquerda:", esquerda)
  print("Máximo da direita:", direita)

print("Máximo global:", resultado)
