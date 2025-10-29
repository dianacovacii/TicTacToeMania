# TicTacToe Mania -- McHacks 2023
A simple AI-powered Tic-Tac-Toe Game built with Pygame. 
This was my first hackathon project, created during McGill's annual hackathon McHacks in 2023 with a partner. This was my introduction to game development and Python's Pygame library.

## Overview
This project implements a fully playable Tic-Tac-Toe game where the player faces off agaisnt a computer opponent. The computer uses a set of heuristics to decide its next move (prioritizing winning, blocking, or takin strategic positions). 

--- 

### The game features: 
   - Interactive graphical interface made with Pygame
   - Basic AI logic
   - Simple and smooth gameplay
   - Clean 3x3 grid layout and visual X/O markers

### How to play: 
1. Run the Python script.
2. Click on a square to place your O.
3. The computer will automatically respond with X.
4. The game ends when either side wins or all sports are filled.

### Installation
1. Clone the repository:
   
   ```bash
   git clone https://github.com/dianacovacii/TicTacToeMania.git
   cd TicTacToeMania
   ```
   
2. Create and activate a virtual environment (optional):
   
   ```bash
   python -m venv venv
   ```

    **Windows:**
   ``` powershell
   .\venv\Scripts\Activate.ps1
   ```

    **Mac/Linux:**
   ```bash
   source venv/vin/activate
   ```
   
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   
4. Run the game

   ```bash
   pytjon TicTacToeMania.py
   ```

### Future Improvements: 
   - Improved AI using the Minimax algorithm
   - Background music or sound effects
   - Message on screen to report game outcome
   - Replay option at the end of the game


### License
This project is licensed under the [MIT License](LICENSE).
