#!python3


def getIntegers(myList):
    integers = []

    x= [i for i in myList if type(i)==int]
    integers.extend(x)

    return integers

def getFactor(myList,number):
    abc = list(myList)
    abc.pop(abc.index(0))
    factors = [i for i in abc if number % i == 0]
    
    return factors

def getNegatives(myList):
    negatives = [i for i in myList if i < 0]

    return negatives

def getIntersection(list1,list2):
    common = [i for i in list1 if i in list2]
    common.sort()

    return common

def getUnion(list1,list2):
    union = list1 + list2
    union.sort()
    for i in union:
        if union.count(i) > 1:
            pos1 = union.index(i)
            union.pop(pos1)

    return union   

def getMerge(list1,list2):
    for i in list2:
        if i in list1:
            pos1 = list1.index(i)
            list1.insert(pos1,i)
        else:
            list1.append(i)

    return list1


def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    try:
        assert getIntegers([3,4,1.2,1.3,5]) == [3,4,5]
        assert getFactor(range(10),12) == [1,2,3,4,6]
        assert getNegatives([-3,-1,0,1,4]) == [-3,-1]
        assert getUnion(easy1,easy2) == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]
        assert getIntersection(easy1,easy2) == [2,4,6]
        assert getMerge(easy1,easy2) == [5,10,15,2,2,4,4,6,6,8,-2,-4,-6,0.1]
        print("All assertions passed")
    except:
        print("At least 1 assertion failed")

if __name__ == "__main__":
    main()
