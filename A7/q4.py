def hash(sum):
    return sum % (2 ** d) # O(1), only one modulo operation

def naive_hash_pattern_finding(pattern, text): # O(n * l) technically O(l + n * l)
    pattern_sum = 0

    for i in range(len(pattern)):
        pattern_sum += pattern[i] # O(l)

    pattern_hash = hash(pattern_sum) # Getting hash code of the pattern

    # entire loop below is O(n * l)

    for i in range(len(text)): # O(n) as there are n substrings 
        sum = 0
        for j in range(len(pattern)): # O(l)
            sum += text[j] 
        
        substring_hash = hash(sum) # O(1)

        if (pattern_hash == substring_hash):
            # check if match is legitimate or false match 

