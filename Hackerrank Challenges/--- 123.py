
import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):
    total_cost = meal_cost + (meal_cost * (tip_percent / 100)) + (meal_cost * (tax_percent / 100))
    print(int(total_cost))




meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())

