import random
import string

def generate_unique_key(existing_keys, max_key_value):
    key = random.randint(1, max_key_value)
    while key in existing_keys:
        key = random.randint(1, max_key_value)
    return key

def generate_random_value(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_trace_file(filename, num_entries, max_key_value):
    with open(filename, 'w') as file:
        used_keys = set()

        for _ in range(num_entries):
            key = generate_unique_key(used_keys, max_key_value)
            value = generate_random_value()
            file.write(f"insert,{key},{value}\n")
            used_keys.add(key)

# Generate a tracefile with 100 unique insert commands
generate_trace_file('tracefile.txt', 100, 10000)