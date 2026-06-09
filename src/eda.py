import pandas as pd

file_path = "data/raw/combined_data_1.txt"

print("Reading first 10000 lines...")

with open(file_path, "r") as f:
    lines = [next(f).strip() for _ in range(10000)]

data = []
current_movie = None

for line in lines:

    if line.endswith(":"):
        current_movie = int(line[:-1])

    else:
        user_id, rating, date = line.split(",")

        data.append([
            current_movie,
            int(user_id),
            int(rating)
        ])

df = pd.DataFrame(
    data,
    columns=["MovieID", "UserID", "Rating"]
)

print("\nFirst 5 Rows\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nUnique Users:")
print(df["UserID"].nunique())

print("\nUnique Movies:")
print(df["MovieID"].nunique())

print("\nAverage Rating:")
print(round(df["Rating"].mean(), 2))

import matplotlib.pyplot as plt

# Rating Distribution
rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index, rating_counts.values)

plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.savefig("reports/rating_distribution.png")

print("\nChart saved as reports/rating_distribution.png")