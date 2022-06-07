s_txt = "placement"

r_txt = "Screening"
fhand = open('example.txt')
print("Original Content:",fhand.read())

with open('example.txt', 'r') as fhand:
    data = fhand.read()

    data = data.replace(s_txt, r_txt)

with open('example.txt', 'w') as fhand:
    fhand.write(data)

print("Replaced Content:",data)
