#Problem 9:
# (a) Calculate the electricity bill in riel using progressive tiers
def electricity_bill(kwh):
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    energy_cost = tier1 * 480 + tier2 * 610 + tier3 * 730
    subtotal = energy_cost + 2000
    total_with_vat = subtotal * 1.10

    return round(total_with_vat)


# (b) Print the formatted comparison table
consumptions = [0, 35, 50, 120, 200, 350]
for kwh in consumptions:
    bill = electricity_bill(kwh)
    usd = bill / 4100
    print(f"{kwh:3} kWh -> {bill:9,} riel ({usd:7.2f} USD)")


# (c) Ask the user for their monthly consumption and print their bill
user_kwh = float(input("\nEnter your monthly consumption (kWh): "))
user_bill = electricity_bill(user_kwh)

if user_bill is None:
    print("Consumption cannot be negative.")
else:
    print(f"Your electricity bill is {user_bill:,} riel ({user_bill / 4100:.2f} USD).")