import csv

def main():
    data = {}
    with open('data.csv') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            dsplit = row[0].split("/")
            date = f"{dsplit[2]}-{dsplit[1]}-01"
            amount_str = row[2]
            if not amount_str:
                continue

            amount = float(amount_str.replace(",", ""))
            if date in data:
                data[date] += amount
            else:
                data[date] = amount
    for key, value in reversed(data.items()):
        if value:
            print(f"{key},Credit Card,{value:.2f}")


if __name__ == "__main__":
    main()
