import math


def flour_cost(price, students):
    total_price = 0
    for x in range(1, students + 1):
        if x % 5 == 0:
            total_price += 0
        else:
            total_price += price
    return total_price


def egg_cost(egg_price, students):
    return students * (10 * egg_price)


def apron_cost(apron_price, students):
    return apron_price * math.ceil((students * 1.2))


def total_cost(flour, egg, apron):
    return flour + egg + apron


budget = float(input())
students = int(input())
flour_package_price = float(input())
egg_price = float(input())
apron_price = float(input())

total_product_cost = total_cost(flour_cost(flour_package_price, students), egg_cost(egg_price, students),
                                apron_cost(apron_price, students))
if total_product_cost <= budget:
    print(f"Items purchased for {total_product_cost:.2f}$.")
else:
    needed = total_product_cost - budget
    print(f"{needed:.2f}$ more needed.")
