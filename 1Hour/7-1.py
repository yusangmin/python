# 이름과 나이를 받아라
# 나이가 10 미만이면 "안녕"이라고 
# 나이가 10살에서 20살 사이면 "안녕하세요"라고
# 그 외에는 "안녕하십니까"라고 말해라

def sayHello(name, age):                # 이름과 나이를 인자로 받는다.
    if age < 10:                        # 나이가 10 보다 작으면
        print("안녕, " + name)          # 안녕이라고 출력해라
    elif age <=20 and age >= 10:        # 나이가 20살보다 적고 10살보다 크면
        print("안녕하세요, " + name)    # 안녕하세요.
    else:                               # 그외에는
        print("안녕하십니까, " + name)  # 
        
sayHello("태희", 20)
sayHello("정수", 6)
sayHello("세영", 40)
sayHello("철수", 10)
