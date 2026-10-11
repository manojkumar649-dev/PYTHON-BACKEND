class OnlineShopping:

    def __init__(self, name, password):
        self.name = name                 
        self.__password = password       
        self._login_status = False       

    def login(self, password):
        if self.__password == password:
            self._login_status =True
            print('Login successful')
        else:
            print('Invalid password')

    def show_status(self):
        print('Name:', self.name)
        print('Login Status:', self._login_status)

user = OnlineShopping('Manoj', '12345')
print(user.name)
user.login('12345')
user.show_status()
