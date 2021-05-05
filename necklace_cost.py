def calculate(price, count):
    return price*count

total_cost = 0

n = int(input("진주원석의 개수는? "))
cost = int(input("진주원석의 가격은? "))
total_cost = total_cost+calculate(cost, n)

n = int(input("사파이어원석의 개수는? "))
cost = int(input("사파이어원석의 가격은? "))
total_cost = total_cost+calculate(cost, n)

n = int(input("목걸이줄 길이는(단위는 미터)? "))
cost = int(input("목걸이줄의 미터당 가격은? "))
total_cost = total_cost+calculate(cost, n)

print(total_cost)
