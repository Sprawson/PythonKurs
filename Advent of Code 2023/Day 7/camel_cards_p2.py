"""--- Part Two ---
To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?"""

def sort_dict(dictionary):
    myKeys = list(dictionary.keys())
    myKeys.sort()
    dictionary_sorted = {i: dictionary[i] for i in myKeys}
    return dictionary_sorted
def kind_of_cards(counters):
    # what if there are Joker cards:
    if 'J' in counters.keys():
        print(counters['J'])

    if len(counters) == 1:
        # 'five_of_kind'
        return '7'
    elif len(counters) == 5:
        #'high_card'
        return '1'

    for item in counters.items():
        # item is for example  ('K', 2)
        if item[1] == 4:
            # 'four_of_kind'
            return '6'
        elif item[1] == 3 and len(counters) == 2:
            # 'full'
            return '5'
        elif item[1] == 3 and len(counters) == 3:
            # 'three_of_kind'
            return '4'
        elif item[1] == 2 and len(counters) == 3:
            # two_pair'
            return '3'
        elif item[1] == 2 and len(counters) == 4:
            # 'one_pair'
            return '2'

def cards_counter(cards):
    card_values = {}
    for card in cards:
        counter = 0
        for x in range(len(cards)):
            if card == cards[x]:
                counter += 1
        card_values.update({card: counter})

    return card_values


file = open("input.txt", 'r')
file_lines = file.readlines()
hands_ratios = []
for line in file_lines:
    hands_ratios.append([line.strip().split(" ")[0], line.strip().split(" ")[1]])


symbol_to_hex = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A', 'J': '1'}
expanded_hands = {}
for cards in hands_ratios:
    # find kind of card
    x = (kind_of_cards(cards_counter(cards[0])))
    # replace symbols to HEX substitute
    for symbol in symbol_to_hex.keys():
        cards[0] = cards[0].replace(symbol, symbol_to_hex[symbol])
    # add kind of card at the start of the hex value (most important bit)
    expanded_hands.update({x + cards[0]: cards[1]})

# sort dict based on keys
expanded_hands_sorted = sort_dict(expanded_hands)
total_winnings = 0
rank = 1
# calculate total winnings
for hand in expanded_hands_sorted:
    total_winnings = total_winnings + (int(expanded_hands_sorted[hand]) * rank)
    rank += 1
print(expanded_hands_sorted)
print(total_winnings)