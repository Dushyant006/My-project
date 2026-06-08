USE data_bank;

SELECT COUNT(DISTINCT node_id) AS unique_node_count FROM customer_nodes;

SELECT region_id,COUNT(DISTINCT node_id) AS unique_node_count FROM customer_nodes GROUP BY region_id ORDER BY region_id;

SELECT region_id,COUNT(DISTINCT customer_id) AS unique_customer_count FROM customer_nodes GROUP BY region_id ORDER BY region_id;

SELECT
    ROUND(
        AVG(DATEDIFF(day, start_date, end_date) * 1.0),
        0
    ) AS avg_reallocation_days
FROM customer_nodes
WHERE end_date <> '9999-12-31';

WITH node_days AS
(
    SELECT
        r.region_name,
        DATEDIFF(day, cn.start_date, cn.end_date) AS reallocation_days
    FROM customer_nodes cn
    JOIN regions r
        ON cn.region_id = r.region_id
    WHERE cn.end_date <> '9999-12-31'
)
SELECT
    region_name,
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY reallocation_days)
        OVER (PARTITION BY region_name) AS median,
    PERCENTILE_CONT(0.8)
        WITHIN GROUP (ORDER BY reallocation_days)
        OVER (PARTITION BY region_name) AS percentile_80,
    PERCENTILE_CONT(0.95)
        WITHIN GROUP (ORDER BY reallocation_days)
        OVER (PARTITION BY region_name) AS percentile_95
FROM node_days;

SELECT
    txn_type,
    COUNT(*) AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type
ORDER BY txn_type;

WITH customer_deposits AS
(
    SELECT
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)

SELECT
    ROUND(AVG(deposit_count),2) AS avg_deposit_count,
    ROUND(AVG(deposit_amount),2) AS avg_deposit_amount
FROM customer_deposits;

WITH monthly_transactions AS
(
    SELECT
        customer_id,
        MONTH(txn_date) AS month_num,
        SUM(CASE WHEN txn_type = 'deposit' THEN 1 ELSE 0 END) AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count
    FROM customer_transactions
    GROUP BY
        customer_id,
        MONTH(txn_date)
)

SELECT
    month_num,
    COUNT(*) AS customer_count
FROM monthly_transactions
WHERE deposit_count > 1
  AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY month_num
ORDER BY month_num;