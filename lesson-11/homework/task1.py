import sqlite3

# Connect to or create the database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# 1. Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Insert initial data
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# 3. Update data (Change Jadzia Dax to Ezri Dax)
cursor.execute("""
UPDATE Roster 
SET Name = 'Ezri Dax' 
WHERE Name = 'Jadzia Dax'
""")

# 4. Retrieve and display Bajoran characters
cursor.execute("""
SELECT Name, Age FROM Roster 
WHERE Species = 'Bajoran'
""")
print("Bajoran Characters:")
for row in cursor.fetchall():
    print(row)

# 5. Delete all characters older than 100 years
cursor.execute("""
DELETE FROM Roster 
WHERE Age > 100
""")

# 6. Add a new column `Rank`
cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")

# 7. Update rank values
rank_data = {
    "Benjamin Sisko": "Captain",
    "Ezri Dax": "Lieutenant",
    "Kira Nerys": "Major"
}

for name, rank in rank_data.items():
    cursor.execute("""
    UPDATE Roster 
    SET Rank = ? 
    WHERE Name = ?
    """, (rank, name))

# 8. Retrieve all characters sorted by age in descending order
cursor.execute("""
SELECT * FROM Roster 
ORDER BY Age DESC
""")
print("\nCharacters sorted by age:")
for row in cursor.fetchall():
    print(row)

# Save changes and close the connection
conn.commit()
conn.close()
