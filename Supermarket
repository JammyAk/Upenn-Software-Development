# Jammy Babalola Akodu
# Penn_ID:53573476
# This work was solely completed by myself without help.
import random

cash = 5.00  # starting cash amount
lottery_ticket = 2.00  # price of lottery ticket
apple = 0.99  # price of an apple
beans = 1.58  # price of beans
sodas = 1.23  # price of sodas
cash_amount = 5.00


# Lottery Ticket fucntion will be called if user decides to play
def lottery_ticket(cash=cash):
    '''The probability of wining a lottery ticket is 33%
    (1) Deduct the price of the lottery ticket from available cash
    (2) Generate a random integer from 0-2 to simulate (0, 1, 2) win p =0.33
    (3) Winnings and cash_amount as global variables so that they can be amended later
    '''
    global cash_amount
    global winnings
    print('Good Luck!')
    cash_amount -= 2.00  # subtracting price of lottery ticket from cash
    print('Cash remaining is {}'.format(cash_amount))

    if random.randint(0, 2) == 0:  # 0,1,3: if 0 is generated 1/3 = 0.33 -> WIN
        # WIN
        print("Congratulations! You have won the lottery")
        winnings = round(random.randint(2, 10))
        print('You have won {} dollars'.format(winnings))
        cash_amount += winnings
        print('New cash balance is {} dollars'.format(cash_amount))
    else:
        # LOSS
        print("Sorry, you did not win the lottery.")
        winnings = 0
    return cash_amount


# buy apple function will ask the user if they want apples and the number they want; if they do not want any these
# will be handled and return updated cash amount
def buy_apple(cash=cash):
    '''Asks the user if they want to buy an apple
    (1) if 'Y' then proceed to ask for quantity
    (2) if 'N' then No apples purchased
    function returns total cost of apples.
    global variables ttl_price_apples quantity_apples and cash_amount
    '''
    global ttl_price_apples, quantity_apples, cash_amount
    buy_apples = input('Would you like to purchase any apples? (please respond Y or N)')
    if buy_apples == 'Y' or buy_apples == 'y':
        quantity_apples = input('How many would you like to purchase?')
        try:
            quantity_apples = int(quantity_apples)
        except ValueError as e:
            print('Please can you enter the number of apples you would like to buy as numerical figure.')
            quantity_apples = int(input('How many would you like to purchase?'))
        ttl_price_apples = quantity_apples * apple
        if ttl_price_apples > cash_amount:
            print('Not enough money.')
            quantity_apples = 0
            ttl_price_apples = 0
        else:
            print('You want to buy {} apple(s). This will cost {} dollars'.format(quantity_apples, ttl_price_apples))
            cash_amount = cash_amount - ttl_price_apples
    elif buy_apples == 'N' or buy_apples == 'n':
        print('No apples were purchased')
        quantity_apples = 0
        ttl_price_apples = 0
        # cash_amount = cash
    else:
        print('Please respond appropriately with Y or N')
        buy_apple()
    return cash_amount


# buy beans function will ask the user if they want can of beans and the number they want; if they do not want any
# these will be handled and return updated cash amount
def buy_cansOfBeans(cash=cash_amount):
    '''Asks the user if they want to buy any Beans
    (1) if 'Y' then proceed to ask for quantity
    (2) if 'N' then No Beans purchased
    function returns total cost of apples.
    '''
    global ttl_price_beans, quantity_beans, cash_amount
    buy_beans = input('Would you like to purchase any Beans? (please respond Y or N)')
    if buy_beans == 'Y' or buy_beans == 'y':
        quantity_beans = input('How many would you like to purchase?')
        try:
            quantity_beans = int(quantity_beans)
        except ValueError as e:
            print('Please can you enter the number of cans of beans you would like to buy as numerical figure.')
            quantity_beans = int(input('How many would you like to purchase?'))
        ttl_price_beans = quantity_beans * beans
        if ttl_price_beans > cash_amount:
            print('Not enough money.')
            quantity_beans = 0
            ttl_price_beans = 0
        else:
            print('You want to buy {} cans of beans(s). This will cost {} dollars'.format(quantity_beans,
                                                                                          ttl_price_beans))
            cash_amount = cash_amount - ttl_price_beans
    elif buy_beans == 'N' or buy_beans == 'n':
        print('No cans of beans were purchased')
        ttl_price_beans = 0
        quantity_beans = 0
    else:
        print('Please respond appropriately with Y or N')
        buy_cansOfBeans()
    return cash_amount


