from collections import deque

class Solution(object):
    def romanToInt(self, s):
        deq = deque(s)
        result = 0
        letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        substr_lettrs = ['I', 'X', 'C']
        minuend_lettrs = ['M', 'D', 'C', 'V', 'X', 'L']
        while deq:
            el = deq.popleft()
            next_el = self.getNext(deq)
            if el in substr_lettrs and next_el in minuend_lettrs and letters[next_el] > letters[el] and next_el != None:
                result += (letters[next_el] - letters[el])
                deq.remove(next_el)
            else:
                result += letters[el]
        return result

    def getNext(self, deq):
        if deq:
            return deq[0]
        else:
            return None

string = input("Enter a roman digits: ")
obj = Solution()
result = obj.romanToInt(string)
print(f"Result = {result}")