from faker import Faker

# Klasa bazowa dla informacji kontaktowych
class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

# Klasa rozszerzona dla informacji kontaktowych związanych z pracą
class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone_number, email, job_title, company_name, work_phone_number):
        super().__init__(first_name, last_name, phone_number, email)
        self.job_title = job_title
        self.company_name = company_name
        self.work_phone_number = work_phone_number

    def contact(self):
        print(f"Wybieram numer {self.work_phone_number} i dzwonię do {self.first_name} {self.last_name}")

# Funkcja do tworzenia losowych wizytówek za pomocą biblioteki Faker
def create_contacts(contact_type, quantity):
    fake = Faker()
    contacts = []
    
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = fake.phone_number()
        email = fake.email()
        
        if contact_type == 'base':
            contacts.append(BaseContact(first_name, last_name, phone_number, email))
        elif contact_type == 'business':
            job_title = fake.job()
            company_name = fake.company()
            work_phone_number = fake.phone_number()
            contacts.append(BusinessContact(first_name, last_name, phone_number, email, job_title, company_name, work_phone_number))
    
    return contacts

# Przykład użycia:
base_contacts = create_contacts('base', 3)
business_contacts = create_contacts('business', 3)

for contact in base_contacts:
    contact.contact()
    print(f"Label length: {contact.label_length}")

for contact in business_contacts:
    contact.contact()
    print(f"Label length: {contact.label_length}")
