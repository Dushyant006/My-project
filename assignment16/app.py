import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("SalesDataAnalysis") \
        .master("local[*]") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("ERROR")
    print("Spark Session Started Successfully.\n")

    # Define paths
    input_path = "data/sales.csv"
    output_path = "output/high_sales_products"

    # 1. Read the CSV file into a DataFrame
    df = spark.read.csv(input_path, header=True, inferSchema=True)
    print("--- Original Dataset ---")
    df.show()

    # 2. Sort all products by sales in descending order and display
    print("--- Products Sorted by Sales (Descending) ---")
    sorted_df = df.orderBy(col("sales").desc())
    sorted_df.show()

    # 3. Display the top 3 products with the highest sales values
    print("--- Top 3 Products with Highest Sales ---")
    top_3_df = sorted_df.limit(3)
    top_3_df.show()

    # 4. Filter products with sales greater than 80,000
    print("--- Filtering Products with Sales > 80,000 ---")
    filtered_df = df.filter(col("sales") > 80000)
    filtered_df.show()

    # 5. Save the output as a CSV file
    print(f"Saving filtered results to: {output_path}")
    filtered_df.coalesce(1).write.csv(output_path, header=True, mode="overwrite")
    print("File saved successfully.")

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()