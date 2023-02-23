# AC
def main():
    s = input()
    s = s.replace('0', '2').replace('1', '0').replace('2', '1')
    print(s)

main()