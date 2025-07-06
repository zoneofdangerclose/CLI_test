import argparse

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple CLI example.")

    # parser.add_argument("-h", "--help", type=str, help="Your name")

    parser.add_argument("-n", '--name', type=str, help="Your name", default='Stranger')
    parser.add_argument("-a", '--age', type=int, help="Your age", default='-1')


    args = parser.parse_args()

    if '-h' in args or '--help' in args:
        print(args.description)

    else:
        greet(args.name, args.age)