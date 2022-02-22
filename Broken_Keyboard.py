k = int(input())

for i in range(k):
    s = input() # String de entrada
    res = []

    letters = {'a':0,'b':0,'c':0,'d':0,'e':0,
                'f':0,'g':0,'h':0,'i':0,'j':0,
                'k':0,'l':0,'m':0,'n':0,'o':0,
                'p':0,'q':0,'r':0,'s':0,'t':0,
                'u':0,'v':0,'w':0,'x':0,'y':0,
                'z':0}
    
    letter_index = 0
    string = 0
    while string < len(s):
        if (s[string] == s[letter_index]):
            letters[s[letter_index]] += 1
            string+=1
        else:
            if (letters[s[letter_index]] % 2 == 1) and (s[letter_index] not in res):
                res.append(s[letter_index])
            letters[s[letter_index]] = 0
            letter_index = string

    if (letters[s[-1]] % 2 == 1) and (s[-1] not in res):
        res.append(s[letter_index])

    res.sort()
    res = ''.join([letter for letter in res])

    print(res)