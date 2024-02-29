#11
def calculate(s):
    
    stack = []
    
    num, sign = 0, '+'
    
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])  
        if s[i] in "+-*/" or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
               
                top = stack.pop()
                if top < 0:
                    stack.append(-(-top // num))
                else:
                    stack.append(top // num)
            num = 0  
            sign = s[i]  
    
    return sum(stack)


test_inputs = ["3+2*2", " 3/2 ", " 3+5 / 2 ", "-1+5", "2+3+5"]
test_outputs = []

for test_input in test_inputs:
    test_outputs.append(calculate(test_input))

test_outputs
