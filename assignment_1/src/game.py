import argparse
from config import load_config
from simulation import run_simulation
from logger import setup_logging

def parse_arguments():
    parser = argparse.ArgumentParser(description="Wolf and Sheep simulation.")
    parser.add_argument("-c", "--config", type=str, help="Path to configuration file.")
    parser.add_argument("-l", "--log", type=str, choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Set logging level.")
    parser.add_argument("-r", "--rounds", type=int, help="Maximum number of rounds.")
    parser.add_argument("-s", "--sheep", type=int, help="Number of sheep.")
    parser.add_argument("-w", "--wait", action="store_true", help="Pause after each round until a key is pressed.")
    return parser.parse_args()

args = parse_arguments()

# Load configuration if provided
coord_limit, sheep_distance, wolf_distance = load_config(args.config) if args.config else (
    10.0, 0.5, 1.0)  # Defaults if no config file

# Validate arguments
max_rounds = args.rounds if args.rounds and args.rounds > 0 else 50
sheep_count = args.sheep if args.sheep and args.sheep > 0 else 15

# Setup logging
setup_logging(args.log)

# Start the simulation
run_simulation(coord_limit, sheep_distance, wolf_distance, max_rounds, sheep_count, args.wait)