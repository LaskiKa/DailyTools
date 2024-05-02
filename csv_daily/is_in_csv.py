import csv


def search_variables(csv_file, variable):
    results = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            for cell in row:
                if variable in cell:
                    results.append(row)
                    # brake loop if founded
                    break
    return results


def main():
    filename = 'path/to/file/filename.csv'
    search_variable = 'searching variable'
    results = search_variables(filename, search_variable)

    if results:
        print("Founded variable:")
        for result in results:
            print(result)

    else:
        print("No results")


if __name__ == "__main__":
    main()
