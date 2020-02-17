"""
    Name:       Hunter Files
    Date:       2/17/2020
    Project:    BibleVerseOfTheDay
    Version:    0.0.1
    Copyright 2020, Hunter Files, All rights reserved.

    This will be an application that you can store and pull bible verses.
    The plan is to have this application ran through my website,
    filestechnologies.com, and start posting a bible verse of the day.

    The website will have many more functions, mainly to show what work I
    have currently completed, a place to find my resume, and if you need
    work you will be able to inquire from there.

    Hope you enjoy this project as much as I have!
"""
from src.bible_verse import Verse
import pymongo


""" Example should come out as verse below is displayed"""
# 2 Timothy 1:7, "For God hath not given us the spirit of fear;
# but of power, and of love, and of a sound mind."
book = '2 Timothy'
chapter = 1
verse = 7
quote = 'For God hath not given us the spirit of fear; but of power, and of love, and of a sound mind.'

todaysVerse = Verse(book, chapter, verse, quote)
print(todaysVerse)
print()
print(todaysVerse.getVerseInfo())
