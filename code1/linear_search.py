number_list=[1,2,3,4,5,6,7,8,9,10]

def search(list,target):
    for index in range(len(number_list)):
        if list[index] == target:
            return index
        
    return -1

print(search(number_list,10))