print

# Get user name

email = raw_input('What is your email address?\n').strip()

print

# Slice user name

user_name = email[0:email.index('@'):1] 

# Slice domain name

domain = email[email.index('@')+1::1]

# Format message

output = 'User name is: {}\nDomain is: {}'.format(user_name,domain)

# Display message

print output