"""Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?"""


def kind_of_cards(counters):
    if len(counters) == 1:
        return 'five_of_kind'
    elif len(counters) == 5:
        return 'high_card'

    for item in counters.items():
        if item[1] == 5:
            return 'five_of_kind'
        elif item[1] == 4:
            return 'four_of_kind'
        elif item[1] == 3 and len(counters) == 2:
            return 'full'
        elif item[1] == 3 and len(counters) == 3:
            return 'three_of_kind'
        elif item[1] == 2 and len(counters) == 3:
            return 'two_pair'
        elif item[1] == 2 and len(counters) == 4:
            return 'one_pair'


def cards_counter(cards):
    card_values = {}
    for card in cards:
        counter = 0
        for x in range(len(cards)):
            if card == cards[x]:
                counter += 1
        card_values.update({card:counter})

    return card_values

file = open("input.txt", 'r')
file_lines = file.readlines()
hands_ratios = []
for line in file_lines:
    hands_ratios.append((line.strip().split(" ")[0], line.strip().split(" ")[1]))

symbol_to_value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

for cards in hands_ratios:
    print(kind_of_cards(cards_counter(cards[0])))
