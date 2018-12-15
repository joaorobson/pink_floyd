import genius
import os

ALBUMS = ["The Piper at the Gates of Dawn",
          "A Saucerful of Secrets",
          "More (Original Film Soundtrack)",
          "Ummagumma",
          "Atom Heart Mother",
          "Meddle",
          "Obscured by Clouds",
          "The Dark Side of the Moon",
          "Wish You Were Here",
          "Animals",
          "The Wall",
          "The Final Cut",
          "A Momentary Lapse of Reason",
          "The Division Bell",
          "The Endless River"]

GENIUS_KEY = os.environ['GENIUS_KEY']
API = genius.Genius(GENIUS_KEY)
genius.Genius.search_album(API, "Pink Floyd","More (Original Film Soundtrack)" )
'''
for album in ALBUMS:
    genius.Genius.search_album(API, "Pink Floyd", album)
'''
