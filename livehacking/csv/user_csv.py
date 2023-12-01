import csv

def read_csv_noheader(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')

    for id, firstname, lastname, birth in rdr:
        yield {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
        }

def read_csv_header(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.DictReader(f, delimiter=';', quotechar='"')

    for row in rdr:
        id = row['ID']
        firstname = row['First name']
        lastname = row['Last name']
        birth = row['Date of Birth']

        yield {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
        }

def print_user(user):
    print(f"ID:{user['id']}, Firstname:{user['firstname']}, Lastname:{user['lastname']}, Date of birth: {user['birth']}")

