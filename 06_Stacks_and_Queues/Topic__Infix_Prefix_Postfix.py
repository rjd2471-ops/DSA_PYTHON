#Topic is that what is prefix,infix,postfix,conversion.
"""
According to the priority 
**
*,/
+,-  this is the prority order for these.
If any comes other then these then its priority is less then these.
"""
"""
what is operator or operand------>>>>>>>> is like A-Z,a-z,0-9.
"""
"""
infix --->> means inside of the operator or operand.
like that--> (x+y)*(a-b) here +,* and - are infix.

postfix---(stack based).   pq+mn+ *--->>>>> this is called postfix beacuse it comes later.
prefix----(lisp,tree).   *  + pr+mn is called prefix because it comes first.
"""

#Here our question is that we have need to convert infix to postfix.
num=a+b*(c^d-e)

class Solution:
    
    def  precedence(self, ch):
        if ch=="+" or ch=="-":
            return 1
        if ch=="*" or ch=="/":
            return 2
        if ch=="^":
            return 3
        return 0
    
    def InfixToPoatfix(self,s):
        stack=[]
        result=[]
        
        for char in s:
            if ("a"<= char<="z") or ("A"<= char <="Z") or ("0"<= char<= "9"):
                result.append(char)
            #If character is "(" push to the stack.
                
            elif char=="(":
                stack.append(char)
                
                
            #If character is ")" pop until you get "(".
            elif char==")":
                while stack and stack[-1]!="(":
                    result.append(stack.pop())
                stack.pop()
                
                
            #If character is an operator
            else:
                while stack and self.precedence(stack[-1])>= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
                
                
        while stack:#Pop remaning element from the stack.
            result.append(stack.pop())
        return "".join(result)
    
    
    
    
#Here the time complaxity is O(N)+O(N) and space comp is O(N)+O(N).
#Question is that convert infix to prefix.
#The way for doing this is
#reverse the infix.
#infix to postfix.
#reverse the ans.
    
    
s=f+d-c*(b+a)
    def infixToprefix(self,s):
        s=s[::-1]
        #In this reverse case we have need to change "(" into ")". due to this reverse.
        s=s.replace(")",temp).replace("(",")").replace(temp,"(")#If i do without using any temp variable then it is not possible to swap.
        stack=[]
        result=[]
        
        for char in s:
            if ("a"<= char<="z") or ("A"<= char <="Z") or ("0"<= char<= "9"):
                result.append(char)
            #If character is "(" push to the stack.
                
            elif char=="(":
                stack.append(char)
            #If character is ")" pop until you get "(".
                
                
            elif char==")":
                while stack and stack[-1]!="(":
                    result.append(stack.pop())
                stack.pop()
                
                
            #If character is an operator
            else:
                while stack and self.precedence(stack[-1])> self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
                
                
        while stack:#Pop remaning element from the stack.
            result.append(stack.pop())
        return "".join(result[::-1])
    
    
    #Its time comp is also similar to the O(N) and space comp is also O(N).
    #Question is that convert a postfix into infix.
    
    
    def postToinf(self,s):
        stack=[]
        
        for char in s:
            if char.isalnum():
                stack.append(char)
                
            else:
                #pop two operand
                op2=stack.pop()
                op1=stack.pop()
                #combine operand with operator
                new=f"({op1}{char}{op2})"
                stack.append(new)
        #In last we have only one elemnt so we can write this like.
        return stack[-1]
    
    
    #Here also time comp is O(N)
    #Question is that convert prefix to infix.
    
    
    def prefixToInfix(self,s):
        stack=[]
        for char in s[::-1]:#Here its time comp is O(N)+O(N).
            #If char is an operand then append it to in the stack.
            if char.isalnum():
                stack.append(char)
                
            else:
                op1=stack.pop()
                op2=stack.pop()
                new=f"({op1}{char}{op2})"
                stack.append(new)
        #Here we only have one element so we can write this in simplest way.
        return stack[-1]
    
    
    #Question is that we have need to convert postfix into prefix.
    def postfixTOprefix(self,s):
        stack=[]
        
        for char in s:
            
            if char.isalnum():
                stack.append(char)
                
            else:
                op2=stack.pop()
                op1=stack.pop()
                new=f"({char}{op1}{op2})"
                stack.append(new)
        return stack[-1]
    
    
    
    #Question is that convert prefix to postfix.
    
    def prefixTopostfix(self,s):
        
        stack=[]
        
        for i in range(len(s)-1,-1,-1):
            char=s[i]
            if char.isalnum():
                stack.append(char)
                
                
            else:
                op1=stack.pop()
                op2=stack.pop()
                new=op1+op2+char
                stack.append(new)
        return stack[-1]
    
    
    

        