#TASK 1

square = lambda x: x * x

print(square(5))



#TASK 2


reverse = lambda x: x[::-1]

print(reverse("python"))

length = lambda x: len(x)

print(length("python"))



#TASK 3


students = [
    ("Arun", 85),
    ("Priya", 45),
    ("Rahul", 72),
    ("Divya", 38),
    ("Karthik", 90)
]

passed = list(filter(lambda x: x[1] >= 50, students))

print(passed)


# TASK 4

Students = {
    "Arun": 85,
    "Priya": 70,
    "Rahul": 90,
    "Divya": 65
}

values = lambda x: x.values()

print(list(values(Students)))














