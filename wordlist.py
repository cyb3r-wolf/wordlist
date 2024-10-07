import itertools

def generate_permutations(input_string):
    # Generate all permutations of the input string
    permutations = set()  # Use a set to avoid duplicates
    for i in range(1, len(input_string) + 1):
        for perm in itertools.permutations(input_string, i):
            permutations.add(''.join(perm))
    return sorted(permutations)

if __name__ == "__main__":
    user_input = input("Enter characters: ")
    all_permutations = generate_permutations(user_input)
    
    print("All possible words:")
    for word in all_permutations:
        print(word)
