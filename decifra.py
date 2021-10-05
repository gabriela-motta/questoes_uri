permuta = input()
frase = input()
alfa = "abcdefghijklmnopqrstuvwxyz"

alfa = [alfa[i:i+1] for i in range(0, len(alfa), 1)]
permuta = [permuta[i:i+1] for i in range(0, len(permuta), 1)]

res = ""

for ch in frase:
  res+=alfa[permuta.index(ch)]
print(res)