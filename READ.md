Data Pipeline Architecture

This repository outlines the architecture and implementation of a data pipeline using Azure Data Factory, Databricks, and Azure SQL Server. The pipeline is designed to efficiently load and process data from an MS SQL Server 2022 into Databricks Delta Tables, supporting both full and incremental data loads.

Overview

The architecture consists of the following components:

	•	MS SQL Server 2022: The source database from which the data is extracted.
	•	Azure Data Factory (ADF): Manages the data extraction, transformation, and loading (ETL) process. The following pipelines are configured in ADF:
	•	REST_API Pipeline: Extracts data from REST APIs and moves it into Azure SQL Server.
	•	Self-hosted Integration Runtime: Connects to the on-premise MS SQL Server 2022 to transfer data into Azure SQL Server.
	•	Azure SQL Server: A staging database where raw data from MS SQL Server and APIs is stored before further processing.
	•	Databricks: Performs transformations and loads the data into Delta Tables for further analysis or consumption. Two types of notebooks are used:
	•	Full_Load Notebook: Handles the complete load of data from Azure SQL Server into Databricks Delta Tables.
	•	Incremental_Load Notebook: Only loads the changed or new data from Azure SQL Server into the Delta Tables to ensure up-to-date information while minimizing processing time.

Data Flow

	1.	Data Extraction:
	•	Data from MS SQL Server 2022 is transferred to Azure SQL Server using the Self-hosted Integration Runtime in Azure Data Factory.
	•	Additionally, data from external REST APIs is ingested using the REST_API Pipeline.
	2.	Data Loading:
	•	Once the data is in Azure SQL Server, it is processed by Databricks.
	•	The Full_Load Notebook loads the entire dataset into Databricks Delta Tables.
	•	The Incremental_Load Notebook is used for ongoing updates by loading only the new or modified data into Delta Tables.

Components

Azure Data Factory

	•	Pipelines:
	•	REST_API Pipeline: Pulls data from external APIs and moves it to Azure SQL Server.
	•	Self-hosted Integration Runtime: Facilitates secure data transfer from on-premise SQL Server to Azure.

Azure SQL Server

	•	Serves as the intermediate storage for data extracted from both MS SQL Server and the REST API.

Databricks

	•	Full_Load Notebook: Performs a complete refresh of data from Azure SQL Server into Delta Tables.
	•	Incremental_Load Notebook: Updates only the changed records in Delta Tables to keep the data fresh and accurate.

Getting Started

Prerequisites

	•	Azure Subscription with permissions to create resources in Azure Data Factory, Azure SQL Server, and Databricks.
	•	Access to MS SQL Server 2022.
	•	Databricks Workspace with notebooks configured for data transformation.

Setup Instructions

	1.	Set up Azure Data Factory and configure the Self-hosted Integration Runtime to connect with the on-premise MS SQL Server 2022.
	2.	Configure the REST_API Pipeline in ADF to pull data from relevant APIs.
	3.	Set up an Azure SQL Server database to store the extracted data.
	4.	Deploy the Databricks Notebooks (Full_Load and Incremental_Load) in your Databricks Workspace.
	5.	Create Delta Tables in Databricks to store processed data for further use.

Contributing

If you’d like to contribute to the improvement of this pipeline, feel free to fork the repository and submit a pull request.