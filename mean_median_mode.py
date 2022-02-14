N = int(input())

X = list(map(int,input().strip().split()))[:N]

l = len(X)
X.sort()

#mean
mean = sum(X)/l

#median
if l%2==0:
    median_1 = X[l//2]
    median_2 = X[l//2 - 1]
    
    median = (median_1+median_2)/2
else:
    median = X[l//2]

#mode
n_l = []
i = 0
while i<len(X):
    n_l.append(X.count(X[i]))
    i+=1
    
d1 = dict(zip(X,n_l))
d2={k for (k,v) in d1.items() if v == max(n_l) }



    
#result   
print(round(mean,1))
print(round(median,1))
print(min(list(d2)))
