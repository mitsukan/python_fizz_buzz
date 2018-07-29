from fizzbuzz import fizzbuzz

def test_fizz_divisible_by_3():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(6) == "fizz"

def test_buzz_divisible_by_5():
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(10) == "buzz"

def test_fizzbuzz_divisible_by_15():
    assert fizzbuzz(15) == "fizzbuzz"

def test_return_x_if_divisible_by_nothing():
    assert fizzbuzz(2) == 2