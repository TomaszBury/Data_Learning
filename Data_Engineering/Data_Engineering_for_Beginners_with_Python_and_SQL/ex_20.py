class MaxNumberFinder:
    def __init__(self, nums):
        self.nums = nums 
        
    def find_max_number(self): 
        return max(self.nums)
    
finder = MaxNumberFinder([1,3,4,2])
print(finder.find_max_number())