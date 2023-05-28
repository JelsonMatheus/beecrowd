def main():
    while True:
        try:
            N = int(input())
            cost_per_day = int(input())
            max_here = 0
            profit = 0
            for _ in range(N):
                value = int(input()) - cost_per_day
                max_here = max(max_here + value, value)
                profit = max(profit, max_here)
            print(profit)
        except EOFError:
            break


if __name__ == '__main__':
    main()