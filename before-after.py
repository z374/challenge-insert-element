import time
import numpy as np

start_time = time.time()

index =[0,1,0,2,1,3,2,1,1,2]
identity = [i for i in range(len(index))] 

size = len(index)
print("Size: ", size)
half_size = int(size/2)
identity = np.array(identity[::-1])
index = np.array(index[::-1]).astype(int)
new_order = [0]*size
target = 0

for e in range(size):    
    current = 0
    while(index[current]!=target):
        current+=1
    new_order[e]=identity[current]

    index = np.concatenate([index[0:current], index[current+1:]])
    identity = np.concatenate([identity[0:current],identity[current+1:]])

    if (current>half_size) and (current!=(size-e-1)):
        index[current:]+=1
        target+=1
    elif (current!=0):
        index[:current]-=1

#print(new_order)
#if (new_order ==[2,8,9,7,4,6,0,5,3,1]):
#    print("OK!")
#else:
#    print("wrong...")

print("--- %s seconds ---" % (time.time() - start_time))










