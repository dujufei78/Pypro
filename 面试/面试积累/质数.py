def is_prime(n):
    # 质数判断
    if n<=1:
        return False
    else:
        for i in range(2, int(n**0.5) +1): # 为了避免 2 3   3 2 重复检查，只检查2即可，即int(6**0.2)=2
            if n % i == 0:
                return False
    return True

if __name__ == '__main__':
    res = is_prime(6)
    print(res)