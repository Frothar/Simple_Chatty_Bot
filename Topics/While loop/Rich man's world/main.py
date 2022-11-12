deposit = float(input())
number_of_years = 0
max_deposit = 700_000
interest_rate = 1.071

while deposit < max_deposit:
    deposit *= interest_rate
    number_of_years += 1
print(number_of_years)
