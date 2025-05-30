import pytest
import random
from car import Car


@pytest.fixture
def car():
    return Car()


def test_initial_speed(car):
    assert car.speed == 0


def test_initial_odometer(car):
    assert car.odometer == 0


def test_initial_time(car):
    assert car.time == 0


# Tests for changing speed
def test_change_speed(car):
    car.change_speed(1)
    assert car.speed == 1


def test_multiple_speed_change(car):
    total_change = 0
    random.seed(42)
    for _ in range(3):
        change = random.randint(0, 10)
        total_change += change
        car.change_speed(change)
    assert car.speed == total_change


# Tests for getting current speed
def test_get_current_speed_from_start(car):
    assert car.get_current_speed() == 0


def test_get_current_speed_after_change(car):
    car.change_speed(27)
    assert car.get_current_speed() == 27

def test_average_speed_div(car):
    car.time = 0
    assert car.average_speed == "Divide by 0! Car did not move!"
    

def test_average_speed_aver(car):
    car.time = 10
    car.change_speed(27)
    assert car.average_speed == 2.7