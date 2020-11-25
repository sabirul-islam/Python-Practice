import re
# pattern = r'colo.r' # u can use more than 1 dot for using more character
# pattern = r'^colo..r$' # ^ this symbol means 'colo' must remain in first, $ this symbol means 'r' must remain in last  
# pattern = r'a*' # * sign means 0 or more number of a
# pattern = r'(ab)*' # (multiple character)*
# pattern = r'a+b' # minimum one time
# pattern = r'a*b' 
pattern = r'ice(-)cream' # minimum one time
pattern = r'ice(-)?cream' # minimum one time
pattern = r'a{1,3}$' # minimum one a or maximum 3 a
# if re.match(pattern, 'abcolo5kr'): # should remain ab together
# if re.match(pattern, 'icecream'): # should remain ab together
if re.match(pattern, 'aaaa'): # should remain ab together
    print('Matched')
else:
    print('Not Matched')