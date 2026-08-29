class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)

        i = 0 
        j = 0 
        prev = 0 
        curr = 0
        for  _ in range((n1 + n2)//2 + 1):
            prev = curr 

            if i < n1 and j < n2: 
                if nums1[i] < nums2[j]:
                    curr = nums1[i]
                    i += 1 
                else: 
                    curr = nums2[j]
                    j += 1 
            elif i < n1:
                curr = nums1[i]
                i += 1 
            else:
                curr = nums2[j]
                j += 1

        if (n1 + n2) % 2 == 1 : 
            return curr 

        return (prev + curr)/2  


