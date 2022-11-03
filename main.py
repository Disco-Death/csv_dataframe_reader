from csv_dataframe_reader import read_csv_as_dataframes_dict


FILENAME = 'IlyaMono.txt'
COLUMN_LINE_NUM = 4
CSV_DELIMITER = ','
CSV_QUOTECHAR = '"'


if __name__ == '__main__':
    dataframes = read_csv_as_dataframes_dict(FILENAME, CSV_DELIMITER, CSV_QUOTECHAR, COLUMN_LINE_NUM)
    for dataframe in dataframes.items():
        print(dataframe[0], ':\n', dataframe[1], '\n', '-' * 50)