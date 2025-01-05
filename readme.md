# Terminal-Based Tic-Tac-Toe Game

## Overview

This is a terminal-based Tic-Tac-Toe game where players can enjoy two different modes:

1. **Two-Player Mode**: Two players take turns playing on the same terminal.
2. **Single-Player Mode**: A user can play against an AI opponent that uses the Minimax algorithm.

---

## Features

- **Game Modes**:
  - Two-Player Mode.
  - Single-Player Mode with AI.
- **Board Display**:
  - Shows the board after every move.
  - Uses color-coded symbols (`X` and `O`) for better readability.
- **Input Validation**:
  - Ensures valid moves within bounds and on empty cells.
- **Game Results**:
  - Detects and announces wins, losses, or draws.
- **AI Opponent**:
  - Makes optimal moves using the Minimax algorithm.

---

## Installation and Setup

### Prerequisites

- Python 3.8 or higher.
- `colorama` library for colored output.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/pushkalkishore/gameberry-assignment
   ```

2. Navigate to the project directory:

   ```bash
   cd tic-tac-toe
   ```

3. Install dependencies:

   ```bash
   pip install colorama
   ```

4. Run the game:
   ```bash
   python tic_tac_toe.py
   ```

---

## How to Play

1. Choose a game mode:
   - Enter `1` for Two-Player Mode.
   - Enter `2` for Single-Player Mode.
2. Make your moves:
   - Input row and column numbers (e.g., `1 1` for the top-left corner).
   - Moves are validated, and the board updates after each turn.
3. Play until the game ends with a win, loss, or draw.

---

## Notes

- The AI uses the Minimax algorithm to make strategic decisions.
- The game announces results clearly and provides error messages for invalid inputs.

---

Enjoy playing Tic-Tac-Toe in your terminal!
