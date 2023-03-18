import matplotlib.pyplot as plt

dane = [
    5, 0.7,
    10, 0.75,
    100, 2.4,
    200, 4.9,
    400, 11,
    800, 29,
    1600, 86,
    3200, 224,
    6400, 497,
    12800, 1092,
    12800 * 2, 2515,
    12800 * 4, 5479
]

# zadanie -- wszystkie elementy na parzystych elementach --> do listy "x", pozostae do listy "y"

x, y = dane[::2], dane[1::2]

# plt.plot(x,y)

y_ratios = [y2/y1 for (y1,y2) in zip(y[:-1], y[1:])]
x_ratios = x[1:]

plt.plot(x_ratios,y_ratios)
plt.xlabel("Rozmiar danych")
plt.ylabel("Czas wykonania (usec)")
plt.show()