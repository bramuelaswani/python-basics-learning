import json

# python object(dictionary) to be dumped
dict1 = {
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
                "age": "34",
                "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
                "age": "24",
                "salary": "40000"
    },
}

# the json file where the output must be stored
out_file = open("myfile.json", "w")

json.dump(dict1, out_file, indent=6)

out_file.close()


# import module

# Data to be written
data = {
    "user": {
        "name": "satyam kumar",
        "age": 21,
                "Place": "Patna",
                "Blood group": "O+"
    }
}

# Serializing json and
# Writing json file
with open("datafile.json", "w") as write:
    json.dump(data, write)
# Python program showing
# use of json package


# {key:value mapping}
a = {"name": "John",
     "age": 31,
     "Salary": 25000}

# conversion to JSON done by dumps() function
b = json.dumps(a)

# printing the output
print(b)
user_data = {
    'user': {
        'name': 'g',
        'age': 5,
        'borm': 'kenya'
    }
}
print(json.dumps(user_data))
