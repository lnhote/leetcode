class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        print nums1, nums2
        result = 0.0;
        pos_start_1 = 0
        pos_end_1 = len1-1
        pos1 = (pos_start_1 + pos_end_1)/2
        pos2 = (len1 + len2)/2-2-pos1
        while True:
            # print 'nums1[%s] = %s' % (pos1, nums1[pos1]), nums1[0:pos1+1], nums1[pos1+1:]
            # print 'nums2[%s] = %s' % (pos2, nums2[pos2]), nums2[0:pos2+1], nums2[pos2+1:]
            if pos1 >= 0 and nums1[pos1] > nums2[pos2+1]:
                # pos1 move back, pos2 move forward
                pos_end_1 = pos1
                pos1 = (pos_start_1 + pos1)/2
                if pos1 == 0 and pos_start_1 == 0:
                    pos1 = -1
                diff = pos_end_1 - pos1
                pos2 = pos2 + diff
            elif pos1 < len1-1 and nums2[pos2] > nums1[pos1+1]:
                # pos1 move forward, pos2 move back
                pos_start_1 = pos1
                pos1 = (pos1 + pos_end_1)/2
                if pos1 == pos_start_1:
                    pos1 = pos1 + 1
                diff = pos1 - pos_start_1
                pos2 = pos2 - diff
            else:
                max_left = 0
                if pos1 < 0:
                    max_left = nums2[pos2]
                elif pos2 < 0:
                    max_left = nums1[pos1]
                else:
                    max_left = max(nums1[pos1],nums2[pos2])
                if pos1 == len1-1:
                    min_right = nums2[pos2+1]
                elif pos2 == len2-1:
                    min_right = nums1[pos1+1]
                else:
                    min_right = min(nums1[pos1+1],nums2[pos2+1])
                if (len1+len2)%2 == 1:
                    return min_right
                if max_left <= min_right:
                    result = (max_left+min_right)/2.0
                    # print 'max_left = %s, min_right = %s' % (max_left, min_right)
                    break
        return result

if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1],[2,4]) # 2.0
    print Solution().findMedianSortedArrays([1,3],[2]) # 2.0
    print Solution().findMedianSortedArrays([1,3],[2,4]) # 2.5
    print Solution().findMedianSortedArrays([1,2,3],[4,5,6]) # 3.5
    print Solution().findMedianSortedArrays([4,5,6],[1,2,3]) # 3.5
    print Solution().findMedianSortedArrays([1,2,5,19],[3,4,6,7,8,9,10,11]) #6.5
    print Solution().findMedianSortedArrays([1,2,3],[4,6,7,8,9,10,11]) #6.5
