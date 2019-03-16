def hash(sum):
    return sum % (2 ** d) # O(1), only one modulo operation

def optimized_hash_pattern_finding(pattern, text): # O(l + n) (technically O(l + l + n))
    pattern_sum = 0

    for i in range(len(pattern)):
        pattern_sum += pattern[i] # O(l)

    pattern_hash = hash(pattern_sum) # Getting hash code of the pattern

    sum = 0
    for i in range(len(pattern)): # O(l)
        sum += text[i]
    
    for i in range(len(text)): # O(n) as there are about n substrings 
        substring_hash = hash(sum)

        if (pattern_hash == substring_hash):
            # check if match is legitimate or false match 
            
        # optimizing steps
        sum -= text[i]
        sum += text[i + len(pattern)]


    
