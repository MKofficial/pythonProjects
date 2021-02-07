# nejdrive si importujeme dekorator given
# a take vsechny strategie
import hypothesis.strategies as st
from hypothesis import given


# Toto je nase funkce, kterou chceme testovat
def get_last_digit_my(number: int) -> str:
    return str(number % 10)


# Toto je urcite fungujici funkce, se kterou budeme porovnavat
def get_last_digit_correct(number: int) -> str:
    return str(number)[-1:]


# Rekneme Hypothesis, ze chceme teto funkci predavat jako parametr cisla (tzn. chceme pouzit strategii integers)
@given(st.integers())
def test_get_last_digit(number: int):
    # print(number)  # odkumentuj toto, pokud chces videt, ktera cisla Hypothesis zkousi
    my_result = get_last_digit_my(number)
    correct_result = get_last_digit_correct(number)

    # porovname vysledky pomoci assert
    # pokud se rovnaji, nase funkce funguje a nic se nestane
    # pokud se nerovnani, vznikne vyjimka a hypothesis nam pote vypise, na cem funkce selhala
    assert my_result == correct_result


# funkci nam staci zavolat pouze jednou, Hypothesis ji pote bude volat opakovane s ruznymi vstupy
test_get_last_digit()
