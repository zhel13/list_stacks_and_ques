number_of_lines = int(input())
result = []

dict_map = {
    "1": lambda x: result.append(x),
    "2": lambda: result.pop() if result else None,
    "3": lambda: print(max(result)) if result else None,
    "4": lambda: print(min(result)) if result else None
}

for _ in range(number_of_lines):
    query = input().split()
    dict_map[query[0]](*query[1:])

print(*result[::-1], sep=", ")