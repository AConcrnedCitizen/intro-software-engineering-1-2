initial = int(input("Starting number of organisms: "))
rate = int(input("Average daily increase (%): "))
days = int(input("Number of days to multiply: "))


def advance(previous):
    return previous + (previous * (rate / 100))

current = initial
for i in range(days):
    if i == 0:
        print(f"Day {i+1}: {current}")
        continue
    current = advance(current)
    print(f"Day {i+1}: {current}")
