import pytest


from hamming import distance


def test_distance_returns_zero_with_two_empty_strings():
    assert distance('', '') == 0

def test_distance_raises_exception_without_strings():
    with pytest.raises(Exception):
        distance()

def test_distance_raises_exception_with_one_string():
    with pytest.raises(Exception):
        distance('')

def test_distance_raises_exception_with_more_than_two_strings():
    with pytest.raises(Exception):
        distance('', '', '')

def test_distance_raises_exception_when_left_string_shorter_than_right():
    with pytest.raises(Exception):
        distance('', 'str')


def test_distance_raises_exception_when_right_string_shorter_than_left():
    with pytest.raises(Exception):
        distance('str', '')


def test_distance_raises_exception_when_right_non_empty_string_shorter_than_left():
    with pytest.raises(Exception):
        distance('str', 'st')


def test_distance_raises_exception_when_left_non_empty_string_shorter_than_right():
    with pytest.raises(Exception):
        distance('st', 'str')


def test_distance_returns_zero_with_one_empty_and_one_space_string():
    assert distance('', '          ') == 0


def test_distance_returns_zero_with_one_non_empty_and_one_space_string():
    assert distance('ab', '  ab') == 0


def test_distance_with_distance_two():
    assert distance('abc', 'aeo') == 2
    