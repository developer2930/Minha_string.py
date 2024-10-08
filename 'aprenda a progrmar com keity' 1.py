texto = 'aprenda a progrmar com keity'

def count_a():
    """Conta quantas vezes a letra 'a' aparece no texto."""
    return texto.count('a')

# Chama a função e armazena o resultado
resultado = count_a()

# Verifica se a letra 'a' foi encontrada e imprime a mensagem correspondente
if resultado > 0:
    print(f"A letra 'a' aparece {resultado} vezes.")
else:
    print("A letra 'a' não foi encontrada.")