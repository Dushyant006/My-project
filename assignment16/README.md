# Dockerized PySpark Employee Data Processor

This repository contains a containerized PySpark application utilizing the Spark RDD (Resilient Distributed Dataset) API to process employee records.

## Features Performed via Spark RDD API:
1. **Sorting:** Sorts all employees dynamically by salary in descending order and prints to the console.
2. **Aggregations:** Groups employees by department to calculate and display cumulative salary distributions.
3. **Action & Storage:** Targets the top 3 highest-paid earners and outputs the metrics safely into a local directory ecosystem.

---

## Requirements
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on your machine.
* Git (to clone the tracking repository).

---

## Setup & Execution Guide

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd pyspark-employee-app