t = int(input())

for i in range(t):
    text = input()
    left_stk = []
    right_stk = []
    result = []        
    for i, k in enumerate(text):
        if k  == '(':
            left_stk.append((i,k))
        else :
            right_stk.append((i,k))
    if len(left_stk) == len(right_stk):
        for i in range(len(text)//2):
            x = left_stk.pop(0)
            y = right_stk.pop(0)
            if x[0] < y[0] :
                hap = x[1] + y[1]
            else :
                hap = y[1] + x[1]
            result.append(hap)

        if len(result) == len(text) //2:
            if ')(' not in result:
                print('YES')
            else :
                print('NO')

    else : 
        print('NO')

