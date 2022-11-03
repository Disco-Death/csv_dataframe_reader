from csv import reader
from pandas import DataFrame


def read_csv(filename: str, delimiter: str, quotechar: str, column_line_num: int) -> tuple:
    ONLY_READ = 'r'
    with open(filename, ONLY_READ) as dest_file:
        all_data = [data for data in reader(dest_file, delimiter = delimiter, quotechar = quotechar)]
        return (all_data[column_line_num + 1:], all_data[column_line_num])


def transpose_list_of_list(l: list):
    return list(map(list, zip(*l)))


def csv_data_array_to_dataframe(table_data: list, column_names: list) -> DataFrame:
    return DataFrame(data=dict(zip(column_names, transpose_list_of_list(table_data))))


def dataframe_to_dataframes_dict(dataframe: list, column_names: list) -> dict:
    result = {}
    for column_name in column_names:
        result[column_name] = dataframe[[column_name]]
    return result


def csv_data_array_to_dataframes_dict(table_data: list, column_names: list) -> dict:
    return dataframe_to_dataframes_dict(csv_data_array_to_dataframe(table_data, column_names), column_names)


def read_csv_as_dataframes_dict(filename: str, delimiter: str, quotechar: str, column_line_num: int) -> dict:
    data_array, column_names = read_csv(filename, delimiter, quotechar, column_line_num)
    return csv_data_array_to_dataframes_dict(data_array, column_names)