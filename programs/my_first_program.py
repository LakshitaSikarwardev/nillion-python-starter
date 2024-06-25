from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the area of the rectangle
    area = my_int1 * my_int2

    # Return the area as an output
    return [Output(area, "my_output", party1)]
