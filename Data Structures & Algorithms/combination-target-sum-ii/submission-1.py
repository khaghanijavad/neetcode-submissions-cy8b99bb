class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue 

                if total + nums[i] > target:
                    break

                cur.append(nums[i])
                dfs(i + 1, cur, total + nums[i])  
                cur.pop()

        dfs(0, [], 0)
        return res