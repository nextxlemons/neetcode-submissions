class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers) - 1
        while i < n:
            curr_sum = numbers[i] + numbers[n]
            if curr_sum == target:
                return [i+1,n+1]
            elif curr_sum > target:
                n -= 1
            else:
                i += 1
            