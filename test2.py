'''
def getIntersection(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in both lists
    # the intersection of the 2 number sets
    
    common = [i for i in list1 if i in list2]
    common.sort()
    print(common)
    return common
'''
'''
def getMerge(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # add the elements of list2 into list1
    # if the list2 element is in list1, add it at the position where it occurs in list1
    # if the list2 element is not in list1, add it to the end

    #iterate through list2, index the spot of each same one in list1 and insert it
    for i in list2:
        if i in list1:
            pos1 = list1.index(i)
            list1.insert(pos1,i)
            pos2 = list2.index(i)
            list2.pop(pos2)
        else:
            list1.append(i)

    print(list2)
    print(list1)
    return list1
'''

def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in either of the lists
    # duplicate values will be ignored
    
    union = list1 + list2
    union.sort()
    for i in union:
        if union.count(i) > 1:
            pos1 = union.index(i)
            union.pop(pos1)


    print(union)
    return union 




easy1 = [5,10,15,2,4,6,8]
easy2 = [-2,-4,-6,2,4,6,0.1]
if getUnion(easy1,easy2) == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]:
    print("yay")
else:
    print("nay")

numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
getUnion(numbers1,numbers2)