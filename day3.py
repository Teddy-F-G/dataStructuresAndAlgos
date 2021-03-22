def naiveFib (targetFib):
    p=1
    n=1
    for i in range(targetFib - 2):
        n=n+p
        p=n-p
    return n

#print (naiveFib(8))

def recursiveFib(targetFib):
    if targetFib<=1:
        return targetFib
    return recursiveFib(targetFib-1)+recursiveFib(targetFib-2)

#print recursiveFib(6)

def fizzbuzzNaive(n):
    for i in range(1, n+1):
        if (i%5==0 and i%3==0):
            print "fizzbuzz"
        elif i%5==0:
            print "buzz"
        elif i%3==0:
            print "fizz"
        else: print str(i)

#fizzbuzzNaive(15)