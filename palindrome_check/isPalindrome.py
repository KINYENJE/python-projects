def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

    print(cleaned_s)
    # output: amanaplanacanalpanama
    
    # Compare the string with its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage:
s = "A man, a plan, a canal, Panama!"
result = is_palindrome(s)
print(result)  # Output: True
