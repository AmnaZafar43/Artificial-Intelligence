## TASK 1
import collections
dict = collections.defaultdict(int)
def fibonacci(num):
        if num in dict:
            return dict[num]
        if num<=1 :
            dict[num]=num 
            return num 
        else:
            a = fibonacci(num-1)+fibonacci(num-2) 
            dict[num] = a 
            return a 
        
print("Enter a number: ") 
number = int(input()) 
for i in range(number):
    print(fibonacci(i))

## TASK 2
LCS = [[]]
def longestSubsequence(s1, s2):
    if s1 == '' or s2 == '':
        return LCS
    else:
        for i in s1:
            for j in s2:
                if i == j:
                    LCS[i][j] = 1 + LCS[i-1][j-1]
                    return LCS
                else:
                    LCS[i][j] = 0
    for x in LCS:
        return max(x)
print('Enter first string: ')
string1 = input()
print('Enter sceong string: ')
string2 = input()
r = longestSubsequence(string1,string2)
print(r)

## TASK 3
newArr = []
def cutting(arr, size):
    if(len(newArr) >= 0):
        return newArr
    maxi = -10000
    for i in range(0, size):
        maxi = max(maxi, arr[i] + cutting(arr,size-i))
        newArr[size] = maxi
        return newArr[size]

arr = [0, 10, 24, 30, 40, 45]
arrSize = len(arr)
print(cutting(arr,arrSize))
