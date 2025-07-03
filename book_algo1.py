import time

def insertion_sort(data,drawData,timer,start,end):
    for i in range(start+1,end+1):
        k = data[i]
        j = i
        while j > start and data[j-1] > k:
            data[j] = data[j-1]
            j -= 1
            drawData(data, ['Yellow' if x == j else "Green" if x == i else 'Red' for x in range(len(data))])
            time.sleep(timer)
        data[j] = k
    drawData(data, ['Purple' for x in range(len(data))])

def partition(data,drawData,timer,start,end):
    pivot = data[end]
    i = j = start
    for i in range(start,end):
        if data[i] < pivot:
            data[i], data[j] = data[j], data[i]
            j += 1
            drawData(data, ['Blue' if x == j else 'Red' for x in range(len(data))])
            time.sleep(timer)
    data[j], data[end] = data[end], data[j]
    return j

def modified_quick(data,drawData,timer,start,end):
    while start < end:
        if end-start < 10:
            insertion_sort(data,drawData,timer,start,end)
            break
        else:
            pivot = partition(data,drawData,timer,start,end)
            if pivot-start < end-pivot:
                modified_quick(data,drawData,timer,start,pivot-1)
                start = pivot+1
            else:
                modified_quick(data,drawData,timer,pivot+1,end)
                end = pivot-1