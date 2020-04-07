class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        return float(nums1[int(len(nums1) / 2)]) if len(nums1) % 2 == 1 else (nums1[int(len(nums1) / 2) - 1] + nums1[int(len(nums1) / 2)]) / 2