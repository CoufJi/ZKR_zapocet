
text = input("Zadej text: ")

special_symbols = ",.-§()+-/*\"''$&@„?”!"
new_text = ""

for i in range(0, len(text)):
    if text[i] not in special_symbols:
        new_text += text[i]

text = new_text

print("\nVýsledek:", text)