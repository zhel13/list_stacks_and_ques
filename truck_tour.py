from collections import deque
num_petrol_pumps = int(input())

result = deque()
pump_num = 0
distance_sum = 0
stops = 0

for _ in range(num_petrol_pumps):
    petrol, distance = data = input().split()
    result.append([int(petrol), int(distance)])

while stops < num_petrol_pumps:
    fuel = 0
    for i in range(num_petrol_pumps):
        fuel += result[i][0]
        distance_sum = result[i][1]
        if fuel < distance_sum:
            result.rotate(-1)
            pump_num += 1
            stops = 0
            break
        fuel -= distance_sum
        stops += 1

print(pump_num)

