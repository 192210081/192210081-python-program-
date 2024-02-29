def are_isomorphic(s, t):
    if len(s) != len(t):
        return False

    
    s_to_t = {}
    
    t_to_s = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        
        if char_s not in s_to_t and char_t not in t_to_s:
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        
        elif char_s not in s_to_t or char_t not in t_to_s:
            return False
        
        elif s_to_t[char_s] != char_t or t_to_s[char_t] != char_s:
            return False

    return True


s = input("Enter the first string: ")
t = input("Enter the second string: ")


if are_isomorphic(s, t):
    print(f"The strings '{s}' and '{t}' are isomorphic.")
else:
    print(f"The strings '{s}' and '{t}' are not isomorphic.")
