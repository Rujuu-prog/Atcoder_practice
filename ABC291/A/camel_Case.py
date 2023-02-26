def main():
    S = input()
    count = 0
    for s in S:
        count += 1
        if s.isupper():
            print(count)
            return
            

main()
