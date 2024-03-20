# You are maintaining a library system where each book is stored as a
# tuple within a list. Your task is to update this system by adding 
# new books and ensuring no duplicates.

# Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.


def add_book(library, book_to_add):
    for book in library:
        if book_to_add[0] == book[0]:
            print("This is a duplicate")
        
            return None
        
        
    library.append(book_to_add)
            
            
add_book(library, ("Seven husbands of evelyn hugo", "taylor jenkin reid"))

add_book(library, ("Brave New World", "Aldous Huxley"))

print(library)