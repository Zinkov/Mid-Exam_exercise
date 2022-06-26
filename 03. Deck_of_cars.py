
def indexExists(list, index):
    if 0 <= int(index) < len(list):
        return True
    else:
        return False


def operation(cards, loops):
    deck = [card for card in cards]

    for command in range(loops):
        command = input().split(", ")
        if command[0] == "Add":
            if command[1] in deck:
                print("Card is already in the deck")
            else:
                deck.append(command[1])
                print("Card successfully added")

        elif command[0] == "Remove":
            if command[1] in deck:
                deck.remove(command[1])
                print("Card successfully removed")
            else:
                print("Card not found")

        elif command[0] == "Remove At":
            if indexExists(deck, command[1]):
                deck.pop(int(command[1]))
                print("Card successfully removed")
            else:
                print("Index out of range")

        elif command[0] == "Insert":
            if command[2] in deck:
                print("Card is already in the deck")
            elif indexExists(deck, command[1]):
                deck.insert(int(command[1]), command[2])
                print("Card successfully added")
            else:
                print("Index out of range")
    print('%s' % ', '.join(map(str, deck)))


cards = list(card for card in input().split(", "))
loops = int(input())

operation(cards, loops)
