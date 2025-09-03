print("welcome to the Life Calculator, if you live to 90 years old.")
age = input("what is your current age? ")
age_as_int = int(age)

years_remaining = 90 - age_as_int

days_remaining = years_remaining * 365

weeks_remaining = years_remaining * 52

months_remaining = years_remaining * 12

message = f"you have {days_remaining} days, {weeks_remaining} weeks or {months_remaining} months left remaining."

print(message)