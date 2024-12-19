import os
import random
import string

def generate_random_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def generate_file_with_strings(file_path, size_mb, min_length, max_length):
    # Convert size to bytes
    size_bytes = size_mb * 1024 * 1024
    written_bytes = 0
    # Open the file for writing
    with open(file_path, 'w') as file:
        while written_bytes < size_bytes:
            # Generate a random string
            random_string = generate_random_string(min_length, max_length)
            # Write the string followed by a newline
            file.write(random_string + '\n')
            # Update the number of written bytes
            written_bytes += len(random_string) + 1  # +1 for the newline character

if __name__ == "__main__":
    file_path = "500mb_file.txt"
    size_mb = 500
    min_length = 10
    max_length = 50
    generate_file_with_strings(file_path, size_mb, min_length, max_length)
    print(f"File '{file_path}' of size {size_mb} MB has been created.")

