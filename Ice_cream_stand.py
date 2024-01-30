# Student Name in Canvas: Jammy Akodu


from random import randint, choice

def print_welcome_and_menu(list_of_flavors, list_of_sizes, list_of_prices):
    """
    Prints the following:
    1. Welcome message (Must contain word 'welcome')
    2. Message on what flavors are available in the ice cream store.
        Hint: Loop through the list_of_flavors
    3. Message on how much each size cost.
        Hint: Loop through the list_of_sizes, list_of_prices
        Format should be: Our {size} ice cream is ${price}.
    """

    print('Welcome to Penn\'s Student Run Ice Cream Stand!',end='\n')
    print('Our current flavors for today are:')
  
    #iterating over list of flavours and printing each item
    for flavor in list_of_flavors:
        print(flavor)
    print('')
    # sequence of indicies to match list_of_sizes to list_of_prices
    # assuming that the list have the same length
    for i in range(len(list_of_sizes)):
        size = list_of_sizes[i]
        price = list_of_prices[i]
        print('Our {} ice cream is ${}'.format(size, price))

def get_order_qty(customer_name):
    """
    Asks the customer how many orders of ice cream they want.
    Valid order quantity should is an integer 1-5 inclusive. If outside the range or non-int, re-prompt.
    Returns: How many orders of ice cream the customer wants.
    """
    order_qty = 0

    while True: # create an infinite loop to get the right quantity
        try:
            #Asking how many order of ice cream
            order_quantity = int(input('Welcome {} How many ice creams will you be ordering (1 to 5)?'.format(customer_name)))
            if order_quantity in range(1, 6):
                return order_quantity
            else: #if we fail make user re-enter a qty
                order_quantity = int(input('Welcome {} How many ice creams will you be ordering (1 to 5)?'.format(customer_name)))
        except ValueError: #if we can't cast ask for valid integer
            print('Please enter a valid integer')

def get_ice_cream_flavor(ice_cream_flavors):
    """
    Asks the customer 'Which flavor would you like (v/c/s)? '
    Then, processes and cleans the input and returns the equivalent flavor from ice_cream_flavors list.
    Returns: String of ice cream flavor picked (e.g "Vanilla")
    """
    flavor_picked = ""
  
    while True:
        input = get_first_letter_of_user_input('Which flavor would you like (v/c/s)?')
        if input == 'v':
            flavor_picked = ice_cream_flavors[0]
            break
        if input == 'c':
            flavor_picked = ice_cream_flavors[1]
            break
        if input == 's':
            flavor_picked = ice_cream_flavors[2]
            break
        if input not in 'vcs':
           continue
    return flavor_picked

def get_ice_cream_size(ice_cream_sizes):
    """
    Ask the customer 'Which size would you like (s/m/l)? '
    Then, processes and cleans the input and returns the equivalent size from ice_cream_sizes list.
    Returns: String of Size picked (e.g "Small")
    ice_cream_sizes = get_ice_cream_size['Small', 'Medium', 'Large']
    """
    size_picked = ""
    # TODO: Write your code here
    while True:
        input = get_first_letter_of_user_input('Which size would you like (s/m/l)?')
        if input == 's':
            size_picked = ice_cream_sizes[0]
            break
        if input == 'm':
            size_picked = ice_cream_sizes[1]
            break
        if input == 'l':
            size_picked = ice_cream_sizes[2]
            break
        if input not in 'sml':
           continue

    return size_picked


def get_ice_cream_order_price(ice_cream_size, ice_cream_prices, ice_cream_sizes):
    """
    Returns: The equivalent price of an ice cream size. Example: Returns 4.99 if ice_cream_size is 'Small'
    ice_cream_sizes = ['Small', 'Medium', 'Large']
    ice_cream_prices = [4.99, 7.49, 8.49]
    """
    order_price =""
  
    if ice_cream_size == ice_cream_sizes[0]:
        order_price = ice_cream_prices[0]
    if ice_cream_size == ice_cream_sizes[1]:
        order_price = ice_cream_prices[1]
    if ice_cream_size == ice_cream_sizes[2]:
        order_price = ice_cream_prices[2]

    return order_price


