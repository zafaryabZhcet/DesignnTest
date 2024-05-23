import os
num_copies = 1

path = 'D:/Github/DesignnTest/src/client0.py'

# Read the content of the original client0 file
with open(path, 'r') as file:
    content = file.read()

# Loop to create copies and modify the client_name variable
for i in range(10,num_copies + 10):
    new_client_name = f"client{i}"
    new_content = content.replace('client0', new_client_name)
    print(f'new client: {new_client_name}')
    
    # Write the new content to the new file
    with open(f"D:/Github/DesignnTest/src/{new_client_name}.py", 'w') as new_file:
        new_file.write(new_content)

print(f"{num_copies + 1} client files created successfully.")
