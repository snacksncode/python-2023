from faker import Faker

Faker.seed(111)

fake = Faker("pl_PL")
# fake = Faker()
for i in range(3):
    print(fake.name())
    print(fake.address())
    print(fake.administrative_unit())
    print(fake.ssn())
    print(fake.vat_id())
    print("-" * 30)
