def sum_of_integers(file_name):
    with open(file_name, "r") as file:
        rows = file.read().splitlines()

    total_sum = 0
    for r in rows:
        data = r.split(",")
        for d in data:
            try:
                num = int(d)
                total_sum += num
            except ValueError as e:
                continue
    return total_sum

file_name = "numbers.txt"

print(
    "The sum of numbers in {} is {}".format(
        file_name, sum_of_integers(file_name)
    )
)
