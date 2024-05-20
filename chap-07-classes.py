from person_class import Person

print("Welcome to creating Person instances!")

person = Person(1, "Marty", "McFly", "marty@b2f.com", "286-934-3344")
print("Person info:")
print(f"id:     {person.id}")
print(f"name:   {person.first_name} {person.last_name}")
print(f"email:  {person.email}")
print(f"phone:  {person.phone}")
person.phone = "222-333-4444"
print(f"id:     {person.phone}")
print(f"get_person_details(): {person.get_person_details()}")


print("bye")