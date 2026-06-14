import os
import shutil
from pyspark import SparkConf, SparkContext

def parse_csv(line):
    # Splits CSV line and parses types: (id, name, department, salary)
    parts = line.split(',')
    return int(parts[0]), parts[1], parts[2], float(parts[3])

def main():
    # Configure Spark Context
    conf = SparkConf().setAppName("EmployeeDataProcessing").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    
    # Minimize verbose logging in console
    sc.setLogLevel("ERROR")

    csv_path = "data/employees.csv"
    output_dir = "output/top_three_paid"

    # Clean output directory if it exists to prevent PySpark FileExistsError
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # 1. Read CSV into RDD
    raw_rdd = sc.textFile(csv_path)
    
    # Extract header and filter it out
    header = raw_rdd.first()
    data_rdd = raw_rdd.filter(lambda line: line != header).map(parse_csv)
    
    # Cache because we are performing multiple actions on this parsed data
    data_rdd.cache()

    print("\n" + "="*50)
    print("OPERATIONS & OUTPUTS")
    print("="*50)

    # --- Task 1: Sort all employees by salary in descending order ---
    print("\n--- Employees Sorted by Salary (Descending) ---")
    # key for sorting is salary (index 3)
    sorted_by_salary = data_rdd.sortBy(lambda emp: emp[3], ascending=False)
    for emp in sorted_by_salary.collect():
        print(f"ID: {emp[0]}, Name: {emp[1]}, Dept: {emp[2]}, Salary: ${emp[3]:,.2f}")

    # --- Task 2: Calculate total salary paid in each department ---
    print("\n--- Total Salary by Department ---")
    # Map to (department, salary) -> Reduce by department key
    dept_salary_rdd = data_rdd.map(lambda emp: (emp[2], emp[3])) \
                              .reduceByKey(lambda a, b: a + b)
    
    for dept, total in dept_salary_rdd.collect():
        print(f"Department: {dept:10} | Total Salary: ${total:,.2f}")

    # --- Task 3: Identify the top 3 highest-paid employees and save to file ---
    print("\n--- Saving Top 3 Highest-Paid Employees to File... ---")
    # Take top 3 based on salary
    top_three = sorted_by_salary.take(3)
    
    # Convert the local Python list back to an RDD to save it via Spark
    top_three_rdd = sc.parallelize(top_three)
    
    # Map to a clean string format before saving
    top_three_rdd.map(lambda emp: f"{emp[0]},{emp[1]},{emp[2]},{emp[3]}") \
                 .saveAsTextFile(output_dir)
                 
    print(f"Successfully saved to: {output_dir}/")
    print("="*50 + "\n")

    sc.stop()

if __name__ == "__main__":
    main()