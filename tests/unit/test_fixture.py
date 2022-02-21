""" Test pytest fixtures """


def test_random_number(random_num):
    """
    Given: A ranndom number fixture as input
    When: A random number is generated
    Then: make sure it is with a range of integers between 0..9
    """
    assert random_num in range(10)
