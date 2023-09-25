# -------------------c-3 start-----------------------
class Customer:
    def __init__(self, first_name,family_name,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
        # self.entry_fee = entry_fee

        # def full_name(self):
            # return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age < 20:
            return "1000"
        elif self.age >= 65:
            return "1200"
        else:
            return "1500"

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.entry_fee() # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee() # 1200 という値を返す

print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee())
# ------------------c-3 finish----------------------------------

# -----------------c-2 start-----------------------------------
# class Customer:
#     def __init__(self, first_name,family_name,age):
#         self.first_name = first_name
#         self.family_name = family_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.family_name}"

# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.age  # 15 という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# tom.age # 57 という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.age # 73 という値を返す

# print(ken.age)
# print(tom.age)
# print(ieyasu.age)
# -------------------c-2 finish---------------------------------

# -------------------c-1 start-----------------------------------
# class Customer:
#     def __init__(self, first_name,family_name):
#         self.first_name = first_name
#         self.family_name = family_name

#     def full_name(self):
#         return f"{self.first_name} {self.family_name}"

# ken = Customer(first_name="Ken", family_name="Tanaka")
# ken.full_name()  # "Ken Tanaka" という値を返す
# print(ken.full_name())

# tom = Customer(first_name="Tom", family_name="Ford")
# tom.full_name()  # "Tom Ford" という値を返す
# print(tom.full_name())
# ---------------------c-1 finish--------------------------------------