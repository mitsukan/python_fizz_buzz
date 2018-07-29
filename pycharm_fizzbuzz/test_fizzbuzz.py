from fizzbuzz import fizzbuzz

def test_fizz_divisible_by_3():
    assert fizzbuzz(3) == "fizz"

def test_buzz_divisible_by_5():
    assert fizzbuzz(5) == "buzz"