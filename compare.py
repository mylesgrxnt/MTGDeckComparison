def parse_card_list(filename):
    card_dict = {}  # Dictionary to store card names and quantities
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" ", 1)  # Split into quantity and card name
            if len(parts) == 2:
                quantity, card_name = parts
                card_dict[card_name] = int(quantity)  # Convert quantity to integer
    return card_dict

def compare_card_dictionaries(original_dict, new_dict):
    # Check for changes and new cards
    print("Added Cards/Modified Quantities:")
    for card_name, new_quantity in new_dict.items():
        if card_name in original_dict:
            if original_dict[card_name] != new_quantity:
                print(f"{card_name}: {original_dict[card_name]} → {new_quantity}")
        else:
            print(f"(New Card) {card_name}: {new_quantity}")
    print("\nCopy-able output:")
    for card_name, new_quantity in new_dict.items():
        if card_name in original_dict:
            if original_dict[card_name] != new_quantity and new_quantity-original_dict[card_name] > 0:
                print(f"{new_quantity-original_dict[card_name]} {card_name}")
        else:
            print(f"{new_quantity} {card_name}")

    print("\nRemoved Cards:")
    # Check for removed cards
    for card_name in original_dict:
        if card_name not in new_dict:
            print(f"(Removed Card) {card_name}")

# Example usage
new_dict = parse_card_list("new.txt")
original_dict = parse_card_list("original.txt")

print("Cards to Add:")
compare_card_dictionaries(original_dict, new_dict)