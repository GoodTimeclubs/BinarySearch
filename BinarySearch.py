import math

A = [1,2,6,13,15,8,23,35,40] #Array of Numbers to search
left = 0 #left index of search interval
right = 8 #right index of search interval
mid = 0 #automatic mid selection
searchkey = 40 #enter searched number




def BinarySearch(A, left, right, searchkey):
    if right < left:
        print("Wurde nicht gefunden!")
        return 0
    mid = math.floor((right + left)/2)
    if searchkey == A[mid]:
        print("Wurde gefunden! An folgender Stelle:")
        print(mid+1)
        return 1
    elif searchkey < A[mid]:
        return BinarySearch(A, left, mid - 1, searchkey)
    else:
        return BinarySearch(A, mid+1,right,searchkey)



if __name__ == '__main__':
    BinarySearch(A, left, right, searchkey)

