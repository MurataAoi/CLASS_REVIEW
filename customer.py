# -----------------------start c-8------------------------------------
# class Customer:
#     def __init__(self, first_name, family_name, age):
#         self.first_name = first_name
#         self.family_name = family_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.family_name}"

#     def entry_fee(self):
#         if self.age <= 3:
#             return "0"
#         elif self.age >= 75:
#             return "500"
#         elif self.age < 20:
#             return "1000"
#         elif self.age >= 65:
#             return "1200"
#         else:
#             return "1500"

#     # def info_csv(self):
#     #     # csv_string = f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}"
#     #     not_csv_string = f"{self.full_name()}|{self.age}|{self.entry_fee()}"
#     #     return not_csv_string

#     def info_pipe(self):
#         return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


# Aoi = Customer(first_name="Aoi", family_name="Murata", age=100)
# Aoi.info_pipe()

# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.info_pipe()  # "Ken Tanaka,15,1000" という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom.info_pipe()  # "Tom Ford,57,1500" という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.info_pipe()  # "Ieyasu Tokugawa,73,1200" という値を返す

# print(Aoi.info_pipe())
# print(ken.info_pipe())
# print(tom.info_pipe())
# print(ieyasu.info_pipe())
# -----------------------finishs c-8----------------------------------
# -----------------------c-7 start------------------------------------
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return "0"
        elif self.age >= 75:
            return "500"
        elif self.age < 20:
            return "1000"
        elif self.age >= 65:
            return "1200"
        else:
            return "1500"

    # def info_csv(self):
    #     # csv_string = f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}"
    #     not_csv_string = f"{self.full_name()}   {self.age}  {self.entry_fee()}"
    #     return not_csv_string

    def info_tab(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"


Aoi = Customer(first_name="Aoi", family_name="Murata", age=100)
Aoi.info_tab()

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_tab()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.info_tab()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_tab()  # "Ieyasu Tokugawa,73,1200" という値を返す

print(Aoi.info_tab())
print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())
# -----------------------c-7 finish-----------------------------------
# -----------------------c-6 start------------------------------------
# class Customer:
#     def __init__(self, first_name, family_name, age):
#         self.first_name = first_name
#         self.family_name = family_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.family_name}"

#     def entry_fee(self):
#         if self.age <= 3:
#             return "0"
#         elif 3 < self.age < 20:
#             return "1000"
#         elif 20 <= self.age < 65:
#             return "1500"
#         elif 65 <= self.age < 75:
#             return "1200"
#         else:
#             return "500"

#     def info_csv(self):
#         # csv_string = f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}"
#         csv_string = f"{self.full_name()},{self.age},{self.entry_fee()}"
#         return csv_string


# Aoi = Customer(first_name="Aoi", family_name="Murata", age=100)
# Aoi.info_csv()

# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom.info_csv()  # "Tom Ford,57,1500" という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す

# print(Aoi.info_csv())
# print(ken.info_csv())
# print(tom.info_csv())
# print(ieyasu.info_csv())
# -----------------------c-6 finish----------------------------------
# ----------------------c-5start------------------------------------
# class Customer:
#     def __init__(self, first_name, family_name, age):
#         self.first_name = first_name
#         self.family_name = family_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.family_name}"

#     def entry_fee(self):
#         if self.age <= 3:
#             return "0"
#         elif self.age < 20:
#             return "1000"
#         elif self.age >= 65:
#             return "1200"
#         else:
#             return "1500"

#     def info_csv(self):
#         # csv_string = f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}"
#         csv_string = f"{self.full_name()},{self.age},{self.entry_fee()}"
#         return csv_string


# Aoi = Customer(first_name="Aoi", family_name="Murata", age=0)
# Aoi.info_csv()

# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom.info_csv()  # "Tom Ford,57,1500" という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す

# print(Aoi.info_csv())
# print(ken.info_csv())
# print(tom.info_csv())
# print(ieyasu.info_csv())
# ----------------------c-5 finish----------------------------------
# ----------------------c-4 start----------------------------------
# class Customer:
#     def __init__(self, first_name, family_name, age):
#         self.first_name = first_name
#         self.family_name = family_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.family_name}"

#     def entry_fee(self):
#         if self.age < 20:
#             return "1000"
#         elif self.age >= 65:
#             return "1200"
#         else:
#             return "1500"

#     def info_csv(self):
#         # csv_string = f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}"
#         csv_string = f"{self.full_name()},{self.age},{self.entry_fee()}"
#         return csv_string


# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom.info_csv()  # "Tom Ford,57,1500" という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す

# print(ken.info_csv())
# print(tom.info_csv())
# print(ieyasu.info_csv())
# -------------------c-4 finish--------------------------------
# -------------------c-3 start--------------------------------
# class Customer:
#     def __init__(self, first_name, family_name, age):
#         self.first_name = first_name
#         self.family_name = family_name
#         self.age = age
#         # self.entry_fee = entry_fee

#     def full_name(self):
#         return f"{self.first_name} {self.family_name}"

#     def entry_fee(self):
#         if self.age < 20:
#             return "1000"
#         elif self.age >= 65:
#             return "1200"
#         else:
#             return "1500"


# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.entry_fee()  # 1000 という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom.entry_fee()  # 1500 という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.entry_fee()  # 1200 という値を返す

# print(ken.entry_fee())
# print(tom.entry_fee())
# print(ieyasu.entry_fee())
# ------------------c-3 finish----------------------------------

# -----------------c-2 start-----------------------------------
# class Customer:
#     def __init__(self, first_name, family_name, age):
#         self.first_name = first_name
#         self.family_name = family_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.family_name}"


# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.age  # 15 という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom.age  # 57 という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.age  # 73 という値を返す

# print(ken.age)
# print(tom.age)
# print(ieyasu.age)
# -------------------c-2 finish---------------------------------

# -------------------c-1 start-----------------------------------
# class Customer:
#     def __init__(self, first_name, family_name):
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