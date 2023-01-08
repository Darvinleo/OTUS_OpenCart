import csv
import pathlib
from config.definitions import ROOT_DIR


def data_logger(data, log_name) -> None:
    """Save test data in path with name.csv"""
    with open(f'{ROOT_DIR}/test_data/{log_name}.csv', 'a', encoding='UTF-8', newline='') as users:
        writer = csv.writer(users)
        writer.writerow(data.values())
