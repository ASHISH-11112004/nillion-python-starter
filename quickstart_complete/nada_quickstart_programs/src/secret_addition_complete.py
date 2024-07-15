from nada_dsl import *

def nada_main():

    # Define the parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Input secret integers for Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Input secret integers for Party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))

    # Perform operations
    sum_int = my_int1 + my_int2
    product_int = sum_int * my_int3
    final_int = product_int - my_int2

    # Return the outputs
    return [
        Output(sum_int, "sum_output", party1),
        Output(product_int, "product_output", party2),
        Output(final_int, "final_output", party1)
    ]
