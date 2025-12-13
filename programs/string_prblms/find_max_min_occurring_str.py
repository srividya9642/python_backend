def count_minimum_maximum_characters(s):
    freq = {}  # Dictionary to store frequency of each character

    # Step 1: Count frequency of each character manually
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Step 2: Initialize variables to track max and min
    max_count = -1
    min_count = len(s) + 1
    max_char = ''
    min_char = ''

    # Step 3: Find maximum and minimum occurring characters
    for ch in freq:
        if freq[ch] > max_count:
            max_count = freq[ch]
            max_char = ch
        if freq[ch] < min_count:
            min_count = freq[ch]
            min_char = ch

    # Step 4: Display results
    print("Maximum occurring character:", max_char, "→", max_count)
    print("Minimum occurring character:", min_char, "→", min_count)


# Example usage
string = input("Enter a string: ")
count_minimum_maximum_characters(string)
