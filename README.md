# song-book-print
This is a short script for creating a nice htmlpage to print a song text with highlighted chords

# how to use it:
  create file .txt in the same directory as main.py
  structure of it have to be
  line 0: chords
  line 1: Name of song
  line 2: author
  line 3: notes, like "capo, 4th. fret" etc
  other lines: text with chords, spaced
  
  run the python file without arguments (or exe file from release) and it will scan current directory for a txt files.
  Using an argument you can convert only the one file.
  Argument help or ? can show usage 

  run! and its done :)
  
  script will create a html static page that has a sup tags around chords and this way it will highlight chords in a text, like this <sup> Chord</sup>. With css you can also customize color, now just a style tag in head, but you can attach a css file to be easily edited and customized. 
