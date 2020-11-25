# num = input('Enter a number : ')
# num = int(input('Enter a number : '))
# result = 20 / num
# print(result)

# text = 'shimul'
# print(text[6])
# print('done')

# try:
#     num = [20, 0, 30.5]
#     result = num[1] / num[2]
#     print(result)
#     print('done')

# # except ZeroDivisionError:
# #     print('Divided by zero is not possible')
# # except IndexError:
# #     print('Index Error')
# except (ValueError, ZeroDivisionError, IndexError):
#     print('Your input is incorrect')
# finally:
#     print('Thanks')


def voter(age):
    if age < 18:
        raise ValueError ('Not Allowed')
    return 'You are allowed to vote'

try:
    print(voter(19))
except ValueError as error:
    print(error)
