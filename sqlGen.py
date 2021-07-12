#!/usr/bin/python3

import json
import os
import os.path

DATAFILE = './lp1977-v4.json'
TID = "LP1977"


class Verse(object):
    def __init__(self, chapter, verseNumber, verseText):
        self.book = "PSAL"  # this is the Book objecfg
        self.chapter = chapter
        self.verseNumber = verseNumber
        self.verseText = verseText
        self.translation = TID

    def __str__(self):
        return f"{self.verseText} — {self.book} {self.chapter}:{self.verseNumber}"

    def sqlInsert(self):
        return f"""INSERT into verses(book_id, translation_short_name, verse_chapter, verse_number, verse_text) VALUES (19,'{self.translation}',{self.chapter},{self.verseNumber},\"{self.verseText.strip()}\");"""


class Chapter(object):
    def __init__(self, chapterNumber, chapterDesc):
        self.chapterNumber = chapterNumber
        self.chapterDesc = chapterDesc
        self.translation = TID
        self.book = "PSAL"

    def __str__(self):
        return f"{self.book} chapter {self.chapterNumber}: {self.chapterDesc}"

    def sqlInsert(self):
        return f"INSERT into ChapterMeta(chapter_number, book_key_name, translation_short_name, chapter_meta_value) VALUES ({self.chapterNumber}, '{self.book}', '{self.translation}', \"{self.chapterDesc}\");"


jsonData = json.load(open(DATAFILE))
# print(jsonData["version"])
# print(len(jsonData["chapters"]))


for c in jsonData["chapters"]:
    chapter = Chapter(c["psalm"], c["incipit"])
    print(chapter.sqlInsert())

verses = []

for c in jsonData["chapters"]:
    cNumber = c["psalm"]
    count = 1
    for v in c["verses"]:
        newVerse = Verse(cNumber, count, v.strip())
        verses.append(newVerse)
        count += 1

for v in verses:
    print(v.sqlInsert())
