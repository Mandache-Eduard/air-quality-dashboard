import pandas as pd

from pathlib import Path


DATA_COLUMNS = [
    "pm10_ug_m3",
    "pm25_ug_m3",
    "temp_c",
    "humidity",
]

TIMESTAMP_COLUMN = "timestamp"


def clean_input_path(path: str) -> Path:
    """
    Allows pasted paths with or without quotes.
    """
    return Path(path.strip().strip('"').strip("'"))


def calculate_missing_stats(df: pd.DataFrame) -> dict:
    total_rows = len(df)

    total_expected_sensor_cells = total_rows * len(DATA_COLUMNS)
    total_missing_sensor_cells = 0

    per_column_missing = {}

    for column in DATA_COLUMNS:
        if column in df.columns:
            missing_count = int(df[column].isna().sum())
        else:
            # If an expected column is absent, all rows are missing that value.
            missing_count = total_rows

        missing_pct = (
            missing_count / total_rows * 100
            if total_rows > 0 else 0
        )

        per_column_missing[column] = {
            "missing_count": missing_count,
            "missing_pct": missing_pct,
        }

        total_missing_sensor_cells += missing_count

    existing_sensor_columns = [
        column for column in DATA_COLUMNS
        if column in df.columns
    ]

    missing_expected_columns = [
        column for column in DATA_COLUMNS
        if column not in df.columns
    ]

    if existing_sensor_columns:
        rows_with_any_missing_sensor_value = int(
            df[existing_sensor_columns].isna().any(axis=1).sum()
        )
    else:
        rows_with_any_missing_sensor_value = total_rows

    # If at least one expected column is completely missing,
    # then every row is incomplete.
    if missing_expected_columns:
        rows_with_any_missing_sensor_value = total_rows

    missing_sensor_data_pct = (
        total_missing_sensor_cells / total_expected_sensor_cells * 100
        if total_expected_sensor_cells > 0 else 0
    )

    rows_with_any_missing_sensor_value_pct = (
        rows_with_any_missing_sensor_value / total_rows * 100
        if total_rows > 0 else 0
    )

    if TIMESTAMP_COLUMN in df.columns:
        missing_timestamps = int(df[TIMESTAMP_COLUMN].isna().sum())
    else:
        missing_timestamps = total_rows

    missing_timestamps_pct = (
        missing_timestamps / total_rows * 100
        if total_rows > 0 else 0
    )

    return {
        "total_rows": total_rows,
        "total_expected_sensor_cells": total_expected_sensor_cells,
        "total_missing_sensor_cells": total_missing_sensor_cells,
        "missing_sensor_data_pct": missing_sensor_data_pct,
        "rows_with_any_missing_sensor_value": rows_with_any_missing_sensor_value,
        "rows_with_any_missing_sensor_value_pct": rows_with_any_missing_sensor_value_pct,
        "missing_timestamps": missing_timestamps,
        "missing_timestamps_pct": missing_timestamps_pct,
        "per_column_missing": per_column_missing,
        "missing_expected_columns": missing_expected_columns,
    }


def print_file_report(parquet_file: Path):
    df = pd.read_parquet(parquet_file, engine="pyarrow")
    stats = calculate_missing_stats(df)

    print()
    print("=" * 70)
    print(f"Missing data report: {parquet_file.name}")
    print("=" * 70)

    print(f"Total rows: {stats['total_rows']}")

    print()
    print("Sensor-cell missingness:")
    print(f"  Expected sensor cells: {stats['total_expected_sensor_cells']}")
    print(f"  Missing sensor cells: {stats['total_missing_sensor_cells']}")
    print(f"  Missing sensor data %: {stats['missing_sensor_data_pct']:.2f}%")

    print()
    print("Rows affected:")
    print(
        "  Rows with at least one missing sensor value: "
        f"{stats['rows_with_any_missing_sensor_value']}"
    )
    print(
        "  Rows with at least one missing sensor value %: "
        f"{stats['rows_with_any_missing_sensor_value_pct']:.2f}%"
    )

    print()
    print("Timestamp missingness:")
    print(f"  Missing timestamps: {stats['missing_timestamps']}")
    print(f"  Missing timestamps %: {stats['missing_timestamps_pct']:.2f}%")

    print()
    print("Missingness by sensor column:")

    for column, column_stats in stats["per_column_missing"].items():
        print(
            f"  {column}: "
            f"{column_stats['missing_count']} missing "
            f"({column_stats['missing_pct']:.2f}%)"
        )

    if stats["missing_expected_columns"]:
        print()
        print("Warning: missing expected columns:")
        for column in stats["missing_expected_columns"]:
            print(f"  - {column}")

    print("=" * 70)
    print()


