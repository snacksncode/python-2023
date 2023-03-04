def is_mixed_case(s: str) -> bool:
    only_upper = s.upper() == s
    only_lower = s.lower() == s
    return (not only_lower) and (not only_upper)


print(is_mixed_case("abc"))
print(is_mixed_case("aBc"))
print(is_mixed_case("AbC"))
print(is_mixed_case("a"))
print(is_mixed_case("ABC"))
