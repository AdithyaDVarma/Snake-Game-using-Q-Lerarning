# SnakeQL: Q-learning Snake Game

This project implements a Q-learning agent to play the Snake game. It includes training the agent using Q-learning and visualizing the game with the trained agent. The project consists of the following files:

- `main.py`: Main script to train the Q-learning agent and visualize the game.
- `snake_no_visual.py`: Implements the Snake game logic without visualization.
- `snakeql.py`: Implements the Q-learning agent.
- `visualsnake.py`: Implements the Snake game logic with visualization using Pygame.

## Getting Started

### Prerequisites

Ensure you have Python installed along with the following packages:
- numpy
- pygame

You can install the required packages using:
```bash
pip install numpy pygame
```

## Files Description

### main.py

The entry point for the project. It allows you to train the agent and visualize the game.

- `train_agent()`: Function to train the Q-learning agent.
- `visualize_game(episode)`: Function to visualize the game for a specific episode.

