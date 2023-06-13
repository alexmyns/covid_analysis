# Data analysis of [Covid data](https://ourworldindata.org/covid-deaths)

## Guide through the project
- [Description](#description)
- [Features](#features)
- [Dataset](#dataset)
- [Architecture](#architecture)
- [How To Use](#how-to-use)
- [Get in touch](#get-in-touch)

## Description
* COVID-19 Deaths Worldwide:
This dataset provides comprehensive information on COVID-19 deaths worldwide, presenting a detailed analysis of the number of deaths attributed to the virus across different countries and time periods.
* By offering data on COVID-19 deaths across multiple countries, this dataset facilitates a comparative analysis of mortality rates, enabling researchers to investigate disparities, evaluate healthcare systems' responses, and identify potential factors influencing outcomes.

## Features
- ⚡Data was scraped from the online web service with <b>BeautifulSoup4</b>
- ⚡<b>Python</b> for EDA, data exploration
- ⚡<b>SQLite</b> for data storage
- ⚡<b>Streamlit</b> for deploying and making cool website (with python)
- ⚡<b>Docker</b> is also used to creating images over the project 
- ⚡<b>PowerBI Desktop</b> for data visualisation (PowerQuery Editor [For data-transformation/data-modeling])
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

# How to use
1. `pip install -r requirements.txt` -  In this command, requirements.txt is the name of the file that contains a list of Python packages and their versions, each on a separate line. The -r flag tells pip to install the packages specified in the requirements file.

2. `streamlit run Home.py` - to run the local working website built on streamlit

3. Build the <b>Docker</b> Docker image: Open a terminal or command prompt, navigate to the directory containing the Dockerfile, and run the following command to build the Docker image: 
`docker build -t myapp .` 
This command builds a Docker image with the tag myapp. The . indicates that the Dockerfile is in the current directory.

4. Run the Docker container: After the image is built, you can run a Docker container based on that image. Use the following command: 
`docker run -p 8501:8501 --name mycontainer myapp`
This command creates and starts a container named mycontainer based on the myapp image. The -p 8501:8501 flag maps port 8501 from the container to port 8501 on the host, allowing you to access the Streamlit app in your browser at http://localhost:8501. If you need to specify a different port, adjust the port numbers accordingly in both the Dockerfile and the docker run command.

### Get in touch
| Email | Telegram |
|  ---    |    ----    |  
| alixan.me@yandex.com | t.me//alexmyns |