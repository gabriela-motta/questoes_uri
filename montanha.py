N = int(input())
alturas = input().split()

res = "N"

for i in range(len(alturas)-2):
  a = int(alturas[i])
  b = int(alturas[i+1])
  c = int(alturas[i+2])

  if(b < a and b< c):
    res = "S"

print(res)