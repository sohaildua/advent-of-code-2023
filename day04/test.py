def simulate_card_game(num_cards):
    # Initialize a list to represent the number of matching numbers on each card
    matching_numbers = [4, 2, 1, 1, 0, 0]

    # Initialize a list to represent the number of copies of each card
    card_copies = [0] * num_cards
    card_copies[0] = 1  # Start with one instance of card 1

    # Simulate the card game
    for i in range(num_cards - 1):
        card_copies[i + 1] += matching_numbers[i] * card_copies[i]

        # Add the new cards only to the original card of the same type
        card_copies[i + 1] += card_copies[i]

    # Return the count for each card
    return card_copies

# Specify the number of cards in the game
num_cards = 6

# Simulate the card game
result = simulate_card_game(num_cards)

# Print the final result for each card
for i, count in enumerate(result):
    print(f"Card {i + 1}: {count} instances")

# Print the total number of scratch cards
total_scratchcards = sum(result)
print("Total number of scratch cards:", total_scratchcards)
