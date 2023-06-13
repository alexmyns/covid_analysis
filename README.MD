# Data analysis of [Covid data](https://ourworldindata.org/covid-deaths)

## Guide through the project
- [Description](#description) 
- [Features](#features)
- [Dataset](#dataset)
- [Architecture](#architecture)
- [How To Use](#how-to-use)
- [License](#license)
- [Credits](#credits)
- [Get in touch](#get-in-touch)

## Description
* COVID-19 Deaths Worldwide:
This dataset provides comprehensive information on COVID-19 deaths worldwide, presenting a detailed analysis of the number of deaths attributed to the virus across different countries and time periods.
* By offering data on COVID-19 deaths across multiple countries, this dataset facilitates a comparative analysis of mortality rates, enabling researchers to investigate disparities, evaluate healthcare systems' responses, and identify potential factors influencing outcomes.
*This dataset provides a longitudinal perspective on COVID-19 deaths, enabling the examination of changes and developments in mortality rates over time. It allows researchers to track the progression of the pandemic and evaluate the effectiveness of mitigation strategies.
*With a country-level breakdown and temporal information, this dataset presents a comprehensive analysis of COVID-19 deaths, allowing for the exploration of patterns, trends, and variations in fatality rates across different nations over time.
*This dataset offers a comprehensive view of COVID-19 mortality rates worldwide, encompassing data on the number of deaths resulting from the virus and providing insights into the global impact of the pandemic.

## Features
- ⚡Python for EDA, data exploration
- ⚡SQL for data storage, SQLAlchemy is also used
- ⚡PowerBI Desktop
- ⚡PowerQuery Editor [For data-transformation/data-modeling]  
- ⚡PowerBI Service [For making the report accessible on the web without PowerBI login]  
- ⚡Multipage fully Interactive Report [For drawing insights and analysis] 

## Architecture

1. High-Level Overview:
   The project aims to analyze and visualize COVID-19 mortality data using SQL, Python, and Power BI. The architecture involves extracting data from external sources, processing it with Python, storing it in a SQL database, and creating interactive dashboards in Power BI to present the insights.

2. Data Flow:
   The data flow begins with extracting COVID-19 mortality data from reliable sources, such as the World Health Organization or government databases. Python scripts are then used to preprocess and transform the raw data, performing tasks like cleaning, aggregating, and feature engineering. The processed data is stored in a SQL database, enabling efficient querying and retrieval. Power BI connects to the SQL database to fetch the data and generate interactive visualizations and dashboards.

3. SQL Component:
   The project utilizes a SQL database to store the COVID-19 mortality data. The database consists of tables that capture relevant information, such as country-wise deaths, date/time, demographic details, and additional variables of interest. SQL queries are executed to retrieve specific data subsets required for analysis and visualization.

4. Python Component:
   Python plays a crucial role in data preprocessing, analysis, and feature engineering. Python libraries like Pandas, NumPy, and Scikit-learn are used to clean the data, handle missing values, perform statistical calculations, and apply machine learning algorithms for further insights. Python scripts interact with the SQL database using appropriate connectors or ORM libraries to retrieve and store data.

5. Power BI Component:
   Power BI is used to create visually appealing and interactive dashboards for COVID-19 mortality analysis. It connects to the SQL database and fetches the relevant data using appropriate queries. Power BI's data modeling capabilities enable the creation of relationships between different tables, ensuring data integrity. Visualizations such as line charts, heatmaps, and maps are created to depict trends, regional patterns, and comparisons. Filters and slicers are applied to allow users to explore the data interactively.

6. Integration and Communication:
   Python interacts with the SQL database using a suitable database connector, such as pyodbc or SQLAlchemy, to fetch and store data. Data processed and transformed by Python is then inserted into the SQL database for storage. Power BI connects to the SQL database using a compatible connector, such as ODBC or SQL Server connector, to retrieve data for visualization.

7. Scalability and Performance Considerations:
   To ensure scalability and performance, the SQL database is designed with appropriate indexes and optimized query structures. Batch processing techniques can be implemented in Python to handle large datasets efficiently. Additionally, Power BI's performance optimization features, such as query folding and data modeling optimizations, can be utilized for faster data retrieval and visualization.

