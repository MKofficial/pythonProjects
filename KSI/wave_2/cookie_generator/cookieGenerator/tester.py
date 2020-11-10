#!/usr/bin/python3.7

from itertools import islice

from solution import primesGenerator, generatorOfGenerators, passwordGenerator, fibonacciGenerator, generatorConnector


# -------------------- TEST FUNCTIONS --------------------------

# expected result: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
def testFibonacciGenerator():
    generator = fibonacciGenerator()
    return list(islice(generator, 10))


# expected result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 7, 9]
def testGeneratorConnector():
    g1 = (x for x in range(5))
    g2 = (x for x in range(5, 10))
    g3 = (x for x in range(5, 10, 2))
    generator = generatorConnector([g1, g2, g3])
    return [x for x in generator]


# expected result: 761
def testPwdGenerator():
    generator = passwordGenerator(3)
    targetPwd = "753"
    i = 1
    for pwd in generator:
        if pwd == targetPwd:
            return i
        i += 1
    raise Exception("Password not found")


# expected result: [[1, 2, 3, 4], [2, 4], [3, 6, 9, 12, 15, 18]]
def testGeneratorOfGenerators():
    generator = generatorOfGenerators()
    g1 = next(generator)
    g2 = next(generator)
    g3 = next(generator)
    return [list(islice(g1, 4)), list(islice(g2, 2)), list(islice(g3, 6))]


# expected result: [2, 3, 5, 7, 11, 13]
def testPrimesGenerator():
    generator = primesGenerator()
    return list(islice(generator, 6))


# ---------------  END OF TEST FUNCTIONS ------------------------


def arrayEquals(a, b, compare=lambda x, y: x == y):
    try:
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not compare(a[i], b[i]):
                return False
        return True
    except:
        return False


def runTest(testFunction, testResult, testName):
    print("\n\n-------- TEST: " + testName + " --------\n")
    try:
        res = testFunction()
    except:
        print("\n\33[31mTEST FAILED WITH EXCEPTON\33[0m")
        return
    print("Result")
    print(res)
    if testResult(res):
        print("\n\33[32mTEST WAS SUCCESSFULL\33[0m")
    else:
        print("\n\33[31mTEST FAILED\33[0m")


def runAllTests():
    runTest(testFibonacciGenerator, lambda x: arrayEquals(x, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]), "Fibonacci")
    runTest(testGeneratorConnector, lambda x: arrayEquals(x, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 7, 9]), "Connector")
    runTest(testPwdGenerator, lambda x: x == 761, "Passwords")
    runTest(testGeneratorOfGenerators,
            lambda x: arrayEquals(x, [[1, 2, 3, 4], [2, 4], [3, 6, 9, 12, 15, 18]], lambda a, b: arrayEquals(a, b)),
            "Generator²")
    runTest(testPrimesGenerator, lambda x: arrayEquals(x, [2, 3, 5, 7, 11, 13]), "Prime numbers")


runAllTests()
