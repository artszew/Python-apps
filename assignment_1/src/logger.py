import logging
import json
import csv

def setup_logging(log_level):
    if log_level:
        logging.basicConfig(filename='../files/chase.log', level=getattr(logging, log_level),
                            format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')

def save_to_json(data):
    with open('../files/pos.json', 'w') as f:
        json.dump(data, f, indent=4)

def save_to_csv(data):
    with open('../files/alive.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Round', 'Alive Sheep'])
        writer.writerows(data)
