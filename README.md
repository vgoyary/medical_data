# Medical Data Analysis Project

This project involves converting and analyzing medical data, starting from a JSON format, and includes steps to filter and process the data, culminating in the generation of a CSV file with user input.
## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Processing Workflow](#workflow)

## Introduction

This project begins with a `train.json` file containing medical data, which is converted into an Excel file for easier manipulation and analysis. The data is analyzed and filtered to create a refined dataset. The final output is a CSV file containing 200 records from 11 different topics, all of which have a choice type of "single". An additional column capturing user input for the answers was also added to the dataset.
## Features

- Conversion: Converts JSON data into an Excel format for better accessibility.
- Data Filtering: Filters the data to create a focused dataset of 200 records covering 11 topics.
- User Input Capture: Adds a new column to the dataset for capturing user-provided answers.
## Installation

Provide step-by-step instructions to get the development environment set up. For example:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repository-name.git

2. Install dependencies:
    ```bash
   pip install -r requirements.txt
   
## Usage

1. Convert JSON to Excel:

   - Use Pandas to load the `train.json` file and convert it to an Excel file for further processing.
2. Data Analysis:

    - Perform data analysis in Jupyter Notebook, filtering the dataset down to 200 records from 11 topics with a choice type of "single".
3. Add User Input:

   - Create a new CSV file where an additional column records the answers provided by users.
   
    Example usage in Python:
    ```bash
    import pandas as pd
    # Load the JSON file
    data = pd.read_json('train.json')
    # Filter and process the data
    filtered_data = data[data['choice_type'] == 'single'].sample(200)
    # Save to CSV
    filtered_data.to_csv('filtered_data.csv', index=False)


## Data Processing Workflow
1. Step 1: Convert `train.json` to Excel using Pandas.
2. Step 2: Perform data analysis in a Jupyter Notebook to filter the data to 200 entries.
3. Step 3: Create a CSV file containing these 200 records.
4. Step 4: Add a new column for user input answers and save the final dataset as a CSV file.
