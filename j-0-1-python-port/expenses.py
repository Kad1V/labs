import csv
totals = {} #category -> total amount
day_total = {} #date -> total amount
max_amount = 0
max_category = ""
max_date = ""


with open('expenses.csv', mode = 'r', newline = '', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row["category"]
        amount = int(row["amount"])
        date = row["date"]

        totals[category] = totals.get(category, 0) + amount
        day_total[date] = day_total.get(date, 0) + amount

        if amount > max_amount:
            max_amount = amount
            max_date = date
            max_category = category

print("Total per category: ")

for category, total in totals.items():
    print(f"{category}: {total}")

print(f"Largest expense: {max_category} on {max_date}, {max_amount}")
top_day = max(day_total, key=day_total.get)
print(f"Most expensive day: {top_day}, {day_total[top_day]}")
