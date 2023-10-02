import string

a_string = 'Zdravo! Kakvo je vrijeme danas?'
new_string = a_string.translate(str.maketrans('', '', string.punctuation))

print(new_string)

# Rezultat: Zdravo Kakvo je vrijeme danas


print(string.punctuation)

# Rezultat: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
