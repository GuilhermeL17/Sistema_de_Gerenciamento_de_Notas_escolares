def busca_sequencial(lista, valor):
    for indice, elemento in enumerate(lista): #permite percorrer a lista tendo acesso ao índice
        if elemento == valor:
            return indice  # Retorna o índice onde encontrou
    return -1  # Retorna -1 se não encontrou

# Exemplo de uso:
notas = [7.5, 8.0, 6.0, 9.2, 5.0]
valor_procurado = 6.0

resultado = busca_sequencial(notas, valor_procurado)
if resultado != -1:
    print(f"Valor {valor_procurado} encontrado na posição {resultado}")
else:
    print("Valor não encontrado na lista.")