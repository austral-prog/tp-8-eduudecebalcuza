"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return coordinate[0], coordinate[1]


def create_record(azara_record, rui_record):
    azara_coordinate = azara_record[1]
    azara_separated = azara_coordinate[0], azara_coordinate[1]
    if azara_separated == rui_record[1]:
        return azara_record + rui_record
    else:
        return "not a match"
