source=[40,30,2,54,123,21,23]

def leftshift(source,k):
    n=len(source)
    for i in range(n-k):
        source[i]=source[i+k]
    for j in range(n-k,n):
        source[j]=0
    return source
leftshift(source,3)
print(source)
