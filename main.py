x = [1, 2, 3, 4]

# x의 4개의 엘레먼트가 있다는 리스트 함수
num_elements = len(x)
print(num_elements)

x = [4,3,2,1]

y = sorted(x)
print(y)


# sum을 이용하면 4,2,3,1 을 합친 값이 나온다
x = [4,2,3,1]

z = sum(x)
print(z)

x = [4,2,3,1]
# 리스트 엘레먼트를 차례대로 보여준다
# sum을 이용하면 4,2,3,1 을 합친 값이 나온다
x = [4,2,3,1]

z = sum(x)
print(z)

x = [4,2,3,1]
y = ["hello", "there"]
# 리스트 엘레먼트를 차례대로 보여준다
for n in x:
  print(n)

for c in y:
  print(c)

# 엘레먼트 위치 찾기
# 0,1,2,3 순으로 정렬
x = [4,2,3,1]
y = ["hello", "there"]

print(x.index(3))
print(y.index("hello"))
print("hello" in y)  # hello 가 y 안에 있어? True
print("bye" in y) # bye 가 y 안에 있어 ? false

if "hello" in y:
  print("hello 가 있어요")

  # 튜플 
x = tuple()
y = ('a', 'b', 'c')
z = (1,"hello", "there")

print(x + y)
print('a' in y)
print(z. index(1))
# Assignment 튜플 안의 값을 업데이트 하는것은 안됨.

# 가변 mutable : 값을 바꿀 수 있음
# 불변 immutable : 값을 바꿀 수 없음

## 딕셔너리
x = {
  "name": "정태",
  "age": 27,
}

print(x)
print(x["name"])
print(x["age"])

x = {
  0:"Jungtae",
  1:"Coding",
  "age": 27,
}

print(x[0])
print(x[1])
print(x["age"])
print("name" in x)
print("age" in x)

print(x.keys()) # 딕셔너리에 있는 모든 키 를 보여준다
print(x.values()) # 딕셔너리 오른쪽 라인에 있는 것을 보여준다

# 딕셔너리는 원래있는 값을 바꾸거나 새로운 값을 넣을수 있다
x = {
  0: "kyoung",
  1: "min",
  "age": 21,
}

x["school"] = "한빛"
print(x)