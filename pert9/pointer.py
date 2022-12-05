def objectArray(array):
    start, end = 0, len(array)-1
    while start< end:
        array[start], array[end] = array[end] , array[start]
        start += 1
        end -= 1

array = [12,15,17,19,21]
objectArray(array)
print(array)