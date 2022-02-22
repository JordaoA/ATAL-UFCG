strength, dragons = map(int, input().split())

dragons_info = []

its_alive = True

for dragon in range(dragons):
    dragon_strength, bonus = map(int, input().split())
    dragons_info.append((dragon_strength, bonus))

dragons_info.sort(reverse = True)

for dragon in range(len(dragons_info)-1,-1,-1):
    if dragons_info[dragon][0] < strength:
        strength += dragons_info[dragon][1]
        dragons_info.pop()
    else:
        its_alive = False
        break

if its_alive: print('YES')
else: print('NO')