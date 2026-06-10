import pandas as pd

movies = pd.read_csv(
    "data/raw/movie_titles.csv",
    header=None,
    names=["MovieID", "Year", "Title"],
    encoding="latin1",
    on_bad_lines="skip"
)

movie_dict = dict(
    zip(movies["MovieID"], movies["Title"])
)

print("Total Movies:", len(movie_dict))

print("\nMovie 1:")
print(movie_dict[1])

print("\nMovie 30:")
print(movie_dict[30])