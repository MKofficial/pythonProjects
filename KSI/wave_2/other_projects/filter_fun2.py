# TODO: Tyto funkce implementuj
# Bude pote volana filter(first_wolf_test, vstupni_data)
from typing import List, Iterator


def first_wolf_test(angle: int) -> bool:
    return angle < 135


# TODO: Implementuj tuto lambda funkci
# Bude pote volana filter(second_wolf_test, vstupni_data)
second_wolf_test = lambda x: x % 4 == 0 and x % 5 == 0


# TODO: Implementuj tuto funkci
# Tato funkce bere seznam a vraci filtrovaný seznam
def third_wolf_test(animals: List[str]) -> Iterator:
    return filter(lambda x: x.lower().startswith("vlk"), animals)


# Nasleduji automaticke testy a ukazka dat
def test_sample_success_rate(function, animals, wolfs, already_filtered=False):
    correct = []
    misidentified = []

    iterator = filter(
        function,
        animals) if not already_filtered else function(animals)

    for possible_wolf in iterator:
        if possible_wolf in wolfs:
            correct.append(possible_wolf)
        else:
            misidentified.append(possible_wolf)

    if len(correct) == len(wolfs) and not misidentified:
        print('Hooray! You managed to capture all hidden wolves!')
        return True

    missed = [wolf for wolf in wolfs if wolf not in correct]
    success_rate = int(100 * (len(correct) - len(misidentified)) / len(wolfs))
    print("You managed to correctly identify %d%% of wolves" % success_rate)
    print("Correct:", correct)
    print("Missed:", missed)
    print("Misidentified:", misidentified)
    return False


if __name__ == '__main__':
    # Namerena data
    print("Test #1")
    test_sample_success_rate(first_wolf_test, [120, 150, 134, 80, 0, 170, 2, 3, 65, 180], {0, 65, 2, 3, 134, 80, 120})

    print("Test #2")
    test_sample_success_rate(second_wolf_test, [128, 192, 70, 200, 40, 840, 1060, 8, 170, 10, 142, 144, 86, 54, 152],
                             {200, 40, 840, 1060})

    print("Test #3")
    test_sample_success_rate(third_wolf_test,
                             ['Vlkoun Obecný',
                              'Pes Domácí',
                              'VLK Velký',
                              'Haryk Haryk',
                              'VlK',
                              'Rex-T',
                              'Stegosaurus Pes'],
                             {'Vlkoun Obecný', 'VLK Velký', 'VlK'}, already_filtered=True)