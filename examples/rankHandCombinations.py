"""
Evaluates all valid poker hands that can be formed from the given cards.
Returns a dictionary of unique valid hands, the best hand, and its name.
"""

from evaluateHand import evaluate_hand
from itertools import combinations

def all_valid_hands(all_cards):
    all_hands = {}
    best_hand = None
    best_hand_name = None
    best_rank = (-1, [])

    # Generate all 5-card combinations
    for combo in combinations(all_cards, 5):
        hand_type, sorted_ranks = evaluate_hand(combo)

        # Only store unique valid hands (ignoring 'High Card' as it's not a valid poker hand)
        if hand_type[0] != 'High Card':
            if hand_type[0] not in all_hands:
                all_hands[hand_type[0]] = []
            all_hands[hand_type[0]].append((combo, sorted_ranks))
        
        # Update the best hand if current is better
        if hand_type[1] > best_rank[0] or (hand_type[1] == best_rank[0] and sorted_ranks > best_rank[1]):
            best_rank = (hand_type[1], sorted_ranks)
            best_hand = combo
            best_hand_name = hand_type[0]

    return all_hands, best_hand, best_hand_name, best_rank

# # Example usage
# all_cards = [('A', 'Hearts'), ('K', 'Hearts'), ('Q', 'Hearts'), ('8', 'Spades'), ('9', 'Hearts'), ('10', 'Diamonds'), ('J', 'Hearts')]
# valid_hands, best_hand, best_hand_name, best_rank = all_valid_hands(all_cards)

# print("All Valid Hands:")
# for hand_type, hands in valid_hands.items():
#     print(f"\n{hand_type}:")
#     for combo, sorted_ranks in hands:
#         print(f"  Hand: {combo}, Sorted Ranks: {sorted_ranks}")

# print("\nBest Hand:")
# print("Hand:", best_hand)
# print("Hand Type:", best_hand_name)
# print("Hand Type and Rank:", best_rank)