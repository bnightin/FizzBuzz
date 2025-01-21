import pytest
from FizzBuzz.fizzbuzz import FizzBuzz

# Tests

def test_fizzbuzz_divisible_by_3_and_5():
    assert FizzBuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]

def test_fizzbuzz_empty():
    assert FizzBuzz(0) == []

def test_fizzbuzz_only_fizz():
    assert FizzBuzz(3) == ["1", "2", "Fizz"]

def test_fizzbuzz_only_buzz():
    assert FizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

def test_fizzbuzz_no_fizzbuzz():
    assert FizzBuzz(2) == ["1", "2"]

if __name__ == "__main__":
    pytest.main()
