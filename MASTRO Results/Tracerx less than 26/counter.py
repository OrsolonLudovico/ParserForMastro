import argparse

def count(riga):
    return riga.split(';', 1)[0].count(',')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Input file")
    args = parser.parse_args()

    cont = []

    with open(args.file, 'r') as file:
        for riga in file:
            num_v = count(riga)
            cont.append(num_v + 1)
            print(num_v + 1)

    if len(cont) > 0:
        mean = sum(cont) / len(cont)
        print(f"Mean: {mean}")
    else:
        print("Sorry, empty file")

if __name__ == "__main__":
    main()