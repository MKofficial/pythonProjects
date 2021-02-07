from typing import List, Tuple

ORIGINYEAR = 1980  # the begin year
MAXYEAR = (ORIGINYEAR + 100)  # the maximum year

monthtable: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthtable_leap: List[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def IsLeapYear(Year: int) -> int:
    """
    Function: IsLeapYear

    Local helper function checks if the year is a leap year

    Parameters:

    Returns:
    """
    leap: int = 0
    if (Year % 4) == 0:
        leap = 1
        if (Year % 100) == 0:
            leap = 0 if (Year % 400) else 1
    return leap


def ConvertDays(days: int) -> Tuple[int, int, int]:
    """
    Function: ConvertDays

    Local helper function that split total days since Jan 1, ORIGINYEAR into
    year, month and day

    Parameters:

    Returns:
    """
    year = ORIGINYEAR
    while days > 365:
        if IsLeapYear(year):
            if days > 366:
                days -= 366;
                year += 1
        else:
            days -= 365
            year += 1

    # Determine whether it is a leap year
    month_tab: List[int] = (monthtable_leap if (IsLeapYear(year)) else monthtable)

    for month in range(12):
        if days <= month_tab[month]:
            break
        days -= month_tab[month]

    month += 1

    return year, month, days


def test_ConvertDays():
    assert ConvertDays(1) == (1980, 1, 1)


if __name__ == '__main__':
    for i in range(1, 3681):
        print(ConvertDays(i))
