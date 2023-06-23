from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, customer_id, firstname, lastname, email_address, password, phone_number, default_address_id):
        self.id = customer_id
        self.firstname = firstname
        self.lastname = lastname
        self.email_address = email_address
        self.password = password
        self.phone_number = phone_number
        self.default_address_id = default_address_id
