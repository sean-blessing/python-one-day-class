from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str
    last_name: str
    email: str
    phone: str
    
    def display_contact(self):
        contact_info = "---------------------------------------\n"
        contact_info +="---- Current Contact ------------------\n"
        contact_info +="---------------------------------------\n"
        contact_info +=f"Name:           {self.first_name} {self.last_name}\n"
        contact_info +=f"Email Address:  {self.email}\n"
        contact_info +=f"Phone Number:   {self.phone}\n"
        contact_info +="---------------------------------------\n"
        return contact_info
        
