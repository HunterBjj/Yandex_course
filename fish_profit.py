day = list(map(int, input().split()))
profit = []
num = list(map(int, input().split()))
profit += num


def cntprofit(profit):
    res = 0
    for i in range(len(profit)):
        for j in range(i, len(profit), 1):
            diff = profit[i] - profit[j]
            if j - i <= day[1] and abs(diff) > abs(res):
                res = diff
    if res > 0:
        return 0
    else:
        return abs(res)


if __name__ == '__main__':
    print(cntprofit(profit))
