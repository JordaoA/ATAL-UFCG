def soma(n):
    k = 0
    for i in n:
        k += int(i)
    return(k)

results = []
input_ = input()
r = max(0, int(input_)-81)

for i in range(r,int(input_)):
    if i + soma(str(i)) == int(input_):
        results.append(i)

print(len(results))
for i in results:
    print(i)
