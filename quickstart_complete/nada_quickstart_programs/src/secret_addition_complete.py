from nada_dsl import *

def nada_main():

    # Define the party involved
    party1 = Party(name="Party1")

    # Input secret integers for Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform a simple operation
    new_int = my_int1 * my_int2

    # Return the output
    return [Output(new_int, "my_output", party1)]
