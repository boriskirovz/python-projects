class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = float(balance)
        self.pin = pin
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else: print("You must enter positive amount of money")

    def withdraw(self, amount, pin):
        if self.pin == pin:
            if self.balance - amount < 0:
                print("Not Enough money in balance")
            else: self.balance -= amount
        else: print("Wrong pin")
    
    def get_account_info(self):
        print(f"{self.account_number} | {self.balance}")
        

print("--- Създаване на банкова сметка ---")
acc_num = input("Номер на сметката: ")

while True:
    try:
        start_bal = float(input("Начален баланс: "))
        if start_bal < 0:
            print("Началният баланс не може да бъде отрицателен.")
            continue
        break
    except ValueError:
        print("Моля, въведете валидно число за баланс.")

acc_pin = input("ПИН код: ")

my_account = Account(acc_num, start_bal, acc_pin)

# Меню цикъл
while True:
    print("\n==================")
    print("МЕНЮ")
    print("==================")
    print("1. Депозит")
    print("2. Теглене")
    print("3. Инфо за сметката")
    print("4. Изход")
    print("==================")
    
    choice = input("Въведете номер на операция: ")

    match choice:
        case '1':
            try:
                amount = float(input("Депозит: "))
                my_account.deposit(amount)
            except ValueError:
                print("Невалидна сума.")

        case '2':
            try:
                amount = float(input("Сума за теглене: "))
                pin_input = input("ПИН код: ")
                my_account.withdraw(amount, pin_input)
            except ValueError:
                print("Невалидна сума.")

        case '3':
            print() 
            my_account.get_account_info()

        case '4':
            print("Довиждане!")
            break
        
        case _:
            print("Невалидна операция. Моля, опитайте отново.")