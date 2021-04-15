#함수 3rd- 반복되는 코드들을 그룹으로 모아놓은 것을 말한다.

# 여러줄 주석  Shift + Alt + A
# 한줄한줄 Ctrl + /

# 다른 이름들을 사용하고 자 할 때

# 4)
a = "정수"
b = "태희"
c = "환준"
d = "세영"
a1 = 20
a2 = 19

# def chat(name1, name2):           #함수들이 인자라는 것을 받는다.(파라미터, 아규먼트로 명칭)
#     print("%s: 안녕? 넌 몇 살이니?" % name1)
#     print("%s: 나? 나는 20살이야!" % name2)

# chat(a, b)
# chat(c, d)


# 5)
def chat(name1, name2, age):           #함수들이 인자라는 것을 받는다.(파라미터, 아규먼트로 명칭)
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 %d" % (name2, age) + "살이야!")

chat("a", "b", a1)
chat("c", "d", a2)