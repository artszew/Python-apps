import configparser

DEFAULT_COORDINATE_LIMIT = 10.0
DEFAULT_SHEEP_DISTANCE = 0.5
DEFAULT_WOLF_DISTANCE = 1.0

def load_config(file):
    config = configparser.ConfigParser()
    try:
        config.read(file)
        coord_limit = float(config.get("Sheep", "InitPosLimit", fallback=DEFAULT_COORDINATE_LIMIT))
        sheep_distance = float(config.get("Sheep", "MoveDist", fallback=DEFAULT_SHEEP_DISTANCE))
        wolf_distance = float(config.get("Wolf", "MoveDist", fallback=DEFAULT_WOLF_DISTANCE))

        # Validate values
        if coord_limit <= 0 or sheep_distance <= 0 or wolf_distance <= 0:
            raise ValueError("Config values must be positive numbers.")

        return coord_limit, sheep_distance, wolf_distance
    except Exception as e:
        print(f"Error loading config file: {e}")
        exit(1)
