import Dict.phone_contacts.functions as f


print(f.add_contact(1, "arsham", 12345))
print(f.add_contact(2, "arsham", 12345))



print(f.contacts)


print(f.remove_contact(1))
print(f.remove_contact(4))

print(f.contacts)

print(f.edit_contact(2,"armita",4567))

print(f.contacts)


f.show_contacts()