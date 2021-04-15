# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본출력
print('Hello Python!')
print("Hello Python!")
print()
print("""Hello Python!""")
print('''Hello Python!''')
print()

# Separator 옵션 설명
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'goole.com', sep='@')

# end 옵션 사용
print('Welcome to', end=' ')
print('the black paradise', end=' ')
print('piano notes')
print()

# format 사용   [], {}, ()
print('{} and {}'. format('You','Me'))
print("{0} and {1} and {0}". format('You', 'Me'))
print("{a} are {b}". format(a='You', b='Me'))

# %s: 문자, %d:정수, %f:실수
print("%s's favorite number is %d"% ('sangmin', 7)) 
print("Test 1: %5d, Price: %4.2f" % (776, 6534.123))  
print("Test 1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))  # 5d : 5자리 정수, 4.2f:4자리 정수와 소수 2자리
print("Test 1: {a: 5d}, Price: {b:4.2f}".format(a=776, b=6534.123))
print()
"""참고 Escape 코드
   \n : 개행
   \t : 탭
   \\ : 문자
   \' : 문자
   \" : 문자
   \r : 캐리지 리턴
   \f : 폼피드
   \a : 벨 소리
   \b : 백 스페이스
   \000 : 널 문자
    ...
"""
print("'you'")
print('\'you\'')
print('"you"')
print("""'You'""")
print('\\you\\\n\n\n')
print('test')
