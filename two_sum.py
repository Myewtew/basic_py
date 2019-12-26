def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    minus_dict = dict()
    for i in range(len(nums)):
        if nums[i] in minus_dict:
            return [minus_dict[nums[i]], i]
        else:
            minus_dict[target-nums[i]] = i
