import time
def insertion_sort(b):
    for i in range(1, len(b)):
        k = b[i]
        j = i - 1
        while j >=0 and b[j] > k:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = k
    return b

def bucket(data,drawData,timer):
    array=[]
    slot_num = 10
    for i in range(slot_num):
        array.append([])
    for j in data:
        index = int(slot_num*j)
        array[index].append(j)
    for i in range(slot_num):
        array[i] = insertion_sort(array[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(array[i])):
            data[k] = array[i][j]
            drawData(data, ['Blue' if x == k else 'Red' for x in range(len(data))]) 
            time.sleep(timer)
            k += 1
    drawData(data, ['Purple' for x in range(len(data))])