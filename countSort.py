import time

def count_sort(data, drawData, timer):
    #k = max(data)+1
    output = [0] * len(data)
    count = [0] * 10
    for i in range(0, len(data)):
        count[data[i]] += 1
    for i in range(1,10):
        count[i] += count[i-1]
        drawData(data, ['Green' if x == i+1 else 'Red' for x in range(len(data))])
        time.sleep(timer)
    i = len(data)-1
    while i >= 0:
        output[count[data[i]]-1] = data[i]
        count[data[i]] -= 1
        i -= 1
        drawData(data, ['Blue' if x == i+1 else 'Red' for x in range(len(data))])
        time.sleep(timer)
    i = 0
    for i in range(len(data)):
        data[i] = output[i]
    drawData(data, ['Purple' for x in range(len(data))])