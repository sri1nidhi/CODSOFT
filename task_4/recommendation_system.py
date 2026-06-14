import pandas as pd

# Load dataset
movies = pd.read_csv("movies.csv")

print("=" * 40)
print("MOVIE RECOMMENDATION SYSTEM")
print("=" * 40)

genre = input(
    "\nEnter preferred genre "
    "(Action/Sci-Fi/Animation/Romance): "
)

recommended = movies[
    movies["Genre"].str.lower() == genre.lower()
]

if len(recommended) > 0:

    print("\nRecommended Movies:\n")

    for movie in recommended["Movie"]:
        print("•", movie)

else:
    print("\nNo recommendations found.")