def take_customer_order(customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices):
    """
    This function runs when a customer reaches the front of the queue. It prints
    the current customer's name being served, and take their order(s).
    Returns: Amount of Revenue from the sale with customer
    """

    total_bill = 0
    # a message "Now serving customer: X" where X is the current customer's name
    print("Now serving customer: {}".format(customer_name))

    order_qty = get_order_qty(customer_name)

    #For Each order you get a flavor, and size
    for order in range(order_qty):
        print("Order No.:", order + 1)
        #get the ice cream flavor for this order
        flavor = get_ice_cream_flavor(ice_cream_flavors)

        #get the ice cream size for this order
        ice_cream_size = get_ice_cream_size(ice_cream_sizes)

        #get the price for this order
        price = get_ice_cream_order_price(ice_cream_size, ice_cream_prices, ice_cream_sizes)

        #Update the total_bill
        total_bill += price

        #Print the details for this order (e.g You ordered a Small Vanilla for $4.99)
        print('You ordered a {} {} for ${}'.format(ice_cream_size,flavor,price))
      
    total_bill = round(total_bill,2)

    print('Your total bill is: ${}'.format(total_bill))
  
    p_or_c = get_first_letter_of_user_input('Would you like to pay or cancel the order (p/c)?')
    if p_or_c == 'c':
        total_bill = 0

    return total_bill


def get_first_letter_of_user_input(question):
    """
    Takes in a string as its argument, to be used as the question you want the user to be asked.
    Returns: The first letter of the input the user provides. Ask again if the input is empty.
    """

    #get first letter from question given inside
    while True:
        input_from_user = input(question).strip()
        #checks if input_from_user is a falsy value (an empty string).
        if not input_from_user:
            continue
        #checks if input_from_user is not in the alphabet
        if not input_from_user.isalpha():
            continue
        try:
            first_letter = input_from_user[0].lower()
            #break if true
            break
        except ValueError:
            print('please try again')
    return first_letter


def are_all_customers_served(customer_queue_length):
    """
    If there are no customers in the queue, returns True, and all customers have been served.
    Otherwise, returns False.
    Returns: True or False
    """
    if customer_queue_length == 0:
        return True
    else:
        return False


def print_current_status(customers_served, tracking_revenue):
    """
    Prints a message of how many customers have been served and the total sales of the ice cream stand.
    No Return, only print statements
    """
    print('\n')
    print('We have now served {} customer(s), and received ${} in revenue'.format(customers_served,round(tracking_revenue,2)))


def print_sales_summary(customers_served, tracking_revenue):
    """
    Takes in the arguments customers_served and tracking_revenue. Prints both
    arguments as strings to let the user know what those values are.
    Output should look something like:
        Total customers served: 3
        Total sales           : $xx.xx
    """
    print('Customers served:  {}'.format(customers_served))
    print('Total revenue: $ {}'.format(round(tracking_revenue,2)))


def random_queue_length():
    """
    Takes no arguments.
    Uses the imported randint function to generate a random integer between 2 and 5 inclusive.
    """
    rand_int = randint(2,5)
    return rand_int


def main():
    """
    Lists of available flavors, sizes and prices. DO NOT CHANGE.
    For sizes and prices, we will use the following convention:
    Index 0 for Small
    Index 1 for Medium
    Index 2 for Large
    """
    ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    ice_cream_sizes = ['Small', 'Medium', 'Large']
    ice_cream_prices = [4.99, 7.49, 8.49]

    #List of names of possible customers
    customer_names = ["Alice", "Bob", "Charlie", "Dan", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

    program_running = True
    while program_running:
        # set shop to open
        input('Press enter to open the shop! ')
        queue_is_open = True

        print_welcome_and_menu(list_of_flavors=ice_cream_flavors, list_of_sizes=ice_cream_sizes, list_of_prices=ice_cream_prices)

        tracking_revenue = 0

        # will hold the list of names of the customers in the queue
        customers_in_queue = []
        customers_served = 0

        # random_queue_length function
        num_of_customers_in_queue = random_queue_length()

        #customers are in the queue
        print('Num of customers in queue:  {}'.format(num_of_customers_in_queue))


        for person in range(1,num_of_customers_in_queue+1):
            customers_in_queue.append(choice(customer_names))

        while queue_is_open:
            current_customer_name = customers_in_queue[0]
            customers_in_queue.pop(0)

            #Take a customer at the window and update the revenue
            revenue = take_customer_order(customer_name = current_customer_name, ice_cream_flavors = ice_cream_flavors, ice_cream_sizes= ice_cream_sizes, ice_cream_prices =ice_cream_prices)

            #Update the customers_served variable
            customers_served += 1
            tracking_revenue += revenue

            print_current_status(customers_served, tracking_revenue)


            #  Check if there are any more customers in the queue.
            #  If False, continue the loop.
            #  If True, call the print_sales_summary(customers_served, tracking_revenue) and close the queue
            if are_all_customers_served(len(customers_in_queue)):
                print_sales_summary(customers_served, tracking_revenue)
                queue_is_open = False

        #Asking if you want to open the ice cream stand again "Do you want to open again (y/n)? "
        again = get_first_letter_of_user_input('Do you want to open again (y/n)? ')
        if again != 'y':
            program_running = False

if __name__ == '__main__':
    main()


