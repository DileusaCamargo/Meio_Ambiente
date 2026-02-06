


numeros = []  # lista vazia para armazenar os valores

# Entrada dos números
for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

# Processamentos
maior = max(numeros)        # maior número
menor = min(numeros)        # menor número
soma = sum(numeros)         # soma de todos os números

# Saída
print("\n--- Resultados ---")
print("Números digitados:", numeros)
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma de todos os números:", soma)
