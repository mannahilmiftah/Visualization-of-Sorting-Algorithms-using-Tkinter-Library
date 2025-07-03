import time

def modified_count(data,drawData,timer):
    a=int(input("Enter Starting Range"))
    b=int(input("Enter Ending Range"))
    k = max(data)+1
    #output = [0] * len(data)
    count = [0] * k
    for i in range(0, len(data)):
        count[data[i]] += 1
    for i in range(1,k):
        count[i] += count[i-1]
    if a == 0:
        print(count[b])
    else:
        print(count[b]-count[a-1])
    '''for i in range(0,len(data)):
        drawData(data, ['Green' if x == data[i] else 'Red' for x in range(len(data))])
        time.sleep(timer)'''

'''data=[9,4,2,7,1,2,4,3,10,12,22,23]
a=int(input("Enter starting range:"))
b=int(input("Enter ending range:"))
modified_count(data)
'''