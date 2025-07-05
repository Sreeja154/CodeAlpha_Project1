import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of IMDb movie URLs
movie_urls = [
    "https://www.imdb.com/title/tt0111161/",  # The Shawshank Redemption
    "https://www.imdb.com/title/tt1375666/",  # Inception
    "https://www.imdb.com/title/tt0468569/",  # The Dark Knight
    "https://www.imdb.com/title/tt4154796/",  # Avengers: Endgame
    "https://www.imdb.com/title/tt0133093/"   # The Matrix
]

# Headers to simulate browser
headers = {"User-Agent": "Mozilla/5.0"}

# Store results
movie_data = []

for url in movie_urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Unknown Title"

    # Extract IMDb rating
    rating_block = soup.find('div', attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"})
    if rating_block:
        rating = rating_block.find('span').get_text(strip=True)
        rating_value = float(rating)
    else:
        rating_value = "N/A"

    # Append result
    movie_data.append({"Movie Title": title, "IMDb Rating": rating_value})
    print(f"✅ {title} → {rating_value}/10")

# Save to Excel
df = pd.DataFrame(movie_data)
df.to_excel("imdb_ratings_multiple.xlsx", index=False)

print("\n📁 All ratings saved to 'imdb_ratings_multiple.xlsx'")
