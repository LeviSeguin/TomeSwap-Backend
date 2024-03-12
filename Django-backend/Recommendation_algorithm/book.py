from Recommendation_algorithm.models import Book

# List of tuples containing book titles and authors
books_data = [
    ("To Kill a Mockingbird", "Harper Lee"),
    ("1984", "George Orwell"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("Pride and Prejudice", "Jane Austen"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("Animal Farm", "George Orwell"),
    ("The Da Vinci Code", "Dan Brown"),
    ("The Alchemist", "Paulo Coelho"),
    ("The Hunger Games", "Suzanne Collins"),
    ("The Kite Runner", "Khaled Hosseini"),
    ("Gone with the Wind", "Margaret Mitchell"),
    ("The Girl with the Dragon Tattoo", "Stieg Larsson"),
    ("The Chronicles of Narnia", "C.S. Lewis"),
    ("Moby-Dick", "Herman Melville"),
    ("Wuthering Heights", "Emily Brontë"),
    ("The Road", "Cormac McCarthy"),
    ("Brave New World", "Aldous Huxley"),
    ("The Hitchhiker's Guide to the Galaxy", "Douglas Adams"),
    ("The Picture of Dorian Gray", "Oscar Wilde"),
    ("Jane Eyre", "Charlotte Brontë"),
    ("Frankenstein", "Mary Shelley"),
    ("One Hundred Years of Solitude", "Gabriel García Márquez"),
    ("Lord of the Flies", "William Golding"),
    ("The Shining", "Stephen King"),
    ("The Handmaid's Tale", "Margaret Atwood"),
    ("A Game of Thrones", "George R.R. Martin"),
    ("The Road Less Traveled", "M. Scott Peck"),
    ("The Bell Jar", "Sylvia Plath"),
    ("Siddhartha", "Hermann Hesse"),
    ("Catch-22", "Joseph Heller"),
    ("Crime and Punishment", "Fyodor Dostoevsky"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky"),
    ("Les Misérables", "Victor Hugo"),
    ("The Count of Monte Cristo", "Alexandre Dumas"),
    ("The Grapes of Wrath", "John Steinbeck"),
    ("East of Eden", "John Steinbeck"),
    ("Anna Karenina", "Leo Tolstoy"),
    ("The Adventures of Sherlock Holmes", "Arthur Conan Doyle"),
    ("A Tale of Two Cities", "Charles Dickens"),
    ("War and Peace", "Leo Tolstoy"),
    ("The Odyssey", "Homer"),
    ("The Iliad", "Homer"),
    ("Don Quixote", "Miguel de Cervantes"),
    ("The Divine Comedy", "Dante Alighieri"),
    ("The Canterbury Tales", "Geoffrey Chaucer"),
    ("Hamlet", "William Shakespeare"),
    # Add more books as needed
]

# Create and save Book objects
for title, author in books_data:
    book = Book(title=title, author=author)
    book.save()