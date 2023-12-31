num_rounds = 100
num_cats = 100
cats_with_hats = [0] * num_cats

for round_num in range(1, num_rounds + 1): #O(n)
    for cat_position in range(round_num, num_cats, round_num): #O(n)
        cats_with_hats[cat_position] = 1 - cats_with_hats[cat_position]

final_cats_with_hats = [index + 1 for index, hat_status in enumerate(cats_with_hats) if hat_status == 1]

print(f"Cats with hats at the end: {final_cats_with_hats}")