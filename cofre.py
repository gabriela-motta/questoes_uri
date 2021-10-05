entrada = input().split()
N = int(entrada[0])
M = int(entrada[1])
barra = input().split()
posicoes = input().split()

freq = [0,0,0,0,0,0,0,0,0,0]

i = 0

while (i < M -1): 
  p = []
  if(int(posicoes[i]) > int(posicoes[i+1])):
    p = barra[int(posicoes[i+1])-1:int(posicoes[i])]
    p[:] = reversed(p)
  else:
    p = barra[int(posicoes[i])-1:int(posicoes[i+1])]
  print(p)
  for num in p:
    freq[int(num)] +=1
  i+=1

print(freq)
