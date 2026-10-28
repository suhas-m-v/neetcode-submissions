class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
                top+=1
            elif top >=0 and (stack[top]=='[' and i == ']' or stack[top]=='{' and i == '}' or stack[top]=='(' and i == ')'):
                stack.pop()
                top-=1
            else:
                stack.append(i)
                top+=1
        if len(stack)==0:
            return True
        return False