ig, jg = list(input())
jg = int(jg)
jg = 9 - jg
ig = (ord(ig) - 97) + 1


for i in range(8):
    for j in range(8):
        if (i == (jg-1)) and (j == (ig)-1):
            print('Q', end = " ")
            
        elif abs(i - (jg-1)) == abs(j - (ig-1)):
            print('X', end = " ")
            
        elif j == ig-1 or i == jg-1:
            print('X', end = " ")
            
        else:
            print('.', end = " ")
            
        if j == 7:
            print()
