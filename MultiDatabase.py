import sqlite3
import xml.etree.ElementTree as ET
from urllib.request import urlopen

conn = sqlite3.connect('multidatabase.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'Library.xml'
fh = open(fname).read()
tree = ET.fromstring(fh)

def lookUp(nodes,key):
    found = False
    for node in nodes:
        if found : return node.text
        if node.tag == 'key' and node.text == key :
            found = True
    return None

xml = tree.findall("dict/dict/dict")
for item in xml:
    if ( lookUp(item, 'Track ID') is None ) : continue
    artist = lookUp(item, 'Artist')
    name = lookUp(item,'Name')
    count = lookUp(item, 'Play Count')
    rating = lookUp(item, 'Rating')
    length = lookUp(item, 'Total Time')
    genre = lookUp(item, 'Genre')
    album = lookUp(item,'Album')
    print(artist,name,count,rating,length,genre,album)
    if name is None or artist is None or album is None or genre is None: 
        continue
    cur.execute('''INSERT OR IGNORE INTO Artist(name) values (?)''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Genre(name) values (?)''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]
    cur.execute('''INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count) VALUES ( ?, ?, ?, ?, ?,? )''', ( name, album_id,genre_id, length, rating, count ) )
conn.commit()

    

    