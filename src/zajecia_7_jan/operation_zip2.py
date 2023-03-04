def foo(x):
    return x**2, x**3


t = foo(3)
print(t)
print(type(t))

names = ["John", "William", "Larry", "Bill", "Xiao"]
scores = [10, 5, 2, 200]

messages = []
for i in range(len(names)):
    name = names[i]
    score = scores[i]
    message = f"{name}'s score is {score}"
    messages.append(message)
    print(message)

print("-" * 30)

for name, score in zip(names, scores):
    message = f"{name}'s score is {score}"
    print(message)
