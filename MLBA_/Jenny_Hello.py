#
#Jenny, 2026/2/25
#Jenny_Hello.py
#Print Hello
#

name="THU"
price = 250
units_sold = 1200

total_sales = price * units_sold
discount = total_sales *0.05
net_sales = total_sales - discount

print(f"Total_sales: ${total_sales:,}")
print(f"Discount    : ${discount:,.2f}")
print(f"Net Sales   : ${net_sales:,.2f}")

# if / elif / else
quarterly_profit = 85_000

if quarterly_profit > 100_000:
    print("Outstanding quarter — bonus approved.")
elif quarterly_profit > 50_000:
    print("Good quarter — on target.")
elif quarterly_profit > 0:
    print("Marginal quarter — review costs.")
else:
    print("Loss this quarter — action required.")

customer_age  = 35
account_value = 120_000

if customer_age >= 30 and account_value >= 100_000:
    print("Eligible for premium wealth management services.")
else:
    print("Standard account services apply.")