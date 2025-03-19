def parse_text_file(filename):
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
    added_list = []
    removed_list = []
    copyable = []
    # print("Added Cards/Modified Quantities:")
    for card_name, new_quantity in new_dict.items():
        if card_name in original_dict:
            if original_dict[card_name] != new_quantity:
                if original_dict[card_name] < new_quantity:
                    added_list.insert(0, f"{card_name}: {original_dict[card_name]} \u2192 {new_quantity}")
                else:
                    removed_list.insert(0, f"{card_name}: {original_dict[card_name]} \u2192 {new_quantity}")
                # print(f"{card_name}: {original_dict[card_name]} \u2192 {new_quantity}")
        else:
            added_list.append(f"{new_quantity}x {card_name}")
            # print(f"(New Card) {card_name}: {new_quantity}")

    # print("\nCopy-able output:")
    for card_name, new_quantity in new_dict.items():
        if card_name in original_dict:
            if original_dict[card_name] != new_quantity and new_quantity-original_dict[card_name] > 0:
                copyable.append(f"{new_quantity-original_dict[card_name]} {card_name}")
                # print(f"{new_quantity-original_dict[card_name]} {card_name}")
        else:
            copyable.append(f"{new_quantity} {card_name}")
            # print(f"{new_quantity} {card_name}")

    # print("\nRemoved Cards:")
    for card_name in original_dict:
        if card_name not in new_dict:
            removed_list.append(f"{card_name}")
            # print(f"(Removed Card) {card_name}")

    return added_list, copyable, removed_list

def parse_strings(deck_list):
    card_dict = {}
    try:
        card_list = deck_list.split("\n")
        print(len(card_list))
        for card in card_list:
            parts = card.strip().split(" ", 1)  # Split into quantity and card name
            if len(parts) == 2:
                quantity, card_name = parts
                card_dict[card_name] = int(quantity)
        return card_dict
    except:
        return "Error"