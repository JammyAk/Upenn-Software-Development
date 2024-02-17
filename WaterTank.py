# TODO: Students, fill out statement of work header
# Student Name in Canvas: Jammy Akodu
# Penn ID: 53573476
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: none

from random import shuffle, choice
import math

# power cards
pwr = ['SOH', 'DOT', 'DMT']


def get_user_input(question):
    '''
    Prompt the user with the given question and process the input.
    :param question: Given Question
    :return: Return the post-processed user input
    '''
    power_cards = ['SOH', 'DOT', 'DMT']
    while True:
        # Remove leading and trailing whitespaces
        input_from_user = input(question).strip()

        if len(input_from_user) == 0:
            print("Invalid input. Please try again.")
            continue

        if input_from_user.isdigit():
            try:
                # Cast input_from_user to integer
                return int(input_from_user)
            except ValueError:
                # If casting to integer fails, return input_from_user
                return input_from_user.lower()

        # Check for power card
        if input_from_user.upper() in power_cards:
            return input_from_user.upper()  # Return power card in uppercase
        else:
            return input_from_user.lower()  # Return input in lowercase if not a power card


def setup_water_cards():
    '''
    Creates a shuffled list of water cards
    :return: Deck of water cards
    '''

    # water cards
    card_values = [1, 5, 10]
    card_quantities = [30, 15, 8]

    # Create an empty list to store water cards
    water_cards = []

    # Populate the water_cards list based on values and quantities
    for value, quantity in zip(card_values, card_quantities):
        water_cards.extend([value] * quantity)

    shuffle(water_cards)

    return water_cards


def setup_power_cards():
    '''
    Creates a shuffled list of power cards
    :return: Deck of power cards
    '''

    # power cards
    card_values = ['SOH', 'DOT', 'DMT']
    card_quantities = [10, 2, 3]

    # list to store power cards
    power_cards = []

    # Populate the power_cards list based on values and quantities
    for value, quantity in zip(card_values, card_quantities):
        power_cards.extend([value] * quantity)

    shuffle(power_cards)

    return power_cards


def setup_cards():
    '''
    Sets up both the water card and power card piles as described in the setup_water_cards and setup_power_cards functions
    :return: Return a 2-tuple containing the water cards pile and the power cards pile, respectively.
    '''
    water_cards = setup_water_cards()
    power_cards = setup_power_cards()
    return water_cards, power_cards


def get_card_from_pile(pile, index):
    '''
    Removes the entry at the specified index of the given pile (water or power) and modifies the pile by reference.
    :param pile: List from either water or power cards
    :param index: index at which card is taken from pile
    :return: card from list the entry at the specified index
    '''
    card = pile.pop(index)

    return card


def arrange_cards(cards_list):
    '''
    Arranges the players cards such that: The first three indices are water cards, sorted in ascending order.
    And The last two indices are power cards, sorted in alphabetical order.
    :param cards_list: List of cards from player or computer
    '''
    # Separate water and power cards
    water_cards = [card for card in cards_list if isinstance(card, int)]
    power_cards = [card for card in cards_list if isinstance(card, str)]

    # Arrange water cards in ascending order
    water_cards.sort()

    # Arrange power cards in alphabetical order
    power_cards.sort()

    # Update cards_list
    cards_list[:3] = water_cards
    cards_list[3:] = power_cards


def deal_cards(water_cards_pile, power_cards_pile):
    '''
    This function deals each player 3 water cards and 2 power cards by using .pop(index0) we get the first element in the list.
    :param water_cards_pile: List of water cards
    :param power_cards_pile: List of power cards
    :return: arranges player one and two cards
    '''

    player_one_hand = []
    player_two_hand = []

    for card in range(3):
        # Deal 3 water cards alternately
        player_one_hand.append(water_cards_pile.pop(0))
        player_two_hand.append(water_cards_pile.pop(0))

    for card in range(2):
        # Deal 2 power cards alternately
        player_one_hand.append(power_cards_pile.pop(0))
        player_two_hand.append(power_cards_pile.pop(0))

    # Arrange the cards for each player
    arrange_cards(player_one_hand)
    arrange_cards(player_two_hand)

    return player_one_hand, player_two_hand


def apply_overflow(tank_level):  # fix tank level
    '''
    Finds out tank level including if any overflow has occured
    remaining water = maximum fill value - overflow
    :param tank_level: int - level of player or computer tank level
    :return:Return the tank level. If no overflow occurred, this is just the starting tank level
    '''
    maximum_fill_value = 80
    if tank_level > maximum_fill_value:
        overflow = tank_level - maximum_fill_value
        new_tank_level = maximum_fill_value - overflow
        return new_tank_level
    else:
        return tank_level


