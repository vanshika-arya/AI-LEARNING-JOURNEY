
count=0
for i in "vanshika": #loop me hum direct string bhi pass kar sakte hain
    if i=='a':
        count+=1
print(count, 'letters found')

#string membership test
s="vanshika"

print('l' in s)
print('shi' in s)

print("alshi".upper())
print("VANSHI".lower())

print("hey i am vanshika jo abhi borrrrrrr ho rhi hai  use ghar jana hai".split())
print(' '.join(['hey', 'i', 'am', 'vanshika', 'jo', 'abhi', 'borrrrrrr', 'ho', 'rhi', 'hai', 'use', 'ghar', 'jana', 'hai']))

print("hello".find("lo")) #agr mila to first letter ka index de dega

s1="good morning"
s2=s1.replace("good" , "bad")
print(s2)

#palindrome or not
# v="alala"
# original=v
# rev=' '
# for i in (v ,-1):
#     rev=rev[i]
# if(original==rev):
#     print("palindrom")
# else:
#     ("not a palindrome")
s = "alala"
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        print("Nhiiii")
        break
else:
    print("haiii")

#que
