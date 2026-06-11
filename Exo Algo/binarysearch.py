# Binary search :

def searchInsert(self, nums: List[int], target: int) -> int:
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left



# two pointers :

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             if not s[left].isalnum():
#                 left += 1
#             elif not s[right].isalnum():
#                 right -= 1
#             elif s[left].lower() != s[right].lower():
#                 return False
#             else:
#                 left += 1
#                 right -= 1
#         return True