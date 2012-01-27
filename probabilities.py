#Jeff Stewart
#1/25/12
#Jan 047


def player_cards_for_hit (total):
    """Counts the number of cards that are possible for a player to accept from hitting without causing the player to bust.

    Returns an integer value of the number of cards which will not cause a player to bust.
    """
    max_val = 21 - total #max_val is the highest value that can be hit without busting
    sum = 0
    for i in range(10):                 #will add all the cards that have a value less than the max_value
        if i + 1 <= max_val:            #if less than or equal to max value that will not result in a bust
            sum += shoe[i]
    return sum


def remove_card (card):
    """Removes a card from the deck.

    Returns None.
    """
    shoe[card - 1] -= 1 #shoe.index(card - 1) - 1
    return


def player_cards_for_bust(total):
    """Calculates the number of cards that will cause a player to bust on the next move.

    Returns an integer
    """
    return cards_left - player_cards_for_hit(total)


def prob_player_bust(total):
    """Calculates the prob that a player will bust on the next card

    Returns a number between 1 and 0
    """
    return player_cards_for_bust(total) / cards_left


def prob_dealer_bust(showing):
    """Calculates the probability that the dealer will bust.
     Currently only checks for the next card.

     Returns a number between 1 and 0
     """
    case_1 = (shoe[0] / cards_left) * dealer_cards_for_bust(showing + 1) / cards_left
    case_2 = (shoe[1] / cards_left) * dealer_cards_for_bust(showing + 2) / cards_left
    case_3 = (shoe[2] / cards_left) * dealer_cards_for_bust(showing + 3) / cards_left
    case_4 = (shoe[3] / cards_left) * dealer_cards_for_bust(showing + 4) / cards_left
    case_5 = (shoe[4] / cards_left) * dealer_cards_for_bust(showing + 5) / cards_left
    case_6 = (shoe[5] / cards_left) * dealer_cards_for_bust(showing + 6) / cards_left
    case_7 = (shoe[6] / cards_left) * dealer_cards_for_bust(showing + 7) / cards_left
    case_8 = (shoe[7] / cards_left) * dealer_cards_for_bust(showing + 8) / cards_left
    case_9 = (shoe[8] / cards_left) * dealer_cards_for_bust(showing + 9) / cards_left
    case_10 = (shoe[9] / cards_left) * dealer_cards_for_bust(showing + 10) / cards_left
    #prob that the dealer will bust on the next card
    bust_on_next = case_1 + case_2 + case_3 + case_4 + case_5 + case_6 + case_7 + case_8 + case_9 + case_10
    return bust_on_next


def dealer_cards_for_bust(total):
    """Calculates the number of cards that will make a dealer bust on the next hit.
    Used multiple times to calculate for each possible card the dealer may have.

    Returns an integer
    """
    sum = 0
    if total >= 17: # handles if dealer must stand
        return 0
    if total <= 11: # handles if dealer cannot bust
        return 0
    lowest_card_for_bust = 22 - total
    for i in range(10):                 # will add all the cards that have a value greater than the lowest for a bust
        if i + 1 >= lowest_card_for_bust:
            sum +=  shoe[i]
    return sum


def prob_win(player, dealer, Dsoft):
    """Calculates the probability that the player will win against the dealer.

    Returns an number between 0 and 1.
    """
    difference = player - dealer
    sum = 0
    for i in range(10):                 # will add all the cards that have a value less than the difference, therefore the player wins
        if i + 1 < difference:            
            sum += shoe[i]
    prob = (sum / cards_left) + prob_dealer_bust(dealer)
    if prob <= 1:
        return prob
    return 1


def count():
    """Calculates the count used in card counting.

    Returns an integer.
    """
    return shoe[9]+shoe[0]-shoe[1]-shoe[2]-shoe[3]-shoe[4]-shoe[5]

# decks can be changed to accommodate different size card shoes.
decks = 1
# shoe contains a list holding all the cards in order of denomination starting at ace ending with 10
shoe = [4.0 * decks, 4.0 * decks, 4.0 * decks, 4.0 * decks, 4.0 * decks, 4.0 * decks, 4.0 * decks, 4.0 * decks, 4.0 * decks, 16.0 * decks,]
cards_left = 52.0 * decks

print "Play blackjack with", decks, "decks of cards"
while input("Would you like to continue? 1/0 "):
    soft = False
    print "The count is:", count(), "bet accordingly.\nGood luck!"


    card1 = input("What is the first card you were delt? (Enter 1 for an Ace)")
    remove_card(card1)
    cards_left -= 1
    card2 = input("What is the second card you were delt? (Enter 1 for an Ace)")
    remove_card(card2)
    cards_left -= 1
    dealer = input("What card is the dealer showing?")
    remove_card(dealer)
    cards_left -= 1

    player_total = card1 + card2
    if card1 == 1:
        soft = True
        player_total += 10
    else:
        if card2 == 1:
            soft = True
            player_total += 10

    if player_total == 21:
        print "Winner Winner, Chicken Dinner!"

    if soft:
        print "You currently have", player_total, "Because you have an ace, your probability of busting if you hit is: ", prob_player_bust(player_total-10)
    else:
        print "You currently have", player_total, "If you hit you have a ", prob_player_bust(player_total), "probability of busting."
    Dsoft = False
    if dealer == 1:
        Dsoft = True
        dealer += 10
        print "The dealer is showing", dealer, "If you do nothing, he has a ", prob_dealer_bust(dealer-10), "probability of busting."
    else:
        print "The dealer is showing", dealer, "If you do nothing, he has a ", prob_dealer_bust(dealer), "probability of busting."
    print "If you do nothing, your probability of winning is:", prob_win(player_total, dealer, Dsoft)
    if prob_player_bust(player_total) >= 1:
        print "You must stand"
    while input("Did you hit? 1/0 "):
        new_card = input("What card did you receive? (1 for Ace) ")
        player_total += new_card
        if player_total < 21 and soft:
            player_total -= 10
        if new_card == 1:
            if player_total <= 11:
                soft = True
                player_total += 10
        if soft:
            print "You currently have", player_total, "Because you have an ace, your probability of busting if you hit is: ", prob_player_bust(player_total-10)
        else:
            print "You currently have", player_total, "If you hit you have a ", prob_player_bust(player_total), "probability of busting."
        print "The dealer is showing", dealer, "If you do nothing, he has a ", prob_dealer_bust(dealer), "probability of busting."
        print "If you do nothing, your probability of winning is:", prob_win(player_total, dealer)
        if prob_player_bust(player_total) >= 1:
            print "You must stand"


    second_dealer = input("What was the dealer's other card? (1 for Ace)")
    remove_card(second_dealer)
    dealer_total = dealer + second_dealer
    while dealer_total < 17:
        new_card = input("What card did the Dealer receive when he hit?? (1 for Ace)")
        remove_card(new_card)
        dealer_total += new_card
        if new_card == 1:
            if dealer_total <= 11:
                dealer_total += 10