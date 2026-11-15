class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist=[]
        n=len(nums)
        for i in range(n):
            if nums[i] not in newlist:
                newlist.append(nums[i])
            else:
                return True
        return False