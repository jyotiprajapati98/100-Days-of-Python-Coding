class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        N = len(target)
        
        if len(target) != len(arr):
            return False
        
        target.sort()
        arr.sort()
        
        for i in range(0, N):
            if target[i] != arr[i]:
                return False
        return True

    list1 = [1,2,3,4]
    list2 = [4,2,3,5]
    print(canBeEqual(list1, list1))

