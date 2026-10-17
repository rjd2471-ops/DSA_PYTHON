#Topic deque means Double ended queue.
#This is very helpful if we want to add or remove from both side one side is tail side and other side is
#called head side.
from collections import deque
lst=deque([])
lst.append(10)
lst.append(20)
lst.appendleft(30)#For append an element in front of the deque with an O(1) operation.
lst.appendleft(100)
lst.pop()
lst.popleft()#For removing element from the front side it is also an O(1) operation.
print(lst)