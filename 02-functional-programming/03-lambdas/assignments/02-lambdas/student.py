class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


def group_by(xs, key_function):
    result = {}
    for x in xs:
        key = key_function(x)
        if key not in result:
            result[key] = []
        result[key].append(x)
    return result


def partition(xs, condition):
    true_list = []
    false_list = []

    for x in xs:
        if condition(x):
            true_list.append(x)
        else:
            false_list.append(x)

    return (true_list, false_list)


def group_by_suit(cards):
    return group_by(cards, lambda card: card.suit)

def group_by_value(cards):
    return group_by(cards, lambda card:card.value)

def partition_by_color(cards):
    return partition(cards,lambda card : card.suit == "spades" or card.suit == "clubs")
    