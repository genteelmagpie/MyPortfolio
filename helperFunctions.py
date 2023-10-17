from os.path import exists
import csv

pathToDatabase = "database/database.csv"


def writeToCSV(data):
    """Appends data to a CSV file without duplicates.

    Args:
        data: A dictionary containing the data to be appended to the CSV file. The keys in the dictionary should be the same as the header names.

    Returns:
        None
    """
    try:

        # Create the CSV file if it does not exist.
        if not exists(pathToDatabase):
            with open(pathToDatabase, mode='w', encoding='utf-8', errors='ignore') as db:
                csvWriter = csv.writer(db, delimiter=',', lineterminator='\n')
                csvWriter.writerow(['Name', 'Email', 'Subject', 'Message'])

        # Open the CSV file in read mode.
        with open(pathToDatabase, mode='r', encoding='utf-8', errors='ignore') as db:
            csvReader = csv.reader(db, delimiter=',', lineterminator='\n')
            existing_data = set([tuple(row) for row in csvReader])

        # Open the CSV file in append mode.
        with open(pathToDatabase, mode='a+', encoding='utf-8', errors='ignore') as db:
            csvWriter = csv.writer(db, delimiter=',', lineterminator='\n')

            # Check if the data is already present in the CSV file. If not, append it.
            if tuple(data.values()) not in existing_data:
                csvWriter.writerow(
                    [data['name'], data['email'], data['subject'], data['message']])
                return 1
            else:
                return -1

    except Exception as e:
        print(e)
        return 0
