class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        
        for k in range(len(nums) - 2):

            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            target = -nums[k]
            i = k + 1
            j = len(nums) - 1
            
            while i < j:
                sums = nums[i] + nums[j]
                if sums == target:
                    result.append([nums[k], nums[i], nums[j]])

                    while i < len(nums)-1 and nums[i] == nums[i + 1]:
                        i += 1

                    while j >= 0 and nums[j] == nums[j - 1]:
                        j -= 1
                    
                    i += 1
                    j -= 1
                elif sums < target:
                    i += 1
                else:
                    j -= 1
        
        return result
    
object = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = object.threeSum(nums)
print(result)  # Output: [[-1, -1, 2], [-1 , 0, 1]]