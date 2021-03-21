def naiveFib (targetFib):
    p=1
    n=1
    for i in range(targetFib - 2):
        n=n+p
        p=n-p
    return n

print (naiveFib(8))

def recursiveFib(targetFib):
    if targetFib<=1:
        return targetFib
    return recursiveFib(targetFib-1)+recursiveFib(targetFib-2)

print recursiveFib(0)