def get_parquet_files(folder: Path, recursive: bool = False) -> list[Path]:
    if recursive:
        return sorted(folder.rglob("*.parquet"))

    return sorted(folder.glob("*.parquet"))


def build_folder_report(folder: Path, recursive: bool = False) -> pd.DataFrame:
    parquet_files = get_parquet_files(folder, recursive=recursive)

    report_rows = []

    for parquet_file in parquet_files:
        df = pd.read_parquet(parquet_file, engine="pyarrow")
        stats = calculate_missing_stats(df)

        row = {
            "file": str(parquet_file),
            "file_name": parquet_file.name,
            "total_rows": stats["total_rows"],
            "expected_sensor_cells": stats["total_expected_sensor_cells"],
            "missing_sensor_cells": stats["total_missing_sensor_cells"],
            "missing_sensor_data_pct": stats["missing_sensor_data_pct"],
            "rows_with_any_missing_sensor_value": stats["rows_with_any_missing_sensor_value"],
            "rows_with_any_missing_sensor_value_pct": stats["rows_with_any_missing_sensor_value_pct"],
            "missing_timestamps": stats["missing_timestamps"],
            "missing_timestamps_pct": stats["missing_timestamps_pct"],
        }

        for column in DATA_COLUMNS:
            row[f"{column}_missing_count"] = stats["per_column_missing"][column]["missing_count"]
            row[f"{column}_missing_pct"] = stats["per_column_missing"][column]["missing_pct"]

        report_rows.append(row)

    return pd.DataFrame(report_rows)


def print_folder_report(folder: Path, recursive: bool = False):
    report_df = build_folder_report(folder, recursive=recursive)

    if report_df.empty:
        print()
        print(f"No .parquet files found in: {folder}")
        print()
        return

    print()
    print("#" * 70)
    print(f"Folder missing data report: {folder}")
    print("#" * 70)

    for _, row in report_df.iterrows():
        print(row["file_name"])
        print(f"  Rows: {row['total_rows']}")
        print(
            "  Missing sensor cells: "
            f"{row['missing_sensor_cells']}/{row['expected_sensor_cells']}"
        )
        print(f"  Missing sensor data %: {row['missing_sensor_data_pct']:.2f}%")
        print(
            "  Rows with at least one missing sensor value: "
            f"{row['rows_with_any_missing_sensor_value']}"
        )
        print(f"  Missing timestamps: {row['missing_timestamps']}")
        print()

    total_rows = int(report_df["total_rows"].sum())
    total_expected_sensor_cells = int(report_df["expected_sensor_cells"].sum())
    total_missing_sensor_cells = int(report_df["missing_sensor_cells"].sum())
    total_rows_with_any_missing_sensor_value = int(
        report_df["rows_with_any_missing_sensor_value"].sum()
    )
    total_missing_timestamps = int(report_df["missing_timestamps"].sum())

    overall_missing_sensor_data_pct = (
        total_missing_sensor_cells / total_expected_sensor_cells * 100
        if total_expected_sensor_cells > 0 else 0
    )

    overall_rows_with_any_missing_sensor_value_pct = (
        total_rows_with_any_missing_sensor_value / total_rows * 100
        if total_rows > 0 else 0
    )

    overall_missing_timestamps_pct = (
        total_missing_timestamps / total_rows * 100
        if total_rows > 0 else 0
    )

    print("OVERALL SUMMARY")
    print(f"Total parquet files: {len(report_df)}")
    print(f"Total rows: {total_rows}")
    print(f"Total expected sensor cells: {total_expected_sensor_cells}")
    print(f"Total missing sensor cells: {total_missing_sensor_cells}")
    print(f"Overall missing sensor data %: {overall_missing_sensor_data_pct:.2f}%")
    print(
        "Rows with at least one missing sensor value: "
        f"{total_rows_with_any_missing_sensor_value}"
    )
    print(
        "Rows with at least one missing sensor value %: "
        f"{overall_rows_with_any_missing_sensor_value_pct:.2f}%"
    )
    print(f"Missing timestamps: {total_missing_timestamps}")
    print(f"Missing timestamps %: {overall_missing_timestamps_pct:.2f}%")

    print()
    print("OVERALL MISSINGNESS BY SENSOR COLUMN")

    for column in DATA_COLUMNS:
        missing_count = int(report_df[f"{column}_missing_count"].sum())
        missing_pct = (
            missing_count / total_rows * 100
            if total_rows > 0 else 0
        )

        print(f"  {column}: {missing_count} missing ({missing_pct:.2f}%)")

    print("#" * 70)
    print()


