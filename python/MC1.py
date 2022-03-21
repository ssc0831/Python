import re
p = re.compile('[a-z]+')
# m = p.match("0ython")
# m = p.match("python")
# m = p.match("0ython python")
# m = p.match("python python")
# m1 = p.search("Python apple")
# m2 = p.match("Python apple")

# print(m)
# print(m1)
# print(m2)

# m = p.match( 'string goes here' )
# if m:
#     print('Match found: ', m.group())
# else:
#     print('No match')

# result1 = p.findall("life is too short")
# result2 = p.finditer("life is too short")
# result = p.findall("Life is too short")
# print(result1)
# for r in result2:
#     print(r)
m = p.match("python")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())