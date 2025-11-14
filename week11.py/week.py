'''
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def play(self):
        print(f" Now playing: '{self.title}' by {self.artist}")

    def __str__(self):
        return f"Song: {self.title} by {self.artist}"



class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = []  

    def add_song(self, song):
        self.songs.append(song)
        print(f"{song.title}' added to playlist '{self.playlist_name}'")

    def play_all(self):
        print(f"\n Playing all songs in playlist: {self.playlist_name}")
        for song in self.songs:
            song.play()

    def __str__(self):
        return f"Playlist: {self.playlist_name} ({len(self.songs)} songs)"



song1 = Song("Shape of You", "Ed Sheeran")
song2 = Song("Blinding Lights", "The Weeknd")

playlist = Playlist("My Favorites")
playlist.add_song(song1)
playlist.add_song(song2)

playlist.play_all()

print(playlist)



class TVShow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def preview(self):
        print(f"Preview: '{self.title}' - Genre: {self.genre}")

    def __str__(self):
        return f"TV Show: {self.title} ({self.genre})"



class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.shows = []  

    def add_show(self, show):
        self.shows.append(show)
        print(f"{show.title}' added to {self.profile_name}'s dashboard")

    def display_recommendations(self):
        print(f"\n{self.profile_name}'s Netflix Dashboard:")
        for show in self.shows:
            show.preview()

    def __str__(self):
        return f"Netflix Dashboard ({self.profile_name}) - {len(self.shows)} shows"



show1 = TVShow("Stranger Things", "Sci-Fi")
show2 = TVShow("Money Heist", "Action/Drama")

dashboard = NetflixDashboard("Risid")
dashboard.add_show(show1)
dashboard.add_show(show2)

dashboard.display_recommendations()

print(dashboard)

#Q11
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print(f"Book Title: '{self.title}', Author: {self.author}")

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []  

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added to library '{self.library_name}'")

    def display_books(self):
        print(f"\nBooks in Library: {self.library_name}")
        for book in self.books:
            book.display_info()

    def __str__(self):
        return f"Library: {self.library_name} ({len(self.books)} books)"
    
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")   

library = Library("City Library")
library.add_book(book1)
library.add_book(book2)
library.display_books()
print(library)

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def show_description(self):
        print(f"Menu Item: '{self.name}', Price: ${self.price:.2f}")

    def __str__(self):
        return f"Menu Item: {self.name} - ${self.price:.2f}"
    
class RestaurantMenu:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu_items = []  

    def add_menu_item(self, item):
        self.menu_items.append(item)
        print(f"'{item.name}' added to menu of '{self.restaurant_name}'")

    def display_menu(self):
        print(f"\nMenu for Restaurant: {self.restaurant_name}")
        for item in self.menu_items:
            item.show_description()

    def __str__(self):
        return f"Restaurant Menu: {self.restaurant_name} ({len(self.menu_items)} items)"
    
item1 = MenuItem("Margherita Pizza", 12.99)
item2 = MenuItem("Caesar Salad", 8.49)
menu = RestaurantMenu("Gourmet Bistro")
menu.add_menu_item(item1)
menu.add_menu_item(item2)
menu.display_menu()
print(menu)'''

class LLM:
    def __init__(self, name: str, token_limit: int):
        self.name = name
        self.token_limit = token_limit if isinstance(token_limit, int) and token_limit > 0 else 0

    def get_token_limit(self) -> int:
        return self.token_limit

    def set_token_limit(self, new_limit: int) -> bool:
        if isinstance(new_limit, int) and new_limit > 0:
            self.token_limit = new_limit
            return True
        print(f"Error: Invalid limit '{new_limit}'. Token limit must be a positive integer.")
        return False

    def __str__(self) -> str:
        return f"LLM Model: {self.name} | Max Context: {self.token_limit} tokens"


class AICompany:
    def __init__(self, company_name: str, founding_year: int):
        self.company_name = company_name
        self.founding_year = founding_year
        self.headquarters = "Not Assigned"
        self.llms = []

    def get_headquarters(self) -> str:
        return self.headquarters

    def set_headquarters(self, new_hq: str):
        self.headquarters = new_hq

    def add_llm(self, llm_instance: LLM):
        if isinstance(llm_instance, LLM):
            self.llms.append(llm_instance)
            print(f"Successfully added LLM '{llm_instance.name}' to {self.company_name}.")
            return
        print("Error: Only LLM instances can be added.")

    def display_models(self):
        print(f"\n--- Developed Models by {self.company_name} ({len(self.llms)} Total) ---")
        if not self.llms:
            print("No LLMs have been developed yet.")
            print("-------------------------------------------------------")
            return

        for i, llm in enumerate(self.llms, 1):
            print(f"  {i}. {llm}")
        print("-------------------------------------------------------")

    def __str__(self) -> str:
        model_names = ', '.join([llm.name for llm in self.llms]) if self.llms else 'None'
        return (f"Company: {self.company_name} | Founded: {self.founding_year} | HQ: {self.headquarters}\n"
                f"  Developed Models ({len(self.llms)}): {model_names}")


print("--- Starting Demonstration ---")

ai_lab = AICompany("Global Research AI", 2020)
print(f"Created company: {ai_lab.company_name}")

ai_lab.set_headquarters("London, UK")

llm_alpha = LLM("Alpha-7", 32768)
llm_beta = LLM("Beta-2 Pro", 128000)

ai_lab.add_llm(llm_alpha)
ai_lab.add_llm(llm_beta)

print("\n--- Current State ---")
print(ai_lab)

ai_lab.display_models()

print(f"\n--- LLM Method Demonstrations ---")
print(f"Current limit of {llm_alpha.name}: {llm_alpha.get_token_limit()}")
llm_alpha.set_token_limit(65536)
print(f"New limit of {llm_alpha.name}: {llm_alpha.get_token_limit()}")

ai_lab.display_models()

print("--- Demonstration Complete ---")