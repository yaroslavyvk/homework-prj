content_text = (
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, \n'
    'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n'
    'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n'
    'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\n'
    'reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \n'
    'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt\n'
    'mollit anim id est laborum.\n'
)

with open('file1.txt', 'w') as file1:
    file1.write(content_text)

with open('file1.txt', 'r') as file1, open('file2.txt','w') as file2:
    content_file1_upper = file1.read().upper()
    file2.write(content_file1_upper)