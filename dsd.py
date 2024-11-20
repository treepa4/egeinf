n = int(input())
lost_items = {}

for _ in range(n):
    day, description = input().split("-")
    lost_items[description.strip()] = int(day)

k = int(input())
storage_items = {}

for _ in range(k):
    day, description = input().split("-")
    storage_items[description.strip()] = int(day)

count = 0

for item, day_lost in lost_items.items():
    if item in storage_items and storage_items[item] > day_lost:
        count += 1

print(count)