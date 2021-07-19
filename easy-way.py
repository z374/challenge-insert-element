import time

start_time = time.time()
index =[0,1,0,2,1,3,2,1,1,2]

identity = [i for i in range(len(index))] 
size=len(index)

print("Size: ", size)
    
output = []
for i,id in list(enumerate(identity)):
    output.insert(index[i],id)

#print(output)
#if (output ==[2,8,9,7,4,6,0,5,3,1]):
#    print("OK!")
#else:
#    print("wrong...")

print("--- %s seconds ---" % (time.time() - start_time))