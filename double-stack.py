import time
start_time = time.time()

index =[0,1,0,2,1,3,2,1,1,2]
identity = [i for i in range(len(index))] 
print("Size: ", len(identity))

s1=[]
s2=[]
def faster(index, identity):
    for i in range(len(index)):
        while (index[i]>len(s1)):
            s1.append(s2.pop())
        while (index[i]<len(s1)):
            s2.append(s1.pop())
        s1.append(identity[i])

    while(len(s2)!=0):
        s1.append(s2.pop()) 
    return s1



output = faster(index, identity)

#print(output)
#if (output ==[2,8,9,7,4,6,0,5,3,1]):
#    print("OK!")
#else:
#    print("wrong...")

print("--- %s seconds ---" % (time.time() - start_time))





""" def faster_old(index, identity):
    for i in range(len(index)):
        while (index[i]<len(s1)):
            s2.append(s1.pop())
        s1.append(identity[i])
        while(len(s2)!=0):
            s1.append(s2.pop()) 
    return s1 """