import math

C = int(input())
A = int(input())

alunos = int(C-1/A)
viagens = A/alunos

print(math.ceil(viagens))
