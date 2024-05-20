from dataclasses import dataclass

@dataclass
class Person:
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str

    def get_person_details(self):
        details = f"id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, "
        details += f"email: {self.email}, phone: {self.phone}"
        return details