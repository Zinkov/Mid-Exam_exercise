import math


def family_calc(years, km):
    init_tax = 50
    km_decline = math.floor(int(km) / 3000)
    init_tax += km_decline * 12
    for y in range(int(years)):
        init_tax -= 5
    return init_tax


def heavy_calc(years, km):
    init_tax = 80
    km_decline = math.floor(int(km) / 9000)
    init_tax += km_decline * 14
    for y in range(int(years)):
        init_tax -= 8
    return init_tax


def sports_calc(years, km):
    init_tax = 100
    km_decline = math.floor(int(km) / 2000)
    init_tax += km_decline * 18
    for y in range(int(years)):
        init_tax -= 9

    return init_tax


def tax_calc(cars):
    tax_collected = 0
    # cars = []
    for vehicle in cars:
        car = vehicle.split(" ")
        if car[0] == "family":
            tax = family_calc(car[1], car[2])
            print(f"A {car[0]} car will pay {tax:.2f} euros in taxes.")
            tax_collected += tax
        elif car[0] == "heavyDuty":
            tax = heavy_calc(car[1], car[2])
            print(f"A {car[0]} car will pay {tax:.2f} euros in taxes.")
            tax_collected += tax
        elif car[0] == "sports":
            tax = sports_calc(car[1], car[2])
            print(f"A {car[0]} car will pay {tax:.2f} euros in taxes.")
            tax_collected += tax
        else:
            print("Invalid car type.")
    print(f"The National Revenue Agency will collect {tax_collected:.2f} euros in taxes.")


cars = list(car for car in input().split(">>"))
tax_calc(cars)
