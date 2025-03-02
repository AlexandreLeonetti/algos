# merge two sorted arrays
#Input: 
nums1 = [1,2,3,7,7,7]
m = 3
nums2 = [2,5,6]
n = 3

#Output: nums1 = [1,2,2,3,5,6]

print(nums1)
print(nums2)

def merge(arr1, arr2):
    i=0
    j=0
    res=[]
    n1 = len(arr1)-1
    n2 = len(arr2)-1
    while i<(n1) and j<(n2):
            print(i,j)

            if arr1[i]<=arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                 res.append(arr2[j])
                 j+=1

    while i<n1:
         res.append(arr1[i])
         i+=1
    while j<n2:
         res.append(arr2[j])
         j+=1
    return res

print(merge(nums1, nums2))



def merge_with_pointers(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1  # Pointers for nums1, nums2, and merged array
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:  # If any elements remain in nums2
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
