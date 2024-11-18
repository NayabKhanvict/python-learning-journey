dict = {
    "name": "Talha",
    "age": 12
}

print(dict['name'])

marks = {}
mark1 = int(input("Enter first mark: "))
marks.update({"key1":mark1})

mark2 = int(input("Enter tow mark: "))
marks.update({"key2":mark2})

mark3 = int(input("Enter third mark: "))
marks.update({'key3':mark3})

print(marks)