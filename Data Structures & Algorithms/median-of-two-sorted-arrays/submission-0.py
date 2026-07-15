class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 , nums2 
        
        if len(A) > len(B):
            A , B = nums2 , nums1 
        
        total = len(A) + len(B) 
        half = total // 2
        r = len(A) - 1
        l = 0 

        while True:
            i = (l + r) // 2 # left partition 
            j =  half - i - 2 # right partition

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i +1] if i+1 < len(A) else  float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j+1] if j+1 < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total%2:
                    return min(A_right,B_right)
                
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif  A_left > B_right: 
                r = i - 1 
            else:
                l = i + 1

        return 0.0