from itertools import combinations

def generate_emails(email_base, count):
    # Ensure the base email is in lowercase
    email_base = email_base.lower()
    
    # Extract the username and domain from the email base
    username = email_base.split('@')[0]
    domain = email_base.split('@')[1]
    
    # List to store all possible email addresses
    generated_emails = []
    
    # Generate all possible combinations for inserting dots
    for num_dots in range(1, len(username)):
        for comb in combinations(range(1, len(username)), num_dots):
            temp_username = list(username)
            for pos in sorted(comb, reverse=True):
                temp_username.insert(pos, '.')
            generated_emails.append(''.join(temp_username))
    
    # Combine the generated usernames with the email domain
    generated_emails = [f"{usr}@{domain}" for usr in generated_emails]

    # Handle cases where n is larger than the number of possible emails
    max_count = min(count, len(generated_emails))
    
    # Write the result up to the specified count (or max possible) to a text file
    with open('generated_emails.txt', 'w') as f:
        for i, email in enumerate(generated_emails[:max_count], start=1):
            f.write(f"{email}\n")

# Example usage
n = 10000  # Number of email addresses to generate
email = "worolkeith@gmail.com"
generate_emails(email, n)
