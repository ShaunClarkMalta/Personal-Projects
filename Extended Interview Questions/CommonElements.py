### Find the common elements in an undetermined number of sorted lists

'''Input *args
Create list[pointers] at 0 (len = len(*args))
Check limits of pointers:
    if min == max; then append
    else; min pointer +1'''

def common_element(*args):
    pointers = [0] * len(args)
    results = []

    #Ensuring that all pointers are in range whilst loop is running
    while all(pointers[i] < len(args[i]) for i in range(len(args))):
        #Check the minimum and maximum values in the lists provided
        min_value = float('inf')
        min_counter = -1
        max_value = 0
        for i in range(len(args)):
            #checks for the min and max values in the current selection
            if args[i][pointers[i]] < min_value:
                min_value = args[i][pointers[i]]
                min_counter = i
            if args[i][pointers[i]] > max_value:
                max_value = args[i][pointers[i]]
        #if Min == max; then all elements are the same and can be appended
        if min_value == max_value:
            results.append(min_value)
            #Must increment all pointers by 1
            pointers = [x + 1 for x in pointers]
        else:
            pointers[min_counter] += 1

    if len(results) > 0:
        return results
    else:
        return -1
    

array1 = [1, 2, 3, 4]
array2 = [2, 3, 4, 5]
array3 = [0, 2, 3, 6]
print(f"The common elements are: {common_element(array1, array2, array3)}")

array1 = [1, 3, 5]
array2 = [2, 4, 6]
array3 = [0, 7, 8]
print(f"The common elements are: {common_element(array1, array2, array3)}")

array1 = [1, 2, 3, 9]
array2 = [0, 3, 4]
array3 = [3, 5, 6]
print(f"The common elements are: {common_element(array1, array2, array3)}")

array1 = [1, 2, 3]
array2 = []
array3 = [2, 3]
print(f"The common elements are: {common_element(array1, array2, array3)}")

array1 = [1, 2, 2, 3]
array2 = [2, 2, 3, 4]
array3 = [2, 3, 3]
print(f"The common elements are: {common_element(array1, array2, array3)}")

array1 = [1, 2, 3, 4, 5, 14]
array2 = [3, 4, 5, 6, 14]
array3 = [0, 3, 7, 14]
array4 = [3, 8, 9, 10, 11, 12, 14]
array5 = [2, 3, 13, 14]
array6 = [3, 14]
array7 = [3, 14, 15, 16]
print(f"The common elements are: {common_element(array1, array2, array3, array4, array5, array6, array7)}")