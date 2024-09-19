"""
Tells the type of poker hand given a list of 5 cards.
"""


from collections import Counter

RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
         '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
SUITS = {'Clubs': 0, 'Diamonds': 1, 'Hearts': 2, 'Spades': 3}

def evaluate_hand(hand):
    ranks = [RANKS[card[0]] for card in hand]
    suits = [card[1] for card in hand]

    # Count the occurrences of each rank and suit
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    # Sort ranks to check for sequences
    sorted_ranks = sorted(ranks)

    # Check for hand types
    is_flush = max(suit_counts.values()) == 5
    is_straight = all(sorted_ranks[i] - sorted_ranks[i - 1] == 1 for i in range(1, 5))
    is_royal = sorted_ranks == [10, 11, 12, 13, 14]

    # Check combinations
    counts = sorted(rank_counts.values(), reverse=True)
    hand_type = None
    if is_flush and is_royal:
        hand_type = ('Royal Flush', 9)
    elif is_flush and is_straight:
        hand_type = ('Straight Flush', 8)
    elif counts == [4, 1]:
        hand_type = ('Four of a Kind', 7)
    elif counts == [3, 2]:
        hand_type = ('Full House', 6)
    elif is_flush:
        hand_type = ('Flush', 5)
    elif is_straight:
        hand_type = ('Straight', 4)
    elif counts == [3, 1, 1]:
        hand_type = ('Three of a Kind', 3)
    elif counts == [2, 2, 1]:
        hand_type = ('Two Pair', 2)
    elif counts == [2, 1, 1, 1]:
        hand_type = ('One Pair', 1)
    else:
        hand_type = ('High Card', 0)
        
    return hand_type, sorted_ranks

# # Example usage
# hand = [('A', 'Hearts'), ('K', 'Hearts'), ('Q', 'Hearts'), ('J', 'Hearts'), ('9', 'Spades')]
# print(evaluate_hand(hand))
