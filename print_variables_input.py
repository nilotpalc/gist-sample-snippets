# Using Variable names in Input function

name = 'Sally'
input('Hi {} Please enter your name: '.format(name))

# This would print out the below line
Hi Sally Please enter your name: (and the input field box)
  
## This concept is different from the print f-string function and the format function can be used 
## in defining functions with input statement

name = 'Sally'
input(f'Hi {name} Please enter your name: ') # using f-string print function in input statement for variable printing

# this would print out the same output
Hi Sally Please enter your name: (and the input field box)
