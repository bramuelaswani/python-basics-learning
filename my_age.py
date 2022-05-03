import datetime

my_birthday = datetime.datetime(year=1996, month=6, day=22)
print(
    f"I was born {my_birthday:%B %d} in the year {my_birthday:%Y}."
)

now = datetime.datetime.now()
print(f"my age is {now.year - my_birthday.year} years old.")
