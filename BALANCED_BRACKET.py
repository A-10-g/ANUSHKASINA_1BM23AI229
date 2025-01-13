
def isBalanced(s):
    
    stack = []
    
   
    matching_bracket = {')': '(', '}': '{', ']': '['}
    

    for char in s:
        if char in matching_bracket.values():
           
            stack.append(char)
        elif char in matching_bracket.keys():
           
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return "NO"  
   
    return "YES" if not stack else "NO"

def check_balanced_brackets(n, strings):
    results = []
    for s in strings:
        results.append(isBalanced(s))
    return results

n = int(input())  
strings = [input().strip() for _ in range(n)]  
results = check_balanced_brackets(n, strings)
for result in results:
    print(result)
