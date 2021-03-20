l1 = [1,2,4,6,8,9]
l2 = [1,3,4]
l3 = l1+l2
l4 = l1.append(l2)

l3.sort()
#print l4 #.sort()

#print l3

#find the indexes of numbers within a list such that the values of the 3 numbers adds up to target. target = 7 for this
l1 = [1,2,4,6,8,9]

target = 7
complementHashMap = {}
index = 0
for i in l1:
    print "i is: " + str(i)
    if i>len(l1):
        print "not today, mate"
        break
    complement = target - i
    if complement in complementHashMap:
        print "successful index is: " + str(index)
        print "and other number is at index: " + str(complementHashMap.get(complement))
        break
    else:
        complementHashMap[i]=index
        print "index is: " + str(index)
        print "complement is: " + str(complement)
        #print ""
        print "hashmap is: " + str(complementHashMap)
        index +=1