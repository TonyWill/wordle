# Wordle! Solver

This is a python web app which will help with solving the Wordle word puzzle game on android.

## Wordle!

The Wordle game is a game where you have six tries to guess a five letter word. You guess by entering a word and the game will highlight any letters that are in the secret word yellow if they are in the wrong position, green if the right letter is in the right position anf gray if the letter is not in the secret word. You keep guessing until you reach six tries or you find the secret word. You get a point for each turn you have left and one point for getting the correct word.

## The Plan

First I will create a sqlite database with a table with a comprehensive list of five letter words, their definition, the count of how many times the word was used in a game and a boolean value for whether or not the game lists this word as one in its internal dictionary.

Next I will create a web app which uses this database to list out possible words for the current game. After each guess a counter will tell you how many tries you have left and the word list will get smaller as I add the hint information I receive from guessing a word in the game.

## The UI

There will be a section for adding a new word to our dictionary and the main game section.

### Main

The main screen will have two columns. On the left are six rows of five boxes, one for each letter in the secret word. These boxes will allow for one letter to be placed in them each and when clicked once the letter changes to yellow, two clicks changes the letter to green and three clicks changes the letter back to the default black color.

Below these boxes is a New Game button which removes all text from the boxes and filters from the word list detailed below.

In the right column will be a list of possible words. Each time a word is guessed in a box and hints are entered as to which letters are present in the secret word the right column list will filter out impossible results.

### Dictionary

This page will allow the addition and removal of words from the dictionary database. It has an add button which allows for the entry of a new word and its definition and it must be a word that was in Wordle's dictionary.
