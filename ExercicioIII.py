def calcularPotencia(base, expoente):
  # Qualquer número elevado a 0 é 1
  if expoente == 0:
    return 1
    
  # Dividindo e conquistando
  meio = calcularPotencia(base, expoente // 2)
    
  if expoente % 2 == 0: # Se o expoente é par
    return meio * meio
  
  else: # Se o expoente é ímpar
    return base * meio * meio

# Digitando a entrada
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = calcularPotencia(base, expoente)

# Saída
print(f"{base}^{expoente} = {resultado}")
