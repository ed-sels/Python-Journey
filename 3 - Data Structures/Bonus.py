import json

def add_movie(movie_collection):
    """Add a movie to the collection."""
    title = input("Enter movie title: ")
    year = int(input("Enter movie year: "))
    movie_collection[title] = year
    print(f"Movie '{title}' added successfully.")

def save_movies(movie_collection):
    """Save the movie collection to a file."""
    with open("movies.json", "w") as file:
        json.dump(movie_collection, file)
    print("Movie collection saved successfully.")

def load_movies():
    """Load the movie collection from a file."""
    try:
        with open("movies.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No movie collection found.")
        return {}

def print_movies(movie_collection):
    """Print all movies sorted by year."""
    sorted_movies = sorted(movie_collection.items(), key=lambda x: x[1])
    for title, year in sorted_movies:
        print(f"{title} ({year})")

def main():
    movie_collection = load_movies()
    
    while True:
        print("\nMovie Collection Manager")
        print("1. Add a movie")
        print("2. Save movies")
        print("3. Load and print movies")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_movie(movie_collection)
        elif choice == "2":
            save_movies(movie_collection)
        elif choice == "3":
            movie_collection = load_movies()
            print_movies(movie_collection)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()