# PySpark Sales Data Analysis Application

This repository contains a PySpark application that processes product sales data. It reads a dataset from a CSV file, performs data transformations, displays targeted insights, and exports the filtered results. The entire setup is containerized using Docker.

## Project Setup & Features
- **Data Ingestion:** Reads product sales records dynamically.
- **Sorting:** Orders products by sales revenue in descending order.
- **Top Analysis:** Isolates and displays the top 3 highest-performing products.
- **Filtering & Export:** Filters for high-value products (> 80,000) and saves the output in CSV format.
- **Dockerized Environment:** Bundles Java, Python, and PySpark for seamless deployment.

## How to Run Locally with Docker

1. **Build the Docker Image:**
   ```bash
   docker build -t pyspark-sales-app .