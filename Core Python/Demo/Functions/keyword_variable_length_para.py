def emp(**data):
    for key, val in data.items():
        print(key, ":", val)

emp(id=101, name="Akshay", age=47, salary = 34000)