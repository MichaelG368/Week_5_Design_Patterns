from random import randint

class AccountFacade():
    def __init__(self):
        self.__account = Account()
        
    def get_account_number(self):
        return self.__account.get_id_number()
    
class Account():
    def __init__(self, first_name = None, last_name = None, gender = None, address = None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address
        self.__id_number = '{:09}'.format(randint(1, 10**9))
        self.__reward_points = 0
        
    def get_id_number(self):
        return self.__id_number
    
def main():
    get_info = AccountFacade()
    get_info.get_account_number()
    
main()