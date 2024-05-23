import random
alunos=['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']
print(f"Lista: {alunos}")
# Embaralhar a lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Ordena a Lista Crescente
alunos.sort()
print(f"Lista crescente: {alunos}")
# Ordena a lista Decrescente
alunos.sort(reverse=True)
print(f"Lista decrescente: {alunos}")