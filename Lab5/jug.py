def solve_water_problem(capacity_a, capacity_b, target):
    a = 0
    b = 0

    b = capacity_b
    print(f"Fill {capacity_b}-gallon jug. Jug A: {a} gallons, Jug B: {b} gallons")

    a = min(capacity_a, a + b)
    b = max(0, b - (capacity_a - a))
    print(f"Pour water from Jug B to Jug A. Jug A: {a} gallons, Jug B: {b} gallons")

    a = 0
    print(f"Empty {capacity_a}-gallon jug. Jug A: {a} gallons, Jug B: {b} gallons")

    a = min(capacity_a, a + b)
    b = max(0, b - (capacity_a - a))
    print(f"Pour water from Jug B to Jug A. Jug A: {a} gallons, Jug B: {b} gallons")

    b = capacity_b
    print(f"Fill {capacity_b}-gallon jug. Jug A: {a} gallons, Jug B: {b} gallons")

    a = min(capacity_a, a + b)
    b = max(0, b - (capacity_a - a))
    print(f"Pour 1 gallon from Jug B to Jug A. Jug A: {a} gallons, Jug B: {b} gallons")

    print(f"Result: Jug A: {a} gallons, Jug B: {b} gallons")

solve_water_problem(3, 5, 4)
