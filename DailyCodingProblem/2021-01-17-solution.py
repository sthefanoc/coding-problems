
# 2D table o currencies
# For each currency on x, we have a price on y
# Starting with amount of money A, is it possible to make trades and get more than A?


# Mock currency table, with X, Y, Z
# Mock values: X = 12, Y = 6, Z = 3

currency_exchange_rates = [
    [1.0, 2.0, 4.0],  # X line
    [0.5, 1.0, 2.0],  # Y line
    [0.25, 0.5, 1.0],  # Z line
]

# Check if the values are equivalent on different lines

# Equivalent values on a matrix 3x3:
# 0x1 -> 1x0
# 0x2 -> 2x0
# 1x0 -> 0x1
# 1x2 -> 2x1

# N x N => 0 x n, 0+1 x n-1, ... , n x 0

# For better efficiency, stop when parity has already been checked (0xn == nx0)


def possible_arbitrage(currency_exchange_rates):
    ref = len(currency_exchange_rates) - 1
    for index in range(len(currency_exchange_rates)):
        print(index, ref)
        ref -= 1


possible_arbitrage(currency_exchange_rates)
