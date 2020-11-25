# parent class, super class, based class
class mobile:
    def call(self):
        print('You can call')
    def message(self):
        print('You can message')

# child class, sub class, derived class
class samsung(mobile): # mobile is superclass and samsung is subclass
    # def call(self):
    #     print('You can call')
    # def message(self):
    #     print('You can message')
    def photo(self):
        print('You can click photo')

s = samsung()
s.call()
s.message()
s.photo()
# print(issubclass(samsung,mobile))