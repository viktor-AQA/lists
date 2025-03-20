def generate_squares(n):
    results = list()
    i = 1
    while i <= n:
        results.append(i ** 2)
        i += 1
        print(results)

generate_squares(5)