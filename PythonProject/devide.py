def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다"
    return a / b

if __name__ == "__main__":
    print(divide(10, 2))  # 결과: 5.0
