class mobile:
    def __init__(self):
        print('I am in mobile class')

class samsung(mobile):
    # pass
    def __init__(self):
        super().__init__()
        print('I am in samsung class')

s = samsung()