def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    '''
    Get that card from the player’s hand, and update the tank level based on the card that was used. This does not include drawing a replacement card, so after using the card, the player_cards size will only be 4 cards.
    Overflow applied if necessary.
    :param player_tank: Player Tank level
    :param card_to_use: Card in play
    :param player_cards: List of cards from player or computer
    :param opponent_tank: Computer Tank level
    :return:Return a 2-tuple containing the player’s tank and the opponent’s tank, respectively.
    '''

    if card_to_use in player_cards:
        if isinstance(card_to_use, int):  # Regular water card
            # Update tank level based on the card used
            player_tank += card_to_use
        else:  # Power card
            if card_to_use == 'SOH':  # steal half
                opponent_tank -= max(0, int(opponent_tank / 2))  # Decrease opponent's tank by half
                player_tank += int(opponent_tank)
            elif card_to_use == 'DOT':
                opponent_tank = 0  # Drain opponents tank
            elif card_to_use == 'DMT':
                player_tank = player_tank * 2  # Double players tank

        player_cards.remove(card_to_use)

        # Check for overflow
        player_tank = apply_overflow(player_tank)

        return player_tank, opponent_tank
    else:
        print("Invalid card. Please try again.")
        return player_tank, opponent_tank


def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    '''
    Discard the given card from the player’s hand and return it to the bottom of the appropriate pile.
    :param card_to_discard: integer or string card selected to remove
    :param player_cards: List - player available cards
    :param water_cards_pile: List -  water cards pile
    :param power_cards_pile: List -  power cards pile
    :return:This function does not return anything.
    '''

    player_cards.remove(card_to_discard)
    # (Water cards should go in the water card pile and power cards should go in the power card pile.)
    if isinstance(card_to_discard, int):
        water_cards_pile.append(card_to_discard)
    else:
        power_cards_pile.append(card_to_discard)


def filled_tank(tank):
    '''
    Determine if the tank level is between the maximum and minimum fill values (inclusive).
    This will be True if the tank is filled
    :param tank: Tank level
    :return: Return a boolean representing whether the tank is filled
    '''
    maximum_fill_value = 80
    minimum_fill_value = 75
    return minimum_fill_value <= tank <= maximum_fill_value


def check_pile(pile, pile_type):
    '''
    Checks if the given pile is empty. If so, call the pile’s setup function to replenish the pile.
    :param pile: List of available cards
    :param pile_type: pile_type is a string to determine what type of pile you are checking (“water” or
    “power”)
    :return: This function does not return anything
    '''
    if len(pile) == 0:
        if pile_type == 'water':
            pile.extend(setup_water_cards())
        elif pile_type == 'power':
            pile.extend(setup_power_cards())


def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
    '''
    :param human_tank: human player’s water level
    :param human_cards: List object - human cards
    :param water_cards_pile: List object - water cards pile
    :param power_cards_pile: List object - power cards pile
    :param opponent_tank: computer player’s water level
    :return: tuple containing the human’s tank level and the computer’s tank level, respectively
    '''

    # human player’s water level and the computer player’s water level
    print('\n')
    print('===Human Play===')
    print(f"Your water level: {human_tank}")
    print(f"Computer's water level: {opponent_tank}")
    print(f"Your hand: {human_cards}")

    # Asking whether player wants to use or discard a card get_user_input function
    action = get_user_input("Do you want to use or discard a card? Enter (u / d): ")
    while action not in ['u', 'd']:
        action = get_user_input("Do you want to use or discard a card? Enter (u / d): ")

    if action == 'u':
        card_to_use = get_user_input("Enter the card you want to use: ")
        while card_to_use not in human_cards:
            print("You don't have that card. Please choose a card from your hand.")
            card_to_use = get_user_input("Enter the card you want to use: ")
        human_tank, opponent_tank = use_card(human_tank, card_to_use, human_cards, opponent_tank)
        if isinstance(card_to_use, int):
            drawn_card = get_card_from_pile(water_cards_pile, 0)
            card_type = 'water'
        else:
            drawn_card = get_card_from_pile(power_cards_pile, 0)
            card_type = 'power'
    elif action == 'd':
        card_to_discard = get_user_input("Enter the card you want to discard: ")
        while card_to_discard not in human_cards:
            print("You don't have that card. Please choose a card from your hand.")
            card_to_discard = get_user_input("Enter the card you want to discard: ")
        discard_card(card_to_discard, human_cards, water_cards_pile, power_cards_pile)
        if isinstance(card_to_discard, int):
            drawn_card = get_card_from_pile(water_cards_pile, 0)
            card_type = 'water'
        else:
            drawn_card = get_card_from_pile(power_cards_pile, 0)
            card_type = 'power'

    human_cards.append(drawn_card)
    print(f"Player drawing {card_type} card:", drawn_card)
    print(f"Your water level is now: {human_tank}")
    print(f"Computer's water level is now at: {opponent_tank}")

    # Draw a new card
    arrange_cards(human_cards)
    print(f"Your cards are now: {human_cards} ")

    return human_tank, opponent_tank


