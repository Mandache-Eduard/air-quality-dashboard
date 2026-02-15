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
    <li><a href="#Demo">Demo</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project combines a script written in [![Python][Python-shield]][Python-url] with a Power BI dashboard to explore local air quality data from the past two years. The script takes raw `.txt` files containing measurements and converts them into `.parquet` format, making the data easier to load and analyze in [![Power BI][PowerBI-shield]][PowerBI-url]. The dataset includes PM10, PM2.5, temperature, and humidity values.

The project has two main parts:

* a Python component that prepares and restructures the raw data, and
* a Power BI dashboard that visualizes trends and patterns over time.

It is built as a portfolio project to demonstrate practical work with real environmental data, from basic data transformation to interactive reporting. The original data source is listed in the <a href="#acknowledgments">Acknowledgments</a> section.

___

<!-- DEMO EXAMPLES -->
## Demo

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

___

<!-- REQUIREMENTS -->
## Requirements

Python version: 3.6 (to run the data cleaning script)

Power BI (to visualize the dashboard)

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
* [Airdata](https://airdata.ro/map) - this is the source of the data used in this project

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
