# golf-solitaire

 ## Description
This is a Python implementation of the classic card game, Golf Solitaire. The game is designed to be played in a text-based format within the console.

## How to Play
1. Run the `golf_solitaire.py` script using Python:
python golf_solitaire.py
2. Follow the on-screen instructions to play the game. You'll be able to select cards from the tableau and attempt to form pairs until no more moves are possible.

## Features
- Interactive text-based interface for playing Golf Solitaire.
- Scoring system to track your performance.
- Rules enforced to ensure a fair game.

## Gameplay Rules
- The goal is to remove all the cards from the tableau.
- Cards can be removed if they form pairs with the same rank or are adjacent in value to each other.
- You can draw cards from the deck or pick cards from the tableau.
- The game ends when you successfully clear the tableau or when there are no more moves left.

## Implementation Details
- The game is built using Python.
- It uses a deck of cards to initialize the tableau.
- The waste pile is used to store cards drawn from the deck.
- The program enforces the game rules and ensures a valid move.
