import re

#get email 
mail=input('Enter your Email :')

#regex for check str
re.search(r'.+\@.+\..{2,3}',mail) 

#condition for print
if re.search(r'.+\@.+\..{2,3}',mail) == None:
    print('Not an email')
else :
    print('Is True')