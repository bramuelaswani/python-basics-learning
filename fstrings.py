import datetime
Home = "Mexico City"
print(f"My home is {Home}")


python_birthday = datetime.datetime(year=1991, month=2, day=20)
print(
    f"Python first appeared on {python_birthday:%B %d} in the year {python_birthday:%Y}."
)

now = datetime.datetime.now()
print(f"Python is {now.year - python_birthday.year} years old.")


# import datetime
# mexico_founding = datetime.datetime(year=1325, month=3, day=13)
# now = datetime.datetime.now()

# f"Mexico-Tenochtitlan was established {mexico_founding - now} years ago."
