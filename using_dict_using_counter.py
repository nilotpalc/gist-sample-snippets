# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    x = 0
    y = 0

    for item in s:
        if item.isupper() == True:
            x +=1
        elif item.islower() == True:
            y +=1
        else:
            pass
            
    print (f'Original String : {s}')
    print (f'No. of Upper case characters: {x}')
    print (f'No. of Lpper case characters: {y}')