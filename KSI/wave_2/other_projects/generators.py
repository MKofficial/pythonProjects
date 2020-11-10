# Túto funkciu implementuj.
def myrange(a0, a1, limit):
    difer = a1 - a0
    current = a0
    if difer >= 0:
        while current <= limit:
            yield current
            current += difer
    else:
        while current > limit:
            yield current
            current += difer


# Pomocná funkcia, vypíše všetky hodnoty generované iterátorom.
def show(it):
    print(list(it))


# Testy:
show(myrange(0, 1, 5))  # [0, 1, 2, 3, 4]
show(myrange(1, 2, 5))  # [1, 2, 3, 4]
show(myrange(1, 3, 9))  # [1, 3, 5, 7]
show(myrange(0, 4, 15)) # [0, 4, 8, 12]
show(myrange(2, 1, -2)) # [2, 1, 0, -1]
show(myrange(0, 1, -1)) # []

