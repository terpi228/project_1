import pandas as pd


def reader_exel(file):

    try:
        exel_data = pd.read_excel(file, engine='xlrd')
        return exel_data
    except FileNotFoundError:
        return "File Not found"


# if __name__ == "__main__":
#     i = reader_exel('../data/TData.xls')
#     print(i.head(2))
#     print("Колонки:", i.columns.tolist())
#     print(i.iloc[0])