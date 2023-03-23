#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
#For example, histogram([4, 9, 7]) should print the following:

def histogram(num):
    l = []
    
    for i in num:
        
        for j in range(i):
            l.append("*")
        
        print("".join(l))
        
        l.clear()


histogram([4, 9, 7])