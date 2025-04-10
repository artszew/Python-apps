import random
import logging
from animals import Sheep, Wolf
from logger import save_to_json, save_to_csv
import time

def run_simulation(coord_limit, sheep_distance, wolf_distance, max_rounds, sheep_count, wait):
    logging.info(f"Simulation started with {sheep_count} sheep and {max_rounds} rounds.")

    # Initialization
    herd = [Sheep(random.uniform(-coord_limit, coord_limit), random.uniform(-coord_limit, coord_limit)) for _ in
            range(sheep_count)]
    wolf = Wolf(0, 0)

    data_for_json = []
    data_for_csv = []

    for round_number in range(1, max_rounds+1):
        if not any(sheep.status == 'alive' for sheep in herd):
            print("All sheep are dead! The wolf won.")
            logging.info("All sheep are dead! The wolf won.")
            break

        print(f"\nRound {round_number}:")
        logging.debug(f"Round {round_number} started.")

        # Sheep move
        for sheep in herd:
            if sheep.status == 'alive':
                sheep.distance = sheep_distance
                sheep.move()
                logging.debug(f"Sheep moved to ({sheep.x:.2f}, {sheep.y:.2f}).")

        # Wolf moves
        wolf.distance = wolf_distance
        nearest = wolf.nearest_sheep(herd)
        if nearest:
            print(f"The wolf is chasing the nearest sheep at ({nearest.x:.2f}, {nearest.y:.2f}).")
            logging.info(f"Wolf chasing sheep at ({nearest.x:.2f}, {nearest.y:.2f}).")
        wolf.move_towards(nearest)

        alive_sheep_count = sum(1 for sheep in herd if sheep.status == 'alive')
        print(f"Number of alive sheep: {alive_sheep_count}")

        # Collect data for saving
        round_data = {
            'round_no': round_number,
            'wolf_pos': [wolf.x, wolf.y],
            'sheep_pos': [[sheep.x, sheep.y] if sheep.status == 'alive' else None for sheep in herd]
        }
        data_for_json.append(round_data)
        data_for_csv.append([round_number, alive_sheep_count])

        if wait:
            input("Press Enter to continue...")

    else:
        print("50 rounds passed, the sheeps survived!")
        logging.info("50 rounds passed, the sheep survived!")

    # Save the simulation data to JSON and CSV
    save_to_json(data_for_json)
    save_to_csv(data_for_csv)
    logging.info("Simulation ended.")
