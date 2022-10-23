N, L, D = map(int, input().split())

total = N * D
qtd = total // (L * 1000)
res = total % (L * 1000)

if res > 0:
    qtd += 1

print(int(qtd * L))