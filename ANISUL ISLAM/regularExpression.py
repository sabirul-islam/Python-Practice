# import re
# pattern = r'colour'
# # if re.match(pattern,'Colour is a red, I love red colour'): # checks from the first
# #     print('Match')
# if re.search(pattern,'red is a colour, I love red colour'): # find from anywhere
#     print('Match')
# else:
#     print('Not Match')

# print(re.findall(pattern,'red is a colour, I love red colour')) # return a list

# import re
# pattern = r'colour'
# text = 'My favourite colour is red'
# match = re.search(pattern,text)
# if match:
#     print(match.start())
#     print(match.end())
#     print(match.span())

import re
pattern = r'colour'
text1 = 'My favourite colour is red. I love red colour.'
text2 = re.sub(pattern, 'color', text1, count=1) # count value : how many times do you want to change the value?
print(text2)