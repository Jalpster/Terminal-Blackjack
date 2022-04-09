import blackjack


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("Please enter a bet: "))
        except ValueError:
            print("Please input a valid number")
            continue
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total} chips")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    if input("Hit or Stand: ").lower() == "hit":
        hit(deck, hand)
    else:
        playing = False


def show_some(player, dealer):
    print("Dealers Hand:")
    print("<Card Hidden>")
    print(dealer.cards[-1])

    print("----------")

    print("Your Hand:")
    print(*player.cards, sep="\n")
    print("\n")


def show_all(player, dealer):
    print(f"Your Hand (Value: {player.value}):")
    print(*player.cards, sep="\n")

    print("----------")

    print(f"Dealer's Hand (Value {dealer.value}):")
    print(*dealer.cards, sep="\n")
    print("\n")


def player_busts(chips):
    print("You busted")
    dealer_wins(chips)


def player_wins(chips):
    print("You won!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer busts")
    player_wins(chips)


def dealer_wins(chips):
    print("Dealer wins")
    chips.lose_bet()


def push():
    print("Its a tie!")


# Set up the Player's chips
player_chips = blackjack.Chips()

while True:

    playing = True

    # Print an opening statement
    print("Its time for Blackjack!")

    # Create & shuffle the deck, deal two cards to each player
    gamedeck = blackjack.Deck()
    gamedeck.shuffle()

    player_hand = blackjack.Hand()
    player_hand.add_card(gamedeck.deal())
    player_hand.add_card(gamedeck.deal())

    dealer_hand = blackjack.Hand()
    dealer_hand.add_card(gamedeck.deal())
    dealer_hand.add_card(gamedeck.deal())

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(gamedeck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while dealer_hand.value < 17 and player_hand.value < 21:
        dealer_hand.add_card(gamedeck.deal())
        dealer_hand.adjust_for_ace()

    # Show all cards
    show_all(player_hand, dealer_hand)

    # Run different winning scenarios
    if dealer_hand.value > 21:
        dealer_busts(player_chips)
    elif player_hand.value <= 21:
        if player_hand.value > dealer_hand.value:
            player_wins(player_chips)
        else:
            dealer_wins(player_chips)
    else:
        print("You busted, dealer wins.")

    # Inform Player of their chips total
    print("Your Total Chips: ", player_chips.total)
    # Ask to play again

    if input("Play Again? (y/n): ") == "y":
        continue
    else:
        break
