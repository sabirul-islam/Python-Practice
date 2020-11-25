import re
pattern = r'colour'
# if re.match(pattern,'Colour is a red, I love red colour'): # checks from the first
#     print('Match')
if re.search(pattern,'red is a colour, I love red colour'): # find from anywhere
    print('Match')
else:
    print('Not Match')

print(re.findall(pattern,'red is a colour, I love red colour')) # return a list