s = input()
s = list(s)
s.reverse()
for i in range(len(s)):
    if s[i] != '0':
        break
print(*s[i::],sep='')

'''s[start:end:interval]
s[start::]
s[:end:]'''