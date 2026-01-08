p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = p + (10-1)* r
for n in range(p, d+r, r):
    print('{}'.format(n), end=' ')
print('Acabou!!')