def export_folder_report_to_csv(folder: Path, recursive: bool = False):
    report_df = build_folder_report(folder, recursive=recursive)

    if report_df.empty:
        print()
        print(f"No .parquet files found in: {folder}")
        print()
        return

    output_path = folder / "missing_data_report.csv"
    report_df.to_csv(output_path, index=False, encoding="utf-8")

    print()
    print(f"CSV report saved to: {output_path}")
    print()


def check_single_file():
    print()
    path = input("Insert path to .parquet file: ")
    parquet_file = clean_input_path(path)

    if not parquet_file.exists():
        print()
        print(f"File does not exist: {parquet_file}")
        print()
        return

    if parquet_file.suffix.lower() != ".parquet":
        print()
        print("Selected file is not a .parquet file.")
        print()
        return

    print_file_report(parquet_file)


def check_folder(recursive: bool = False):
    print()
    path = input("Insert path to folder containing .parquet files: ")
    folder = clean_input_path(path)

    if not folder.exists():
        print()
        print(f"Folder does not exist: {folder}")
        print()
        return

    if not folder.is_dir():
        print()
        print("Selected path is not a folder.")
        print()
        return

    print_folder_report(folder, recursive=recursive)


def export_folder_csv(recursive: bool = False):
    print()
    path = input("Insert path to folder containing .parquet files: ")
    folder = clean_input_path(path)

    if not folder.exists():
        print()
        print(f"Folder does not exist: {folder}")
        print()
        return

    if not folder.is_dir():
        print()
        print("Selected path is not a folder.")
        print()
        return

    export_folder_report_to_csv(folder, recursive=recursive)


def print_menu():
    print()
    print("Missing Data Checker")
    print("=" * 30)
    print("1. Check one .parquet file")
    print("2. Check all .parquet files in a folder")
    print("3. Check all .parquet files in a folder recursively")
    print("4. Export folder report to CSV")
    print("5. Export recursive folder report to CSV")
    print("0. Exit")
    print("=" * 30)


def main():
    while True:
        print_menu()
        option = input("Choose an option: ").strip()

        if option == "1":
            check_single_file()

        elif option == "2":
            check_folder(recursive=False)

        elif option == "3":
            check_folder(recursive=True)

        elif option == "4":
            export_folder_csv(recursive=False)

        elif option == "5":
            export_folder_csv(recursive=True)

        elif option == "0":
            print()
            print("Exiting.")
            break

        else:
            print()
            print("Invalid option. Please choose one of the listed options.")


if __name__ == "__main__":
    main()