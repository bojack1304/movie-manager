from db import init_db, add_movie, get_all_movies
from tabulate import tabulate

def show_menu():
    print("\n🎬 Gestionnaire de films")
    print("1. Ajouter un film")
    print("2. Afficher tous les films")
    print("3. Quitter")

def menu():
    init_db()
    
    while True:
        show_menu()
        choice = input("\nChoix : ").strip()
        
        if choice == "1":
            title = input("Titre : ")
            director = input("Réalisateur : ")
            year = int(input("Année : "))
            genre = input("Genre : ")
            rating = float(input("Note (/10) : "))
            add_movie(title, director, year, genre, rating)
            print("✅ Film ajouté avec succès !")

        elif choice == "2":
            movies = get_all_movies()
            if movies:
                headers = ["ID", "Titre", "Réalisateur", "Année", "Genre", "Note"]
                print("\n🎞️ Liste des films :")
                print(tabulate(movies, headers=headers, tablefmt="fancy_grid"))
            else:
                print("❌ Aucun film trouvé.")

        elif choice == "3":
            print("👋 Au revoir !")
            break

        else:
            print("⛔ Choix invalide.")

if __name__ == "__main__":
    menu()
