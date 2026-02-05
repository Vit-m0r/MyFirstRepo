EXPECTED_BAKE_TIME = 40  # минут
PREPARATION_TIME = 2     # минуты на слой

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining baking time.

    :param elapsed_bake_time: int - minutes the lasagna has been in the oven.
    :return: int - minutes remaining based on EXPECTED_BAKE_TIME.

    This function takes the time already spent baking and returns
    how many minutes are left until the lasagna is fully cooked.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for the lasagna.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - total preparation time (in minutes).

    This function multiplies the number of layers by the constant
    PREPARATION_TIME to determine the total preparation time.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
