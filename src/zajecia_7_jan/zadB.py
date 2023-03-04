from faker import Faker

# instalacja: pip install Faker
Faker.seed(111)
fake = Faker("pl_PL")


def get_imie_nazwisko(name_string: str):
    data = name_string.split(" ")
    imie = data[-2]
    nazwisko = data[-1]
    return imie, nazwisko


def generate_username(imie: str, nazwisko: str):
    return nazwisko + imie[0]


s = "Hubert Andziak".lower()
print(get_imie_nazwisko(s))
imienazwisko = get_imie_nazwisko(s)
print(generate_username(imienazwisko[0], imienazwisko[1]))


usernames = set()
N = 10**6
for i in range(N):
    name = fake.name()
    # print(f'{name:40s}', ' # ', get_imie_nazwisko(name))
    imienazwisko = get_imie_nazwisko(name)
    uname = generate_username(imienazwisko[0], imienazwisko[1])
    usernames.add(uname)

print(f"unikalnych usernames: {len(usernames)} / {N}")
