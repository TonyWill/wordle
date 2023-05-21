import csv
import sqlite3

# Create a new database
conn = sqlite3.connect("wordle.db")

# Create a table to store the words
cur = conn.cursor()
cur.execute("CREATE TABLE words (word TEXT, definition TEXT, letter_count INTEGER, usage_count INTEGER, is_word BOOLEAN)")

# Populate the table with words
with open("words.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        word = row[0]
        definition = row[1]
        letter_count = len(word)
        usage_count = 0
        is_word = True
        cur.execute("INSERT INTO words VALUES(?, ?, ?, ?, ?)", (word, definition, letter_count, usage_count, is_word))

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
