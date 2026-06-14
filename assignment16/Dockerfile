# Use a slim Python base image
FROM python:3.11-slim

# Install system dependencies and Java 21 (Required for modern Debian Trixie images)
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless \
    curl \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Environment Variables for Java 21
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Set Spark version and environment variables
ENV SPARK_VERSION=3.5.1
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# Download and install Apache Spark
RUN curl -O https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && tar -xvzf spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && mv spark-${SPARK_VERSION}-bin-hadoop3 ${SPARK_HOME} \
    && rm spark-${SPARK_VERSION}-bin-hadoop3.tgz

# Set PySpark Python path environment configurations
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# Establish working directory inside the container
WORKDIR /app

# Install PySpark Python library matching the Spark version
RUN pip install --no-cache-dir pyspark==${SPARK_VERSION}

# Copy application files and dataset into the container
COPY app.py /app/
COPY data/ /app/data/

# Create a volume destination to easily copy output files to host if needed
VOLUME [ "/app/output" ]

# Automatically run the application when container starts
CMD ["python", "app.py"]