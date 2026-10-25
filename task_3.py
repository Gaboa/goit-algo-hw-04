import random
import timeit


def insertion_sort(values):
	result = values.copy()
	for index in range(1, len(result)):
		current = result[index]
		position = index - 1
		while position >= 0 and result[position] > current:
			result[position + 1] = result[position]
			position -= 1
		result[position + 1] = current
	return result


def merge_sort(values):
	if len(values) < 2:
		return values

	middle = len(values) // 2
	left = merge_sort(values[:middle])
	right = merge_sort(values[middle:])
	merged = []
	left_index = 0
	right_index = 0

	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			merged.append(left[left_index])
			left_index += 1
		else:
			merged.append(right[right_index])
			right_index += 1

	merged.extend(left[left_index:])
	merged.extend(right[right_index:])
	return merged


def timsort_sorted(values):
	return sorted(values)


ALGORITHMS = (
	("Insert", insertion_sort),
	("Merge", merge_sort),
	("sorted()", timsort_sorted),
)
SIZES = (100, 1_000, 5_000, 20_000)

def make_datasets(size):
	generator = random.Random(size)
	random_values = [generator.randrange(size * 10) for _ in range(size)]
	ordered = sorted(random_values)

	return {
		"Random": random_values,
		"Ordered": ordered,
		"Reversed": ordered[::-1],
	}


def measure(algorithm, values):
	timer = timeit.Timer(lambda: algorithm(values))
	return timer.timeit(number=1)


def main():
	for dataset_name in ("Random", "Ordered", "Reversed"):
		print(f"\n{dataset_name}")
		print(f"{'Size':>8}  {'Insert':>12}  {'Merge':>12}  {'sorted()':>12}")

		for size in SIZES:
			values = make_datasets(size)[dataset_name]
			results = []
			for name, algorithm in ALGORITHMS:
				results.append(f"{measure(algorithm, values):.6f}")

			print(f"{size:>8}  " + "  ".join(f"{result:>12}" for result in results))


if __name__ == "__main__":
	main()