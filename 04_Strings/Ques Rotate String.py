#Ques Rotate String.

s = "abcde"
goal = "deabc"

for i in range(len(s)):
    
    s= s[-1] + s[:len(s)-1]#here time comp is O(N).
    if s== goal:
        print(True)
        break
else:
    print(False)
    
#Total time comp is O(N**2).
    
s = "abcde"
goal = "deabc"

if len(s) == len(goal) and goal in (s+s):
    print(True)
else:
    print(False)