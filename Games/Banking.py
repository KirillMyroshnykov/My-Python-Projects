# Banking program

def show_balance(balance, debt):
    print(f'Ваш баланс: ${balance:.2f}')
    print(f'Ваша задолженность по кредиту: ${debt:.2f}')

def deposit():
    amount = float(input('Сколько вы хотите положить на счёт?: '))
    if amount < 0:
        print('Сумма должна быть больше нуля!')
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input('Сколько вы хотите снять со счёта?: '))
    if amount < 0:
        print('Сумма должна быть больше нуля!')
        return 0
    elif amount > balance:
        print('Недостаточно средств!')
        return 0
    else:
        return amount

def credit(year_percent):
    amount = float(input('Сколько вы хотите взять кредитных средств?: '))
    debt = amount + amount*year_percent

    if amount < 0:
        print('Сумма должна быть больше нуля!')
        return 0
    else:
        return debt

def credit_payment(debt):
    amount = float(input('Введите сумму для погашения кредита: '))
    if amount < 0:
        print('Сумма должна быть больше нуля!')
        return 0
    elif amount > debt:
        print('Задолженность по кредиту не может быть отрицательной')
        return 0
    else:
        return amount

def main():
    balance = 0
    debt = 0
    year_percent = 0.07

    while True:
        print('****************************')
        print('Добро пожаловать в наш банк!')
        print('****************************')
        print('Что бы вы хотели сделать?:')
        print('''1.Вывести баланс/Вывести задолженность по кредиту\n2.Положить деньги на счёт\n
              3.Снять деньги со счёта\n4.Взять кредит\n5.Погасить кредит\n6.Выйти''')
        
        option = input('Выберите вариант(1-6): ')

        if option == '1':
            show_balance(balance, debt)
        elif option == '2':
            balance += deposit()
        elif option == '3':
            balance -= withdraw(balance)
        elif option == '4':
            debt += credit(year_percent)
        elif option == '5':
            debt -= credit_payment(debt)
        elif option == '6':
            print('Спасибо! Приходите ещё!')
            break
        else:
            print('Недействительный вариант!')

if __name__ == '__main__':
    main()