def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):
    '''
    Computer play

    :param computer_tank: int - computer tank level
    :param computer_cards: List object - computer available cards
    :param water_cards_pile: List object - water cards pile
    :param power_cards_pile: List object - power cards pile
    :param opponent_tank: Player tank level
    :return: Return a 2-tuple containing the computer’s tank level and the human’s tank level,
    respectively
    '''
    print('\n')
    print("=== Computer Player's turn ===")
    print("Computer's water level is at:", computer_tank)
    print("Your water level is at:", opponent_tank)
    print("Computer's hand:", computer_cards)

    # Computer strategy :
    # Check if the computer's tank is greater than 30, and if so, use the 'DMT' power card
    if opponent_tank == 0 and 'DMT' in computer_cards:
        card_to_use = 'DMT'
    elif computer_tank > 30 and 'SOH' in computer_cards:
        card_to_use = 'SOH'
    elif opponent_tank > 10 and 'SOH' in computer_cards:
        card_to_use = 'SOH'
    elif opponent_tank > 50 and 'DOT' in computer_cards:
        card_to_use = 'DOT'
    else:
        # Use the maximum integer value card available
        card_to_use = max(computer_cards[:3])

    print("Computer playing with card:", card_to_use)
    computer_tank, opponent_tank = use_card(computer_tank, card_to_use, computer_cards, opponent_tank)

    if isinstance(card_to_use, int):
        drawn_card = get_card_from_pile(water_cards_pile, 0)
        card_type = 'water'
    else:
        drawn_card = get_card_from_pile(power_cards_pile, 0)
        card_type = 'power'

    computer_cards.append(drawn_card)
    print(f"Computer drawing {card_type} card:", drawn_card)

    # check if piles are empty and draw a new card
    check_pile(water_cards_pile, 'water')
    check_pile(power_cards_pile, 'power')

    # arranging
    arrange_cards(computer_cards)
    print(f"Computer's water level is now at: {computer_tank}")

    return computer_tank, opponent_tank


def main():
    '''
    Game Logic: Random player to go first.For each turn, a player can use a card (then draw a new card) or discard a card (then draw a new card).
    '''

    print('Welcome to the WATER TANK game and play against the computer!')
    print('The first player to fill their tank wins the game.')
    print('Good luck!')
    print('\n')

    # Randomly choose the starting player
    starting_player = "human" if choice([True, False]) else "computer"

    # Set up water and power card piles
    water_cards_pile, power_cards_pile = setup_cards()

    # Set up initial tank levels
    human_tank = 0
    computer_tank = 0

    # Set up initial hands for players
    human_cards, computer_cards = deal_cards(water_cards_pile, power_cards_pile)

    # Game loop
    while True:
        while True:
            if starting_player == "human":
                human_tank, computer_tank = human_play(human_tank, human_cards, water_cards_pile, power_cards_pile,
                                                       computer_tank)
                # Check if any player has filled their tank
                if filled_tank(human_tank):
                    print('\n')
                    print('=== Game Over ===')
                    print("Congratulations! You filled your tank and won the game!")
                    print("Player Tank level".format(human_tank))
                    return
                starting_player = "computer"
            else:
                computer_tank, human_tank = computer_play(computer_tank, computer_cards, water_cards_pile,
                                                          power_cards_pile,
                                                          human_tank)
                # Check if any player has filled their tank
                if filled_tank(computer_tank):
                    print('\n')
                    print('=== Game Over ===')
                    print("Sorry! The computer filled its tank and won the game!")
                    print("Computer Tank level".format(computer_tank))
                    return
                starting_player = "human"


if __name__ == '__main__':
    main()