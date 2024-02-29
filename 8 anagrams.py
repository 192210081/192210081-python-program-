

def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = [s]
        else:
            anagrams[key].append(s)
    return list(anagrams.values())


test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],  
    [""],
    ["a"],  
]


results = []
for tc in test_cases:
    result = groupAnagrams(tc)
    results.append(result)


for i, result in enumerate(results, start=1):
    print(f"Test Case {i}: Input: {test_cases[i-1]}")
    print(f"Output: {result}\n")
