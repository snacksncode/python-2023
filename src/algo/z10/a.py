s = '><><><>>><<'

# solution:
f = [0] + [c if s[c - 1] == '<' else -c for c in range(1, len(s))]

print(f)

s = 'AbBc'
print(s.lower())
