import csv
from datetime import date
from dateutil.relativedelta import relativedelta

def main():
    data = {}
    with open('data.csv') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            if not row:
                continue
            dsplit = row[0].split("/")
            d = f"{dsplit[2]}-{dsplit[1]}-01"
            amount_str = row[2]
            if not amount_str:
                continue

            amount = float(amount_str.replace(",", ""))
            if d in data:
                data[d] += amount
            else:
                data[d] = amount
    for key, value in reversed(data.items()):
        if value:
            year, month, day = [int(i) for i in key.split("-")]
            end_of_month = date(year, month, day) + relativedelta(months=1) - relativedelta(days=1)
            print(f"ADD CC {value:.2f} {end_of_month}")


if __name__ == "__main__":
    main()
