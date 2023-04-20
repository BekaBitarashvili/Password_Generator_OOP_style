import random

pass_length = int(input("შეიყვანეთ პაროლის სიგრძე: "))
pass_lower = input("დაბალი ასოები პაროლში: (ki/ara) ")
pass_upper = input("მაღალი ასოები პაროლში: (ki/ara) ")
pass_nums = input("ციფრები პაროლში: (ki/ara) ")

class RandomPasswordGenerator:
    def __init__(self, pass_length, pass_lower, pass_upper, pass_nums):
        self.pass_length = pass_length
        self.pass_lower = pass_lower
        self.pass_upper = pass_upper
        self.pass_nums = pass_nums
    
    def generate_password(self):
        small_letters = "abcdefghijklmnopqrstuvwxyz"
        big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        
        chars = ""
        if self.pass_lower == "ki":
            chars += small_letters
        if self.pass_upper == "ki":
            chars += big_letters
        if self.pass_nums == "ki":
            chars += digits

        pass_data = "".join(random.choice(chars) for _ in range(self.pass_length))
        return pass_data

generator = RandomPasswordGenerator(pass_length, pass_lower, pass_upper, pass_nums)
pass_data = generator.generate_password()
print(f"შემთხვევითი პაროლია: {pass_data}")