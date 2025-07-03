import time
from tkinter import *
from tkinter import ttk

def m_count(data,drawData,timer):
    s=Tk()
    a=int(input("Enter Starting Range"))
    b=int(input("Enter Ending Range"))
    k = max(data)+1
    #output = [0] * len(data)
    count = [0] * k
    for i in range(0, len(data)):
        count[data[i]] += 1
    for i in range(1,k):
        count[i] += count[i-1]
        drawData(data, ['Green' if x == i+1 else 'Red' for x in range(len(data))])
        time.sleep(timer)
    if a == 0:
        print(count[b])
    else:
        print(count[b]-count[a-1])
    '''l1=[]
    for i in range(0,len(data)):
        if (data[i] >= a and data[i] <= b):
            l1.append(data[i])
    s.canvas.delete("all")
    drawData(data, ['Green' for x in range(len(l1))])  '''  
    #drawData(data, ['Green' if x>=a and x<=b else 'Red' for x in range(len(data))])
    
    time.sleep(timer)

'''data=[9,4,2,7,1,2,4,3,10,12,22,23]
a=int(input("Enter starting range:"))
b=int(input("Enter ending range:"))
m_count(data,a,b)'''