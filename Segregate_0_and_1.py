class Solution:
    def segregate0and1(self, arr):
        l = 0
        r = len(arr) - 1

        while l < r:

            if arr[l] == 0:
                l += 1

            elif arr[r] == 1:
                r -= 1

            else:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        return arr

object = Solution()
arr = [0, 1, 0, 1, 0, 1]
result = object.segregate0and1(arr)
print(result)  # Output: [0, 0, 0, 1, 1, 1]