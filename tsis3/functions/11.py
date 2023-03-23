#Write a Python function that checks whether a word or phrase is palindrome or not. 
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

s = str(input())

def pallindrome(s):
    
    ok = True
    
    for i in range(len(s)):
        
        if(s[i] != s[-1 - i]):
            ok = False
            break
    
    return ok

print(pallindrome(s))