n, m, k = map(int, input().split())
houses = list(map(int, input().split()))
menor = 1000 # 1000 pode ser inf pois ultrapassa o tamanho maximo que a lista pode chegar

for i in range(m-1,-1,-1): # de trás pra frente
    if (houses[i] != 0) and (k >= houses[i]):
        suposto_menor = abs((i+1)-m)*10
        if(suposto_menor < menor):
            menor = suposto_menor

for i in range(m,n): # de frente pra trás
    if (houses[i] != 0) and (k >= houses[i]):
        suposto_menor = abs((i+1)-m)*10
        if(suposto_menor < menor):
            menor = suposto_menor

print(menor)
