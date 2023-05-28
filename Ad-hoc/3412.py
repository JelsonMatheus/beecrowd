
def calc(notas):
    if len(notas) <= 3:
        return sum(notas) / max(len(notas), 2)
    else:
        notas = sorted(notas)
        notas.pop(0)
        return sum(notas) / len(notas)



N = int(input())

for _ in range(N):
    nome = input()
    notas = list(map(float, input().split()))
    media = calc(notas)
    print(f'{nome}: {media:.1f}')
