class student:
    # roll = ''
    # gpa = ''

    # def setValue(self, roll, gpa):
    #     self.roll = roll
    #     self.gpa = gpa
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
        
    def display(self):
        print(f'Roll : {self.roll}, GPA : {self.gpa}')

sabirul = student(101, 3.19)
# print(isinstance(sabirul, student)) # showing true / false
# sabirul.roll = 101
# sabirul.gpa = 3.19

# sabirul.setValue(101, 3.19)
sabirul.display()

# print(f'Roll : {sabirul.roll}, GPA : {sabirul.gpa}')

shimul = student(102, 4.00)
# shimul.roll = 102
# shimul.gpa = 4.00

# shimul.setValue(102, 4.00)
shimul.display()

# print(f'Roll : {shimul.roll}, GPA : {shimul.gpa}')