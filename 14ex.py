class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite
        dict = {"id": self.current_id,
                "name": self.name,
                "phone": self.phone,
                "email": self.email,
                "favorite": self.favorite}
        self.contacts.append(dict)
        Contacts.current_id += 1