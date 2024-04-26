example = [26, 6, 90, 55]
i_pivot = len(example) - 1

while i_pivot >= 0:
    i_largest = example[i_pivot]
    print(f"i_largest 1 = {i_largest}")
    i_largest_position = 0  # Initialize with a default value
    for i, i_check in enumerate(example[1:i_pivot]):
        if i_check > i_largest:
            i_largest = i_check
            i_largest_position = i + 1
            print(f"i_largest 2 = {i_largest}")

    if i_largest > example[i_pivot - 1]:
        example[i_pivot], example[i_pivot - 1] = example[i_pivot - 1], example[i_pivot]
    elif i_largest_position != 0:  # Check if i_largest_position is assigned
        example[i_largest_position], example[i_pivot - 1] = example[i_pivot - 1], example[i_largest_position]
    print(f"i_largest 3 = {i_largest}")
    i_pivot = i_pivot - 1

print(f"{example}")
