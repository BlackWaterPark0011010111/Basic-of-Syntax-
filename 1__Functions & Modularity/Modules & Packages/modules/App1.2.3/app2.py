import getopt
import sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:", ["help", "name="])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    name = None

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Usage: app2.py [-h] [-n NAME]")
            print("-h, --help : show this help message")
            print("-n NAME, --name=NAME : specify the name")
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg

    if name:
        print(f"Good Morning {name}!")
    else:
        print("Good Morning folks!")

if __name__ == "__main__":
    main()