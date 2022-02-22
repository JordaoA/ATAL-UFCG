piles = int(input())

for time in range(piles):
    n = int(input())
    sla = n//2
    p1 = [2**(quadr+1) for quadr in range(sla-1)]
    p1.append(2**n)
    p2 = [2**(quadr+1) for quadr in range(sla-1, n-1)]
    print(abs(sum(p1)-sum(p2)))
    
    

