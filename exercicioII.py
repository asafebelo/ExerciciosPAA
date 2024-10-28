def somaArray(array, inicio, fim):
    if inicio == fim: # Se o array só tem um elemento, logo ele é o máximo
        return array[inicio]

    meio = int((inicio + fim) / 2)

    # Dividindo e conquistando aqui
    somaEsquerda = somaArray(array, inicio, meio)
    somaDireita = somaArray(array, meio + 1, fim)
    return somaEsquerda + somaDireita

tamanhoArray = int(input("Digite o tamanho do vetor: ")) # Guarde o tamanho do array
fim = int(tamanhoArray - 1)

# Usuário passando os dados do array
array = []
for i in range(tamanhoArray):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    array.append(elemento)

resultado = somaArray(array, 0, fim)

if tamanhoArray > 1:
    meio = int((tamanhoArray - 1) / 2)
    esquerda = somaArray(array, 0, meio)
    direita = somaArray(array, meio + 1, fim)
    print("Soma da esquerda:", esquerda)
    print("Soma da direita:", direita)

print("Soma total:", resultado)


