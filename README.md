# Data Cleaning Automation Tool

## Overview

Data Cleaning Automation Tool is a web-based application developed using Streamlit that simplifies the process of cleaning and preparing datasets for analysis. The application allows users to upload CSV files and automatically perform common data preprocessing operations such as handling missing values, removing duplicate records, detecting outliers, and exporting cleaned datasets.

The project is designed for students, data analysts, and machine learning practitioners who want to reduce the time spent on manual data cleaning and improve overall data quality before analysis or model development.

## Features

### CSV File Upload

Users can upload CSV datasets directly through the application interface for processing.

### Dataset Preview

The uploaded dataset can be viewed before cleaning to inspect its structure and contents.

### Missing Value Handling

The application automatically detects missing values and fills numerical columns using mean imputation.

### Duplicate Removal

Duplicate records are identified and removed to ensure data consistency and accuracy.

### Outlier Detection and Removal

Outliers are detected using the Z-Score statistical method and removed from the dataset to improve data quality.

### Download Cleaned Dataset

After processing, users can download the cleaned dataset in CSV format for further analysis or machine learning tasks.

## Technology Stack

* Python
* Streamlit
* Pandas
* NumPy
* SciPy

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/data-cleaning-automation-tool.git
cd data-cleaning-automation-tool
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Usage

1. Launch the application.
2. Upload a CSV file.
3. Review the dataset preview.
4. Apply automated cleaning operations.
5. Download the cleaned CSV file.

## How It Works

The application follows a simple workflow:

1. Upload a dataset in CSV format.
2. Detect and remove duplicate records.
3. Identify missing values and replace them using mean imputation.
4. Detect outliers using the Z-Score method.
5. Remove identified outliers.
6. Generate a cleaned dataset.
7. Allow users to download the processed file.

## Use Cases

* Data preprocessing for machine learning projects
* Data analytics and visualization preparation
* Academic and research projects
* Business intelligence workflows
* Portfolio and learning projects

## Future Enhancements

* Support for Excel and JSON files
* Multiple missing value handling techniques
* Interactive data visualization
* Feature scaling and normalization
* Automated data quality reports
* Customizable cleaning options

## Author

Ajay D. Waghmare

B.Tech Computer Science and Engineering

Java Full Stack Developer | Data Analytics Enthusiast | AI Developer
