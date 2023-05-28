N = int(input())

for _ in range(N):
    valor, t = input().split()
    valor = int(valor)
    k = 0 if t == '1T' else 45

    if valor > 45:
        acres = valor - 45
        print(f'{45+k}+{acres}')
    else:
        print(f'{valor+k}')

