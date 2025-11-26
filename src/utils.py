import math
import pandas as pd
from typing import List, Dict, Any


def reader_exel(path: str):
    try:
        return pd.read_excel(path)
    except Exception as e:
        print(f"Ошибка чтения {path}: {e}")
        return None



def round_to_next(val, step):
    result = math.ceil(val / step) * step
    return result


if __name__ == "__main__":
    pass
