# main.py

import argparse
from snakeql import SnakeQAgent
from visualsnake import VisualSnake

def train_agent():
    agent = SnakeQAgent()
    agent.train()
    print("Training complete!")

def visualize_game(episode):
    game = VisualSnake()
    game.run_game(episode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train and visualize a Q-learning agent for Snake game.")
    parser.add_argument("--train", action="store_true", help="Train the Q-learning agent.")
    parser.add_argument("--visualize", type=int, help="Visualize the trained agent for the given episode.")

    args = parser.parse_args()

    if args.train:
        train_agent()
    if args.visualize is not None:
        visualize_game(args.visualize)
