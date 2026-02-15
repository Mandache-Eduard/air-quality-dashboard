import pandas as pd

from datetime import datetime
from pathlib import Path

PATH = '.\\raw_data\\2024_raw.txt'

MONTHS = {
    "ian.": 1,
    "feb.": 2,
    "mart.": 3,
    "apr.": 4,
    "mai": 5,
    "iun.": 6,
    "iul.": 7,
    "aug.": 8,
    "sept.": 9,
    "oct.": 10,
    "nov.": 11,
    "dec.": 12,
}

def parse_timestamp(ts: str, file_path: str) -> datetime:
    stem = Path(file_path).stem          # "2026_raw"
    year_str = stem.split("_", 1)[0]     # "2026"
    year = int(year_str)

    parts = ts.strip().split()           # ["31", "mart.,", "17:00"]
    day = int(parts[0])

    month_token = parts[1].replace(",", "")  # "mart.," -> "mart."
    month = MONTHS[month_token]

    hour = int(parts[2].split(":")[0])  # "17:00" -> ["17", "00"] -> 17

    return datetime(year, month, day, hour, 0)

def parse_pm(s: str) -> float:
    s = s.strip()
    if s == "-":
        return float("nan")
    return float(s.split()[0].replace(",", "."))

def parse_temp(s: str) -> float:
    s = s.strip()
    if s == "-":
        return float("nan")
    s = s.replace("Â", "").replace("°C", "").strip()
    return float(s.replace(",", "."))

def parse_humidity(s: str, decimals: int = 3) -> float:
    s = s.strip()
    if s == "-" or not s:
        return float("nan")

    value = float(s.replace("%", "").strip().replace(",", ".")) / 100.0
    value = round(value, decimals)
    return value if 0.0 <= value <= 1.0 else float("nan")

def save_to_parquet(df: pd.DataFrame, in_file_path: str):
    stem = Path(in_file_path).stem
    year_str = stem.split("_", 1)[0]
    year = int(year_str)

    out_dir = Path(".\\sanitized_data")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file_path = out_dir / f"{year}_sanitized.parquet"

    if out_file_path.exists():
        answer = input(
            f"File '{out_file_path.name}' already exists. Overwrite? (Y/N): "
        ).strip().upper()
        if answer != "Y":
            return None

    df.to_parquet(out_file_path, engine="pyarrow", index=False)
    return out_file_path

rows = []
buffer_row = []

with open(PATH, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        buffer_row.append(line)

        if len(buffer_row) == 5:

            row = {'timestamp': parse_timestamp(buffer_row[0], PATH),
                  'pm10_ug_m3': parse_pm(buffer_row[1]),
                  'pm25_ug_m3': parse_pm(buffer_row[2]),
                  'temp_c': parse_temp(buffer_row[3]),
                  'humidity': parse_humidity(buffer_row[4])
                  }

            rows.append(row)
            buffer_row.clear()

    if buffer_row:
        print("Warning: incomplete row at EOF:", buffer_row)

    rows = sorted(rows, key = lambda d: d['timestamp'], reverse = True)
    rows = pd.DataFrame(rows)

    parquet_file = save_to_parquet(rows, PATH)
    if parquet_file is None:
        print("Skipped writing parquet (user chose not to overwrite).")
        raise SystemExit

    df_check = pd.read_parquet(parquet_file, engine="pyarrow")
    print(df_check.dtypes)
    print(len(df_check))
    print(df_check.head(10))
