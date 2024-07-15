#platform - coding ninjas
#link - https://www.naukri.com/code360/problems/ninja-and-the-sorted-check_6581957
#concept - check it is sorted or not
#expected time complexity - O(n)

def isSorted(n: int,  a: [int]) -> int:
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            return 0;
    return 1;

