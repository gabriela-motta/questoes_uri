# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
entrada = input().split()

tabela = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}
preco = tabela.get(int(entrada[0]))
total = preco * int(entrada[1])

print("Total: R$ {:.2f}".format(total))