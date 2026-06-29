class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        memory = {}
        res = []
        for i in range(len(nums)):
            if i == 0:
                memory[f"{i}_left"] = 1
            else:
                memory[f"{i}_left"] = memory[f"{i-1}_left"] * nums[i-1]

        for i in  range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                memory[f"{i}_right"] = 1
            else:
                memory[f"{i}_right"] = memory[f"{i+1}_right"] * nums[i+1]
        for i in range(len(nums)):
            if i == 0:
                res.append(memory[f"{i}_right"])
            elif i == len(nums)-1:
                res.append(memory[f"{i}_left"])
            else:
                res.append(memory[f"{i}_left"]*memory[f"{i}_right"])
        return res
          