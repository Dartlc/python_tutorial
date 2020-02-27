from division_task_pack.input_getting import *


def division_task(nu_r1: int, nu_r2: int, d_r1: int, d_r2: int):
    output = {i: [j for j in range(nu_r1, nu_r2) if j // i == j % i] for i in range(d_r1, d_r2)}
    print(output)


if __name__ == '__main__':
    division_task(nu_r1=get_integer_input(), nu_r2=get_integer_input(), d_r1=get_integer_input(), d_r2=get_integer_input())
