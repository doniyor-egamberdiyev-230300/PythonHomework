import sqlite3

# Connect to or create the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# 1. Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# 2. Insert initial data
cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

# 3. Update data (Change the Year_Published of "1984" to 1950)
cursor.execute("""
UPDATE Books 
SET Year_Published = 1950 
WHERE Title = '1984'
""")

# 4. Retrieve and display Dystopian books
cursor.execute("""
SELECT Title, Author FROM Books 
WHERE Genre = 'Dystopian'
""")
print("Dystopian Books:")
for row in cursor.fetchall():
    print(row)

# 5. Delete all books published before 1950
cursor.execute("""
DELETE FROM Books 
WHERE Year_Published < 1950
""")

# 6. Add a new column `Rating`
cursor.execute("""
ALTER TABLE Books ADD COLUMN Rating REAL
""")

# 7. Update rating values
rating_data = {
    "To Kill a Mockingbird": 4.8,
    "1984": 4.7,
    "The Great Gatsby": 4.5
}

for title, rating in rating_data.items():
    cursor.execute("""
    UPDATE Books 
    SET Rating = ? 
    WHERE Title = ?
    """, (rating, title))

# 8. Retrieve all books sorted by Year_Published in ascending order
cursor.execute("""
SELECT * FROM Books 
ORDER BY Year_Published ASC
""")
print("\nBooks sorted by Year_Published:")
for row in cursor.fetchall():
    print(row)

# Save changes and close the connection
conn.commit()
conn.close()
