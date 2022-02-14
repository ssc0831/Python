# for문
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장 2
#     ...

# # test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a: 
#     print(first + last)

# a = [(1,2), (3,4), (5,6)]
# for i in a: 
#     print(i)

# a = [(1,2), (3,4), (5,6)]
# for i, j in a: 
#     print(i, j)


# a = [(1,2), (3,4), (5,6)]
# for i in a: 
#     print(i, "-->", type(i))

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# marks = [90, 25, 67, 45, 80]
# number = 0 
# for mark in marks: 
#     number += 1 
#     if mark < 60: 
#         continue
#     print("%d번 학생은 합격입니다." % number)

# a = [1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i, end=' ')
# print()
# for i in range(1,11):
#     print(i, end=' ')

# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# for i in range(2,10):
#     print()
#     for j in range(1,10):
#         print(i,"*", j, "=", i*j, end='  ')
# print()

# for i in range(2,10):
#     for j in range(1,10):
#         print(i,"*", j, "=", i*j, end='    ')
#     print()

# a=[1, 2, 3, 4]
# result=[]
# for(num*3) num in a:
#     result.append
# print(result)

# a=[1, 2, 3, 4]
# result=[num * 3 for num in a]
# print(result)

# a=[1, 2, 3, 4]
# result=[num * 3 for num in a if num % 2 ==0]
# print(result)

