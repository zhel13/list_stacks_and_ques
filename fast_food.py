from collections import deque


def orders(qty, ordr):
    current_order = 0
    while ordr:

        result = ordr.popleft()
        current_order += result
        if current_order > qty:
            ordr.appendleft(result)
            print(f"Orders left: {' '.join(str(x) for x in ordr)}")
            return

    print("Orders complete")


food_qty = int(input())
orders_data = deque([int(x) for x in input().split()])
print(max(orders_data))
orders(food_qty, orders_data)
#
#
#
# while orders:
#     if served_orders <= food_qty:
#         current_order = orders.popleft()
#     if served_orders + current_order > food_qty:
#         orders.appendleft(current_order)
#         break
#     else:
#         served_orders += current_order
#
# if orders:
#     print(f"Orders left: {' '. join(str(x) for x in orders)}")
# else:
#     print("Orders complete")