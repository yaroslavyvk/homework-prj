import random

letters = [chr(ord('A') + i) for i in range(26)]
file_data = {}
for letter in letters:
    file_name = f'{letter}.txt'
    with open(file_name, 'w') as file:
        random_num = random.randint(1,100)
        file.write(f'{random_num}')
        file_data[file_name] = random_num

with open("summary.txt", "w") as summary_file:
    for filename, random_number in file_data.items():
        summary_file.write(f"{filename}: {random_number}\n")