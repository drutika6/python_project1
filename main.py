movies = [
    {"name": "Baahubali: The Beginning", "genres": ["action", "drama"]},
    {"name": "Baahubali: The Conclusion", "genres": ["action", "drama"]},
    {"name": "RRR", "genres": ["action", "drama"]},
    {"name": "Arjun Reddy", "genres": ["romance", "drama"]},
    {"name": "Geetha Govindam", "genres": ["romance", "comedy"]},
    {"name": "Eega", "genres": ["fantasy", "action"]},
    {"name": "Mahanati", "genres": ["biography", "drama"]},
    {"name": "Jersey", "genres": ["sports", "drama"]},
    {"name": "Ala Vaikunthapurramuloo", "genres": ["family", "drama"]},
    {"name": "Pushpa: The Rise", "genres": ["action", "crime"]},
    {"name": "Pokiri", "genres": ["action", "crime"]},
    {"name": "Fidaa", "genres": ["romance", "drama"]},
    {"name": "Temper", "genres": ["action", "drama"]},
    {"name": "Athadu", "genres": ["action", "thriller"]},
    {"name": "Khaleja", "genres": ["action", "comedy"]}
]

user_input = input("Enter genres you like (comma separated): ").lower().split(",")

user_genres = [g.strip() for g in user_input]

recommendations = []

for movie in movies:
    match_count = 0

    for genre in user_genres:
        if genre in movie["genres"]:
            match_count += 1

    if match_count > 0:
        recommendations.append((movie["name"], match_count))

recommendations.sort(key=lambda x: x[1], reverse=True)

if recommendations:
    print("\nTop Telugu Movie Recommendations:")
    for movie, score in recommendations[:5]:
        print(f"{movie} (match score: {score})")
else:
    print("No matching movies found")
