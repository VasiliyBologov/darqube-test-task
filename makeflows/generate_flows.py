import random
import string


# TODO: need add tests
def generate_flows():
    return [generate_names() for i in range(1000)]


# TODO: need add tests
def generate_names():
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(5))
    return rand_string

if __name__ == '__main__':
    print(generate_flows())
