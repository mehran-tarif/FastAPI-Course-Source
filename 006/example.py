def person(name, age, city):
    print({
        "name": name,
        "age": age,
        "city": city
    })

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

person(
    name=data["name"],
    age=data["age"],
    city=data["city"]
)

person(**data)