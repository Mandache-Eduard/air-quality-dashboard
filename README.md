<h3 align="center">Local Air Quality Dashboard</h3>

___

  <p align="center">
    A Python data filtering script and Power BI dashboard that help analyze and visualize recent local air quality and weather humidity trends.
  </p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#to-do">To-Do</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project combines a script written in [![Python][Python-shield]][Python-url] with a Power BI dashboard to explore local air quality data pulled from 2025. The script takes raw `.txt` files containing measurements and converts them into `.parquet` format, making the data easier to load and analyze in [![Power BI][PowerBI-shield]][PowerBI-url]. The dataset includes PM10, PM2.5, temperature, and humidity values.

The project has two main parts:

* a Python component that prepares and restructures the raw data, and
* a Power BI dashboard that visualizes trends and patterns over time.

It is built as a portfolio project to demonstrate practical work with real environmental data, from basic data transformation to interactive reporting. The original data source, along with the one currently used, are both listed in the <a href="#acknowledgments">Acknowledgments</a> section.

### How did I choose the topic?

* I wanted the topic to be local, in the city where I am currently studying.
* I wanted to work with real, flawed data rather than algorithmically generated datasets that I could create on my own or get from Kaggle.

### How did I search for data?

* At first, I tried OpenAQ, but I ran into several issues:
  * limited API call rates;
  * too much missing or corrupted data;
  * a limited number of nodes.
* I ended up using airdata.ro and settled only on 2025 data, because the 2024 data from certain nodes had approximately one third of the information missing.
* Compared with OpenAQ, airdata.ro had several advantages:
  * more consistent data;
  * a higher number of nodes;
  * clear details about the methodology and technologies used.
* The main disadvantages of airdata.ro were:
  * limited data about pollutants;
  * lack of an API.

### How did I choose the node locations?

* There should not be two locations in the same area or neighborhood.
* Locations should not be on private property.
* Locations should not be in surrounding localities, such as Ghiroda, Chișoda, Giroc, or Dumbrăvița.

#### Zone division

**Ultracentral**

* 33-P-ta Sf Gheorghe

**Central**

* 07-St. Gh. Lazar
* 09-Pasajul Jiul
* 11-Bd. Vasile Parvan
* 04-Bd. Take Ionescu
* 12-St. Divizia 9 Cavalerie

**Suburbs**

* 114-Calea Buziasului_AEM
* 02-Bd. L. Rebreanu
* 120-Dorobantilor
* 152-C.Aradului/G.T.Popa
* 116-Str. Closca

### How complete is the selected data?

After converting the raw data to Parquet format, I checked it missing values.

Across the 11 selected Parquet files, the dataset contains:

* 96,349 timestamped records;
* 385,396 expected sensor measurements;
* 14,213 missing sensor measurements;
* an overall missing data rate of 3.69% at measurement-level;
* 6,609 records with at least one missing sensor measurement, representing 6.86% missing data rate at row-level.;

The missing values are not evenly distributed across the measured attributes:

| Attribute | Missing values | Missing percentage |
|---|---:|---:|
| PM10 | 1,765 | 1.83% |
| PM2.5 | 1,766 | 1.83% |
| Temperature | 4,074 | 4.23% |
| Humidity | 6,608 | 6.86% |

I chose to measure data completeness at the individual sensor measurement level rather than at the full-row level. This is because many records are only partially incomplete. For example, a row may be missing humidity while still containing valid PM10, PM2.5, temperature, and timestamp values.

The full data integrity report is available here: [DATA_INTEGRITY.md](DATA_INTEGRITY.md).

___

<!-- TO-DO -->
## To-Do
- Expand to dataset to multiple years/locations for more conclusive results
- Rewrite the script to:
  - omit temperature and humidity values;
  - include more data nodes.
- Add overview/dashboard on first page.
- Create a mobile-friendly report format.

### Done

~~- Finished the report in desktop format. ~~
~~- Included a PDF version for easier access and visualization. ~~

___

<!-- REQUIREMENTS -->
## Requirements

- Python 3.6 (to run the data cleaning script)
- Power BI (to visualize the dashboard)
- Any PDF viewer (to open the PDF version of the report)

___

<!-- INSTALLATION -->
## Installation

To run it locally:

1. Clone the repository
   ```sh
   git clone https://github.com/Mandache-Eduard/air-quality-dashboard.git
    ```
3. Run the program using Python

   ```sh
   python main.py <path-to-flac-file-or-folder>
   ```
___

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0-only. See `LICENSE` or click the link below for more information.
<br>
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

___

<!-- CONTACT -->
## Contact

Mandache Eduard
<br>
[![LinkedIn][LinkedIn-shield]][LinkedIn-url]
<br>
![Outlook](https://img.shields.io/badge/Email-Outlook-0078D4?logo=microsoft-outlook&logoColor=white)
<br>
Project Link: [https://github.com/Mandache-Eduard/flac-authenticator](https://github.com/Mandache-Eduard/flac-authenticator)

___

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Choose an Open Source License](https://choosealicense.com)
* [Airdata](https://airdata.ro/map) - this is the currently used data source of this project
* [OpenAQ](https://openaq.org/) - this is the originally used data source of this project

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[License-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[License-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[LinkedIn-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[LinkedIn-url]: https://linkedin.com/in/linkedin_username](https://www.linkedin.com/in/eduard-mandache-89588035b/
[Python-shield]: https://img.shields.io/badge/Python-3.6-blue
[Python-url]: https://www.python.org/
[PowerBI-shield]: https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi&logoColor=black
[PowerBI-url]: https://powerbi.microsoft.com/
