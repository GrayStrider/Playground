"""

It's pretty easy in Python, all methods are already implemented....
pop, append/+=, insert, not to mention the whole Queue built-in class.


Still spent shitton of time, forgot to put "return" into functions. I dislike sample code in general, it's
too wordy, which makes it hard to read.
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, s):
        self.stack += s

    def enqueueCharacter(self, s):
        self.queue.insert(0, s)

    def popCharacter(self):
        return self.stack.pop()  # forgot to put "return"...

    def dequeueCharacter(self):
        return self.queue.pop(-1)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
print(obj.stack)
print(obj.queue)
isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    print(obj.stack[i], obj.queue[i])
    # print(obj.popCharacter())
    # print(obj.dequeueCharacter())
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
