import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

categories = {
    "Food": ["Restaurant", "Swiggy", "Zomato", "Cafe"],
    "Travel": ["Uber", "Ola", "Metro", "Flight"],
    "Shopping": ["Amazon", "Flipkart", "Mall"],
    "Bills": ["Electricity", "Internet", "Mobile Recharge"],
    "Entertainment": ["Netflix", "Movie", "Spotify"]
}

payment_modes = ["UPI", "Credit Card", "Debit Card", "Cash"]

data = []

for _ in range(5000):

    category = random.choice(list(categories.keys()))
    description = random.choice(categories[category])

    transaction = {
        "Date": fake.date_between(start_date="-1y", end_date="today"),
        "Description": description,
        "Category": category,
        "Amount": round(random.uniform(50, 5000), 2),
        "Payment_Mode": random.choice(payment_modes),
        "Location": fake.city()
    }

    data.append(transaction)

df = pd.DataFrame(data)

df.to_csv("data/raw/transactions.csv", index=False)

print("Dataset created successfully")