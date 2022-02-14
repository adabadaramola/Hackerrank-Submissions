def interquartile(val, freq):
    # Print your answer to 1 decimal place within this function
    S = []
    for r in range(n):
        for i in range(freq[r]):
            S.append(val[r])
    
    S.sort()
    print(S)
    l = len(S)
    if l%2==0:
        q2_1 = S[l//2]
        q2_2 = S[l//2 - 1]
    
        q2 = (q2_1+q2_2)/2
    else:
        q2 = S[l//2]

        
        
    #dividing the arr into two halves

    part_1 = []
    part_2 = []
    
    for i in S:
        if i<q2:
            part_1.append(i)
        if i>q2:
            part_2.append(i)
    
    #q1 calculation
    l = len(part_1)
    if l%2==0:
        q1_1 = part_1[l//2]
        q1_2 = part_1[l//2 - 1]
        
        q1 = (q1_1 + q1_2)/2
    else:
        q1 = part_1[l//2]
        
    #q3 calcualation
    l = len(part_2)
    if l%2==0:
        q3_1 = part_2[l//2]
        q3_2 = part_2[l//2 - 1]
        
        q3 = (q3_1 + q3_2)/2
    else:
        q3 = part_2[l//2]
    
    print(round(q3 - q1,1))
    

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interquartile(val, freq)
