class Element(object):
    def __init__(self, ch, count):
        self.ch = ch
        self.count = count


class Solution(object):
    def frequencySort(self, s):
        freq = {}
        for i, ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 0
            freq[ch] = freq[ch]+1
        bucket = ['']*(len(s)+1)
        for i, key in enumerate(freq):
            val = freq[key]
            if val > 0:
                bucket[val] = bucket[val] + key*val
        result = ''
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i] != '':
                result = result + bucket[i]
        return result

    def frequencySort1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        table = [0]*128
        for i in range(0, len(s)):
            index = ord(s[i])
            table[index] = table[index] + 1

        elements = []
        for i in range(0, 128):
            letter_count = table[i]
            if letter_count > 0:
                ch = chr(i)
                element = Element(ch, letter_count)
                elements.append(element)

        self.quicksort(elements, 0, len(elements)-1)
        result = ''
        for i in range(len(elements)-1, -1, -1):
            result = result + elements[i].ch*elements[i].count
        return result

    def partion(self, elements, start, end):
        # print 'partion ', [ele.count for ele in elements], start, end
        pivot = elements[start]
        while start < end:
            while start < end and elements[end].count >= pivot.count:
                end = end - 1
            elements[start] = elements[end]
            while start < end and elements[start].count < pivot.count:
                start = start + 1
            elements[end] = elements[start]
            elements[start] = pivot
        return start

    def quicksort(self, elements, start, end):
        # print 'quicksort ', [ele.count for ele in elements], start, end
        mid = self.partion(elements, start, end)
        # print 'mid = ', mid
        if mid > start:
            self.quicksort(elements, start, mid-1)
        if mid+1 < end:
            self.quicksort(elements, mid+1, end)

if __name__ == '__main__':
    print Solution().frequencySort('')
    print Solution().frequencySort('tree')
    print Solution().frequencySort('eeee')
