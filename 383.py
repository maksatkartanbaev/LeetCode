ransomNote = 'i will kill you'
magazine = 'ewqewqewqewqewewqe'
letters = {}
if len(magazine) < len(ransomNote):
    print(False)
for i in magazine:
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 0
for i in ransomNote:
    if i in letters:
        print(letters[i])
        if letters[i] > 0:
            letters[i] -= 1
        else:
            print(False)
            break
    else:
        print(False)
        break
print(True)