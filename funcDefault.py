def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def m2toft2(area_meter2):
    area_feet2 = 10.76391 * area_meter2
    return area_feet2


print(m2toft2(4))
