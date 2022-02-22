def mzr(string):
    letters = []
    indexs = []

    for letter in range(len(string)):
        if string[letter] not in letters:
            letters.append(string[letter])
            indexs.append(letter)

    return(letters,indexs)

n = int(input())

for i in range(n):
    s = input()
    t = input()

    s_ = [letter for letter in s]
    s_.sort()

    t_ = [letter for letter in t]
    t_copy = [letter for letter in t]    
    t_.sort()

    if t_ == t_copy:    
        if len(s_) >= 3:
            k = mzr(s_)
            if t in ''.join(k[0]):
                if len(k[1]) > 3:
                    s__ = s_[k[1][1]:k[1][3]]
                    s__.sort(reverse=True)
                    s_ = s_[:k[1][1]] + s__ + s_[k[1][3]:]
                else:
                    s__ = s_[k[1][1]:]
                    s__.sort(reverse=True)
                    s_ = s_[:k[1][1]] + s__
            print(''.join(s_))
        else: print(''.join(s_))
    else:
        s_ = ''.join([letters for letters in s_])
        print(''.join(s_))