"""

Missed the round() part, had to look up the answer.. Pay attention!

"""
# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):
    total_cost = meal_cost + (meal_cost * (tip_percent / 100)) + (meal_cost * (tax_percent / 100))
    print(int(round(total_cost)))


if __name__ == '__main__':

    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
