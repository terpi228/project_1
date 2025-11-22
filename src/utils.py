import math
import pandas as pd
from typing import List, Dict, Any


def reader_exel(file: [Dict[str, Any]]) -> str:
    try:
        exel_data = pd.read_excel(file)
        return exel_data
    except FileNotFoundError:
        print(f"❌ Файл не найден: {file}")
        return None
    except Exception as e:
        print(f"❌ Ошибка чтения файла: {e}")
        return None


def round_to_next(val, step):
    result = math.ceil(val / step) * step
    return result


if __name__ == "__main__":
    pass
