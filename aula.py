#Exercícios de fixação
# Solicita ao usuário uma letra específica
letra_pedida = input("Digite uma letra para ver sua posição na lista: ")

# Cria uma lista para armazenar as letras
lista_letras = list(letra_pedida)

# Pede ao usuário para escolher uma posição (índice)
indice = int(input(f"Escolha um número de 0 a {len(lista_letras)-1} para ver a letra correspondente: "))

# Verifica se o índice está dentro do intervalo válido e exibe a letra correspondente
if 0 <= indice < len(lista_letras):
    print(f"A letra na posição {indice} é: {lista_letras[indice]}")
else:
    print("Índice inválido!")