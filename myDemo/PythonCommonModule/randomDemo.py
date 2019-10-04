import random


def v_code():
    code = ""
    for i in range(4):
        num = random.randint(0, 9)
        A1Z1 = chr(random.randint(65, 90))
        a1z1 = chr(random.randint(97, 122))
        add = random.choice([num, A1Z1, a1z1])
        code = "".join([code, str(add)])
    return code


print(v_code())
