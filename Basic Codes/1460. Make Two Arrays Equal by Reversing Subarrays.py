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
