import imdb

# Create an instance of IMDb
ia = imdb.IMDb()

def get_movie_recommendations(genre):
    """
    Get movie recommendations based on the provided genre.

    Parameters:
    - genre (str): The genre for which movie recommendations are requested.

    Returns:
    - list: A list of movie titles.
    """
    # Search for movies based on the provided genre
    movies = ia.get_keyword(genre)
    
    # Extract titles of the first 10 movies
    movie_titles = [movie['title'] for movie in movies[:10]]
    
    return movie_titles

def get_movie_details(movie_title):
    """
    Get details of a movie based on its title.

    Parameters:
    - movie_title (str): The title of the movie.

    Returns:
    - tuple: A tuple containing director, actors, and description.
    """
    # Search for the movie by title
    movie = ia.search_movie(movie_title)[0]
    
    # Retrieve detailed information about the movie
    ia.update(movie)
    
    # Extract information
    director = ', '.join([person['name'] for person in movie.get('director', [])])
    actors = [person['name'] for person in movie.get('cast', [])][:3]  # Take only the first 3 actors
    description = movie.get('plot')[0] if movie.get('plot') else "Not available"
    
    return director, actors, description

def main():
    # Ask the user for a movie genre
    genre = input("Enter a movie genre: ")
    
    # Get recommendations based on the provided genre
    recommendations = get_movie_recommendations(genre)
    
    # Print the recommendations
    print("Recommended movies:")
    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")
    
    # Ask the user to select a movie
    while True:
        try:
            selection = int(input("Select a movie (enter the number): "))
            if 1 <= selection <= len(recommendations):
                break
            else:
                print("Invalid selection. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    selected_movie = recommendations[selection - 1]
    
    # Get details of the selected movie
    director, actors, description = get_movie_details(selected_movie)
    
    # Print the details
    print("\nMovie Details:")
    print("Director:", director)
    print("Actors:")
    for actor in actors:
        print("-", actor)
    print("Description:", description)

if __name__ == "__main__":
    main()