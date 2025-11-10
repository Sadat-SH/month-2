class Contact:
    def __init__(self, name, phone_number, contact_id=None):
        self.name = name
        self.phone_number = phone_number
        self.id = contact_id  

    @staticmethod
    def validate_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []  
    last_id = 0    

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            cls.last_id += 1
            new_contact = Contact(name, phone_number, cls.last_id)
            cls.all_contacts.append(new_contact)
            print(f"Контакт '{name}' успешно добавлен.")
        else:
            raise ValueError("Ошибка: номер телефона должен содержать ровно 10 цифр!")

    @classmethod
    def remove_contact(cls, contact_id):
        for contact in cls.all_contacts:
            if contact.id == contact_id:
                cls.all_contacts.remove(contact)
                print(f"Контакт с id={contact_id} удалён.")
                return
        print(f"Контакт с id={contact_id} не найден.")


print(ContactList.all_contacts)  # []

ContactList.add_contact("Алия Сартова", "0700100200")
ContactList.add_contact("Бектур Асанов", "0500123456")

print("\nВсе контакты:")
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, contact.id)

try:
    ContactList.add_contact("Ton Holand", "5551234")
except ValueError as e:
    print(e)

print("\nУдаление контакта с id=1:")
ContactList.remove_contact(1)

print("\nПосле удаления:")
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, contact.id)

print("\nПоследний ID:", ContactList.last_id)
