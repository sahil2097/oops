class password:

    __password1 = 'abc@123'

    def access_password(self):
        print(password.__password1)

    def change_password(self):
        self.__password1 = 'sahil@123'

ps = password()
ps.access_password()
# accessing private data using class is called data abstraction
print(ps._password__password1)

ps._password__password1 = '123@abc'
ps.access_password()

# we are using data encapsulation by changing the private variable data through function
ps.change_password()
print(ps._password__password1)