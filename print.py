def mask_password(password):
    length = len(password)

    # Edge Case: If the password is 2 characters or less, 
    # there is no "middle" to hide.
    if length <= 2:
        return password

    # 1. Get the first character
    first_char = password[0]
    
    # 2. Get the last character
    last_char = password[-1]
    
    # 3. Create a string of stars. 
    # quantity = total length minus the first and last char (2)
    stars = "*" * (length - 2)

    # Combine them
    return first_char + stars + last_char

# --- Main Program ---
user_input = input("Enter your password: ")
masked_output = mask_password(user_input)