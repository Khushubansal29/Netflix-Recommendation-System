import pandas as pd

input_file = "data/raw/combined_data_1.txt"
output_file = "data/sample_ratings.csv"

TARGET_RATINGS = 100000

data = []
current_movie = None
rating_count = 0

print("Creating sample dataset...")

with open(input_file, "r") as f:

    for line in f:

        line = line.strip()

        if line.endswith(":"):
            current_movie = int(line[:-1])

        else:
            user_id, rating, date = line.split(",")

            data.append([
                current_movie,
                int(user_id),
                int(rating)
            ])

            rating_count += 1

            if rating_count >= TARGET_RATINGS:
                break

df = pd.DataFrame(
    data,
    columns=["MovieID", "UserID", "Rating"]
)

df.to_csv(output_file, index=False)

print("\nSample dataset created!")
print(df.shape)
print(f"Saved to: {output_file}")