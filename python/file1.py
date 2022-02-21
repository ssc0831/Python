# 파일 열기
# f = open('python/새파일.txt', 'r')

# 파일 쓰기
# for i in range(11, 21):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)

# 파일 읽기
# while True:
#     line = f.readline()
#     if not line: break
#     print(line, end='')

# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)

# data = f.read()
# print(data)

# 파일 닫기
# f.close()

# with문과 함께 사용하기
# f = open("새파일.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()

# with open("foo.txt", 'w') as f:
#     f.write("Life is too short, you need python")
