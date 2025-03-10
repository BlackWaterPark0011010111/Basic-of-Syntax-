import argparse

def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("first_name", nargs="?", default="Larry", help="First name")
    parser.add_argument("last_name", nargs="?", default="Hanson", help="Last name")
    parser.add_argument("age", nargs="?", type=int, default=100, help="Age")
    parser.add_argument("--fast", action="store_true", help="enable fast mode")

    args = parser.parse_args()

    if args.fast:
        print("Fast mode enabled")
    
    age_plus_one = args.age + 1
    print(f"Hello, {args.first_name} {args.last_name}! I see you have had {age_plus_one} birthdays.")

if __name__ == "__main__":
    main()