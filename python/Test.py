def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return int(sum(hand) / len(hand))


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    aprox_avg = 0
    if len(hand) % 2 == 0:
        aprox_avg = (hand[0] + hand[len(hand) - 1]) / 2
    else:
        aprox_avg = hand[(int(len(hand) / 2))]

    print(card_average(hand))
    print(aprox_avg)
    return aprox_avg == card_average(hand)

print(card_average([2, 3, 4, 8, 8]))
print(approx_average_is_average([2, 3, 4, 8, 8]))


