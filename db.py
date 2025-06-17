import sqlite3
import os

DB_PATH = os.path.join("data", "movies.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT,
            year INTEGER,
            genre TEXT,
            rating REAL
        )
    ''')
    
    conn.commit()
    conn.close()
def add_movie(title, director, year, genre, rating):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO movies (title, director, year, genre, rating)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, director, year, genre, rating))
    
    conn.commit()
    conn.close()
from tabulate import tabulate

def get_all_movies():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT id, title, director, year, genre, rating FROM movies')
    movies = cursor.fetchall()

    conn.close()
    return movies
