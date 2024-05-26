num_copies = 30

path = './src/client0.py'

# Read the content of the original client0 file
with open(path, 'r') as file:
    content = file.read()

# Loop to create copies and modify the client_name variable
for i in range(1, num_copies):
    new_client_name = f"client{i}"
    new_content = content.replace('client0', new_client_name)
    new_content = new_content.replace(f'client=0', f'client={i}')
    if i>19:
        new_content = new_content.replace(f'target=0', f'target=1')
        new_content = new_content.replace(f'[rnd*35:rnd*(35)+35]', f'[rnd*54:rnd*(54)+54]')
    print(f'new client: {new_client_name}')
    
    # Write the new content to the new file
    with open(f"./src/{new_client_name}.py", 'w') as new_file:
        new_file.write(new_content)

print(f"{num_copies + 1} client files created successfully.")
