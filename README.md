# SnakeQL: Q-learning Snake Game

This project implements a Q-learning agent to play the Snake game. It includes training the agent using Q-learning and visualizing the game with the trained agent. The project consists of the following files:

## Files Description

### main.py

The entry point for the project. It allows you to train the agent and visualize the game.

- `train_agent()`: Function to train the Q-learning agent.
- `visualize_game(episode)`: Function to visualize the game for a specific episode.

### snake_no_visual.py

Contains the `LearnSnake` class which implements the Snake game logic without visualization.

- `LearnSnake`: Class implementing the game logic.
- `get_state()`: Returns the current state of the game.
- `is_unsafe(r, c)`: Checks if the given cell is unsafe (wall or body).
- `generate_food()`: Randomly generates food on the board.
- `step(action)`: Updates the game state based on the action taken.
- `run_game(episode)`: Runs the game using a specific Q-table for a given episode.

### snakeql.py

Contains the `SnakeQAgent` class which implements the Q-learning algorithm.

- `SnakeQAgent`: Class implementing the Q-learning agent.
- `get_action(state)`: Returns the action to be taken based on the current state using epsilon-greedy policy.
- `train()`: Trains the Q-learning agent by playing multiple episodes of the Snake game.

### visualsnake.py

Contains the `VisualSnake` class which implements the Snake game logic with visualization using Pygame.

- `VisualSnake`: Class implementing the game logic with visualization.
- `print_score(score)`: Displays the current score on the screen.
- `print_episode()`: Displays the current episode number on the screen.
- `draw_snake()`: Draws the snake on the screen.
- `step(action)`: Updates the game state based on the action taken and updates the display.
- `run_game(episode)`: Runs the game with visualization using a specific Q-table for a given episode.

## Running the Project

### Train the Agent:

To train the Q-learning agent, run the following command:

```bash
python main.py --train
```

### Visualize the Game:

To visualize the game using a specific episode's Q-table, run the following command:

```bash
python main.py --visualize <episode_number>
```
Replace <episode_number> with the episode number of the Q-table you want to visualize (e.g., 500).
