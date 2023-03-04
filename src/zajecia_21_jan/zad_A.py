from faker import Faker

Faker.seed(111)
fake = Faker("pl_PL")

unique_last_names = set([fake.last_name().lower() for _ in range(10**5)])

name_frequency = dict()  # name -> n_of_occurrences


letter_2_names = dict()

for name in unique_last_names:
    if name[:2] not in letter_2_names:
        letter_2_names[name[:2]] = []
    letter_2_names[name[:2]].append(name)

for names in letter_2_names.values():
    names.sort()


def get_name_autocompletion(prefix: str) -> list[str]:
    candidates = [
        name for name in letter_2_names[prefix[:2]] if name.startswith(prefix)
    ]  # comprehension
    return candidates


print(get_name_autocompletion("xi"))
