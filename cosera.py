import re


def f1(list_of_list):
    result = []
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in result:
                result.append(x)
    return result


def f2(list_of_list):
    flat_list = []
    for inner_list in list_of_list:
        flat_list.extend(inner_list)
    return [
        x for i, x in enumerate(flat_list)
        if flat_list.index(x) == i]


def f3(list_of_list):
    result = []
    seen = set()
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in seen:
                result.append(x)
                seen.add(x)
    return result

    """
Content of "log.txt":
10.1.2.1 - car [01/Mar/2022:13:05:05 +0900] "GET /python HTTP/1.0" 200 2222
10.1.1.9 - bike [01/Mar/2022:13:05:10 +0900] "GET /python HTTP/1.0" 200 2222

Expected output:
01/Mar/2022:13:05:05 +0900
01/Mar/2022:13:05:10 +0900
"""


def parse1():
    for line in open("log.txt"):
        print(line.split("[")[1].split("]")[0])


def parse2():
    for line in open("log.txt", "r"):
        print(line.split()[3].strip("[]"))


def parse3():
    for line in open("log.txt", "r"):
        print(" ".join(line.split("[" or "]")[3:5]))


def parse4():
    for line in open("log.txt", "rw"):
        print(" ".join(line.split()[3:5]).strip("[]"))


def parse5():
    for line in open("log.txt"):
        print(re.split("\[|\]", line)[1])


def sqsum4():
    return sum(x**2 for x in nums if x > 0)


class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year

    def __str__(self):
        return f"FunEvent(tags={self.tags}, year={self.year})"


tags = ["google", "ml"]
year = 2022
bootcamp = FunEvent(tags, year)
tags.append("bootcamp")
year = 2023
print(bootcamp)


class BaseLayer:
    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return f"{self.name}Layer"


class ActivationLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("Activation")
        self.size = size


class FCLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("FullyConnected")
        self.size = size


def tail(filename, n=10):
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines.pop(n):
        print(line)


"""
Content of "log.txt":
10.1.2.1 - car [01/Mar/2022:13:05:05 +0900] "GET /python HTTP/1.0" 200 2222
10.1.1.9 - bike [01/Mar/2022:13:05:10 +0900] "GET /python HTTP/1.0" 200 2222

Expected output:
01/Mar/2022:13:05:05 +0900
01/Mar/2022:13:05:10 +0900
"""


def parse1():
    for line in open("log.txt"):
        print(line.split("[")[1].split("]")[0])


def parse2():
    for line in open("log.txt", "r"):
        print(line.split()[3].strip("[]"))


def parse3():
    for line in open("log.txt", "r"):
        print(" ".join(line.split("[" or "]")[3:5]))


def parse4():
    for line in open("log.txt", "rw"):
        print(" ".join(line.split()[3:5]).strip("[]"))


def parse5():
    for line in open("log.txt")
            print(re.split("\[|\]", line)[1])
