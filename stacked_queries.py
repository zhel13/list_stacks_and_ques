number_of_lines = int(input())
result = []

for i in range(number_of_lines):
    query = input().split()
    command = query[0]

    if command == "1":
        result.append(int(query[1]))
    if result:
        if command == "2":
            result.pop()
        elif command == "3":
            print(max(result))
        elif command == "4":
            print(min(result))

print(*result[::-1], sep=", ")



