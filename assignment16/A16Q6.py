def CheckNum(no):
    if no>0:
        print("positive number(+ve)")
    elif no<0:
        print("negative number(-ve)")
    else:
        print("zero(0)")

def main():
    num = int(input("enter a number"))
    CheckNum(num)


if __name__ == "__main__":
    main()
