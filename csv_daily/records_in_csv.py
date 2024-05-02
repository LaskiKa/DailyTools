import pandas as pd


def count_records_in_csv(csv_file):
    try:
        # Load csv file to DataFrame
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        return print("No such file or directory", FileNotFoundError)

    # count records in csv file
    num_of_records = df.shape[0]
    return num_of_records

def main():
    csv_file = input("Add path to file: ")
    result = count_records_in_csv(csv_file)
    print(f"Numer of records in CSV {csv_file} is {result}")

if __name__ == "__main__":
    main()