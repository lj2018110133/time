from functools import wraps
import time


# class dev:
#     def __init__(self,*args,**kwargs):


def comTime(func1):
    @wraps(func1)
    def jisuanFuncTime():
        start = time.time()
        func1()
        print(time.time() - start)

    return jisuanFuncTime


def con3(func):
    start = time.time()
    func()
    return time.time() - start


def func2():
    return "hello world"


@comTime
def fun3():
    print("123344")


# func2()
# fun3()

# print(con3(func2))

index1 = [1, 2, 3, 4]
index1[3] = 5
print(index1)


def minNumberInRotateArray(rotateArray):
    if len(rotateArray) == 0:
        return 0
    minindex = 0
    for i in range(1, len(rotateArray)):
        if rotateArray[minindex] > rotateArray[i]:
            minindex = i
    return rotateArray[minindex]


index = [3, 4, 5, 0, 2]
print(minNumberInRotateArray(index))


def com(rote):
    return min(rote)


print(com(index))


def minNumberInRotateArray1(rotateArray, target):
    # write code here
    length = len(rotateArray)
    if length == 0:
        return 0
    elif length == 1:
        return rotateArray[0]
    else:
        left = 0
        right = length - 1
        while left < right:
            mid = int((left + right) / 2)
            if rotateArray[mid] == target:
                return mid
            elif rotateArray[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
    return left


print(minNumberInRotateArray1(index, 5))
print(int((1 + 2) / 2))


def jiaohuan(index, i, j):
    temp = index[i]
    index[i] = index[j]
    index[j] = temp

jiaohuan(index,0,1)
print(index)