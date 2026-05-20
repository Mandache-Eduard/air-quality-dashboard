# Data Integrity Report

This report summarizes the completeness of the selected 2025 air quality dataset after conversion to Parquet format.

The report measures missing data at the **individual sensor measurement level**, not at the full-record level. This means that if a timestamped record is missing only one value, such as humidity, the remaining valid measurements in that record are still counted as usable data.

## Dataset Summary

| Metric | Value |
|---|---:|
| Parquet files analyzed | 11 |
| Total timestamped records | 96,349 |
| Expected sensor measurements | 385,396 |
| Missing sensor measurements | 14,213 |
| Overall missing data rate | 3.69% |
| Records with at least one missing sensor value | 6,609 |
| Records with at least one missing sensor value | 6.86% |

## Missing Data by Sensor Attribute

| Attribute | Missing values | Missing percentage |
|---|---:|---:|
| PM10 | 1,765 | 1.83% |
| PM2.5 | 1,766 | 1.83% |
| Temperature | 4,074 | 4.23% |
| Humidity | 6,608 | 6.86% |

## Missing Data by File

| File | Records | Missing sensor measurements | Expected sensor measurements | Missing data rate | Records with at least one missing sensor value |
|---|---:|---:|---:|---:|---:|
| `02-Bulevardul_Liviu_Rebreanu_2025_sanitized.parquet` | 8,759 | 950 | 35,036 | 2.71% | 238 |
| `04-Bulevardul_Take_Ionescu_2025_sanitized.parquet` | 8,759 | 0 | 35,036 | 0.00% | 0 |
| `07-Strada_Gheorghe_Lazar_2025_sanitized.parquet` | 8,759 | 2,416 | 35,036 | 6.90% | 1,174 |
| `09-Pasajul_Jiul_2025_sanitized.parquet` | 8,759 | 160 | 35,036 | 0.46% | 40 |
| `11-Bulevardul_Vasile_Parvan_2025_sanitized.parquet` | 8,759 | 792 | 35,036 | 2.26% | 198 |
| `114_Calea_Buziasului_AEM_2025_sanitized.parquet` | 8,759 | 1,331 | 35,036 | 3.80% | 962 |
| `116-Strada_Closca_2025_sanitized.parquet` | 8,759 | 364 | 35,036 | 1.04% | 91 |
| `12-Strada_Divizia_9_Cavalerie_2025_sanitized.parquet` | 8,759 | 2,348 | 35,036 | 6.70% | 1,171 |
| `120-Dorobantilor_2025_sanitized.parquet` | 8,759 | 2,176 | 35,036 | 6.21% | 544 |
| `152-Calea_Aradului_G_T_Popa_2025_sanitized.parquet` | 8,759 | 1,964 | 35,036 | 5.61% | 1,763 |
| `33-Piata_Sf_Gheorghe_2025_sanitized.parquet` | 8,759 | 1,712 | 35,036 | 4.89% | 428 |

## Notes

Each file contains 8,759 timestamped records and 35,036 expected sensor measurements.

The expected number of sensor measurements per file is calculated as:

```text
8,759 records × 4 sensor attributes = 35,036 expected sensor measurements