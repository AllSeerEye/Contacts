import sys
from tinydb import TinyDB, Query

def main():
    usage_str = """
Usage: 
    python3 contacts.py list -> lists all contacts stored in database
    python3 contacts.py add "New Contact Name" "New Contact Number" -> adds a new contact
    python3 contacts.py remove "Contact Name" -> removes an existing contact
    python3 contacts.py show "Contact Name" -> shows a contact's name and number
"""

    db = TinyDB("db.json")
    User = Query()
    
    if len(sys.argv) == 4:
        command = sys.argv[1]
        name = sys.argv[2]
        number = sys.argv[3]
        if command == "add":
            if not db.search(User.name == name):
                db.insert({"name": name, "number": number})
            else:
                print("Contact already exists")
        else:
            print(usage_str)
    elif len(sys.argv) == 3:
        command = sys.argv[1]
        name = sys.argv[2]
        if command == "show":
            if db.search(User.name == name):
                print(db.search(User.name == name)[0]["name"])
                print(db.search(User.name == name)[0]["number"])
            else:
                print("Contact does not exist")
        elif command == "remove":
            if db.search(User.name == name):
                db.remove(User.name == name)
            else:
                print("Contact does not exist")
        else:
            print(usage_str)
    elif len(sys.argv) == 2:
        command = sys.argv[1]
        if command == "list":
            for item in db:
                print(item)
        else:
            print(usage_str)
    else:
        print(usage_str)

if __name__ == "__main__":
    main()