# buy sodas function will ask the user if they want apples and the number they want; if they do not want any these
# will be handled and return updated cash amount
def buy_sodas_func(cash=cash_amount):
    '''Asks the user if they want to buy any sodas
    (1) if 'Y' then proceed to ask for quantity
    (2) if 'N' then No Sodas purchased
    function returns total cost of sodas.
    '''
    global ttl_price_sodas, quantity_sodas, cash_amount
    buy_sodas = input('Would you like to purchase any sodas? (please respond Y or N)')
    if buy_sodas == 'Y' or buy_sodas == 'y':
        quantity_sodas = input('How many would you like to purchase?')
        try:
            quantity_sodas = int(quantity_sodas)
        except ValueError as e:
            print('Please can you enter the number of sodas you would like to buy as numerical figure.')
            quantity_sodas = int(input('How many would you like to purchase?'))
        ttl_price_sodas = quantity_sodas * sodas
        if ttl_price_sodas > cash_amount:
            print('Not enough money.')
            quantity_sodas = 0
            ttl_price_sodas = 0
        else:
            print('You want to buy {} sodas(s). This will cost {} dollars'.format(quantity_sodas, ttl_price_sodas))
            cash_amount = cash_amount - quantity_sodas
    elif buy_sodas == 'N' or buy_sodas == 'n':
        print('No sodas were purchased')
        quantity_sodas = 0
        ttl_price_sodas = 0
    else:
        print('Please respond appropriately with Y or N')
        buy_sodas_func()
    return cash_amount


# This supermarket function combines buy_apple, buy_canOfBeans, and buy_sodas-func
# will dynamically update the cash amount available
def supermarket(cash=cash):
    global winnings
    print('Hi, welcome to the supermarket! Before you start shopping would you like a chance to $2-10 from a lottery ticket for the cost of $2')
    lottery_response = input('Does this interest you? (please respond Y or N)')
    if lottery_response == 'Y' or lottery_response == 'y':
        quantity_lottery = 1
        cash_amount = lottery_ticket()
        lottery_cost = 2.00
    elif lottery_response == 'N' or lottery_response == 'n':
        print('No problem at all.')
        quantity_lottery = 0
        lottery_cost = 0.00
        winnings = 0
        cash_amount = cash
    else:
        print('Please respond appropriately with Y or N')
        supermarket()

    print('Below are the products we sell and their respective prices:')
    print('price per apple: $0.99')
    print('price per beans: $1.58')
    print('price per soda: $1.23',end="\n\n")

    cash = round(buy_apple(cash_amount), 2)
    print('You have {} dollars remaining'.format(cash),end="\n\n")
    cash = round(buy_cansOfBeans(cash_amount), 2)
    print('You have {} dollars remaining'.format(cash),end="\n\n")
    cash = round(buy_sodas_func(cash_amount), 2)
    print('You have {} dollars remaining'.format(cash),end="\n\n")

    Total = round(lottery_cost + ttl_price_apples + ttl_price_beans + ttl_price_sodas, 2)
    print('You have {} remaining and here is your basket:'.format(cash),end="\n\n")
    print('You bought {} lottery ticket'.format(quantity_lottery))
    print('You won {} dollars from the lottery'.format(winnings))
    print('You bought {} apple(s)'.format(quantity_apples))
    print('You bought {} cans of beans'.format(quantity_beans))
    print('You bought {} sodas'.format(quantity_sodas))

    print('The total cost of your shop comes to {} dollars '.format(Total))


if __name__ == '__main__':
    supermarket()
