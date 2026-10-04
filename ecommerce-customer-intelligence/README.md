# E-Commerce Customer Intelligence System

The E-Commerce Customer Intelligence System is a data analytics project designed to analyze customer 
behavior, sales performance, product performance, order outcomes, and revenue trends 
using a real-world-style e-commerce dataset.

The project applies Python, NumPy, Pandas, and Matplotlib to transform raw transactional data into 
meaningful business insights. 
The analysis covers data cleaning, feature engineering, KPI development, customer segmentation, sales 
analysis, product and category performance, discount analysis, order-status analysis, 
outlier detection, and business-focused data visualization.

The primary objective is to understand what drives revenue, how customers contribute to sales, 
which products and categories perform best, and where potential business 
opportunities or operational issues exist.

## Business Objectives

The analysis was designed to answer the following business questions:

1. **Sales Performance**

   * How is revenue distributed across categories and time periods?
   * Which months generate the highest and lowest revenue?
   * How does revenue change month over month?

2. **Customer Analysis**

   * How frequently do customers place orders?
   * What proportion of customers are repeat customers?
   * Which customers contribute the most revenue?
   * Is revenue concentrated among a small group of customers?

3. **Product & Category Performance**

   * Which products generate the most revenue?
   * Which categories are the primary revenue drivers?
   * How do product prices, quantities, and AOV influence revenue?

4. **Discount Analysis**

   * How does discount level relate to AOV and revenue per unit?
   * Does increasing the discount appear to affect purchasing behavior?

5. **Order & Operational Analysis**

   * What proportion of orders are delivered, cancelled, returned, or shipped?
   * Are certain products or categories associated with higher cancellation or return rates?

6. **Data Quality & Statistical Analysis**

   * Are there missing, duplicate, invalid, or inconsistent records?
   * Are there significant revenue outliers?
   * Which unusual transactions require further investigation?

    
## Dataset & Tools

### Dataset

The dataset contains **15,075 e-commerce transaction records** covering customer orders, products, pricing, discounts, payment methods, locations, and order statuses.

**Key columns include:**

| Column         | Description                         |
| -------------- | ----------------------------------- |
| `Order_ID`     | Unique identifier for each order    |
| `Customer_ID`  | Unique identifier for each customer |
| `Date`         | Order date                          |
| `City`         | Customer city                       |
| `Category`     | Product category                    |
| `Product`      | Product purchased                   |
| `Price`        | Product price                       |
| `Quantity`     | Number of units purchased           |
| `Discount`     | Discount percentage                 |
| `Payment`      | Payment method                      |
| `Order_Status` | Order outcome                       |

### Technologies & Libraries

* **Python** — Data analysis and processing
* **NumPy** — Numerical calculations
* **Pandas** — Data cleaning, transformation, aggregation, and analysis
* **Matplotlib** — Data visualization
* **Jupyter Notebook** — Interactive analysis and documentation


## Data Cleaning

The raw dataset was examined for missing values, duplicates, invalid entries, and categorical inconsistencies before analysis.

### Cleaning Steps

* Checked for duplicate records and missing values.
* Investigated invalid values in `Quantity`, `Price`, and `Discount`.
* Filled missing `Discount` values with `0`, treating them as orders without a recorded discount.
* Standardized `Category` values using `str.strip()` and `str.title()`.
* Standardized `City` values using `str.strip()` and `str.title()`.
* Converted the `Date` column into a datetime format using `pd.to_datetime()` with mixed date handling.
* Verified that discount values were within the valid range (0–100%).

After cleaning, the dataset was ready for feature engineering, statistical analysis, and visualization.

## Feature Engineering

New calculated fields were created to support revenue and business analysis.

### Revenue Calculation

The following metrics were derived from `Price`, `Quantity`, and `Discount`:

* **Revenue** — gross value before discount.
* **Discount Amount** — monetary value of the discount applied.
* **Net Revenue** — revenue after discount.

```python
df["Revenue"] = df["Price"] * df["Quantity"]

df["Discount_Amount"] = (
    df["Revenue"] * df["Discount"] / 100
)

df["Net_Revenue"] = (
    df["Revenue"] - df["Discount_Amount"]
)
```

### Realized Revenue

To distinguish completed sales from other order outcomes, a `Realized_Revenue` field was created using only delivered orders:

```python
df["Realized_Revenue"] = np.where(
    df["Order_Status"] == "Delivered",
    df["Net_Revenue"],
    0
)
```

This metric was used in analyses where revenue should represent completed deliveries rather than cancelled, returned, or still-shipped orders.

## Key Performance Indicators

The following KPIs were calculated to provide a high-level view of the e-commerce business:

| KPI                       |      Value |
| ------------------------- | ---------: |
| Total Customers           |      2,494 |
| Total Orders              |     15,045 |
| Calculated Net Revenue    |   ₹246.32M |
| Average Order Value (AOV) | ₹16,454.27 |
| Delivered Orders          |      8,582 |
| Delivery Rate             |     57.33% |
| Cancellation Rate         |     14.45% |
| Return Rate               |     14.35% |
| Delivered Revenue         |   ₹144.75M |
| Delivered Revenue Share   |     58.77% |

> **Note:** Calculated Net Revenue includes all order statuses. Delivered Revenue represents revenue associated with delivered orders only.


## Sales & Time-Based Analysis

Sales performance was analyzed across product categories, payment methods, order statuses, and time periods.

### Key Analysis

* Compared revenue contribution across product categories.
* Analyzed monthly revenue trends using the order date.
* Calculated month-over-month revenue growth.
* Identified the highest- and lowest-revenue months.
* Compared payment methods based on revenue, order volume, and Average Order Value (AOV).
* Evaluated delivered revenue separately from calculated net revenue.
* Analyzed order-status distribution across Delivered, Shipped, Cancelled, and Returned orders.

### Time-Based Findings

Revenue showed fluctuations across the analyzed months, with **June recording the highest revenue** and **December recording the lowest revenue**.

Some periods contained very few records, particularly **July 2026 and December 2026**. Therefore, unusually large month-over-month changes in these periods were treated as potential data-coverage issues rather than reliable business trends.

## Customer Analysis

Customer behavior was analyzed to understand purchasing frequency, revenue contribution, customer value, and revenue concentration.

### Key Analysis

* Calculated the number of orders placed by each customer.
* Identified one-time and repeat customers.
* Calculated revenue generated per customer.
* Identified the top customers by revenue and Average Order Value (AOV).
* Segmented customers into Low Value, Medium Value, and High Value groups using revenue quartiles.
* Analyzed the relationship between order frequency and customer revenue.
* Evaluated customer revenue concentration using cumulative revenue analysis.

### Key Findings

* **2,494 customers** were identified in the dataset.
* **98.52%** of customers were repeat customers.
* Repeat customers accounted for approximately **99.81% of calculated net revenue**.
* The average customer placed approximately **6 orders**.
* The top 10 customers contributed only about **1.63% of total calculated revenue**, indicating low revenue concentration among the highest-value customers.
* High-value customers accounted for approximately **49.6% of total calculated revenue**, while medium-value customers contributed **43.3%** and low-value customers contributed **7.1%**.
* The correlation between total orders and total customer revenue was approximately **0.58**, indicating a moderate positive relationship.
* The correlation between total orders and AOV was approximately **0.04**, indicating almost no linear relationship between order frequency and average order value.

> **Note:** These customer behavior patterns are specific to this dataset and should not be treated as general industry benchmarks.

## Product & Category Analysis

Product and category performance were analyzed to identify the main revenue drivers, high-performing products, and differences in average order value and revenue contribution.

### Key Analysis

* Ranked products based on total calculated net revenue.
* Analyzed product-level order volume and quantity sold.
* Calculated Average Order Value (AOV) for each product.
* Calculated average revenue per unit.
* Compared revenue contribution across product categories.
* Compared category-level order volume, quantity, AOV, and revenue share.
* Compared revenue share with order share to identify categories generating disproportionately high or low revenue.

### Key Findings

* **Electronics** was the largest revenue-generating category, contributing approximately **62.94% of total calculated revenue**.
* Electronics had an AOV of approximately **₹34,437**, substantially higher than Clothing at approximately **₹6,858**.
* Electronics generated a much larger revenue share than its order share, indicating that **higher product prices were the primary driver of its revenue contribution**.
* The average quantity per order was relatively similar across categories, suggesting that Electronics' revenue dominance was not primarily caused by customers purchasing significantly more units.
* **USB-C Hub, Wireless Earbuds, Headphones, Gaming Mouse, and Mechanical Keyboard** were among the highest-revenue products.
* The top eight products were predominantly electronics, highlighting the importance of high-value electronic products to overall revenue.
* Books, Beauty, and Clothing generated a larger proportion of orders relative to their revenue contribution because their products had substantially lower average prices.

> **Note:** Revenue figures represent calculated net revenue unless explicitly stated otherwise. Revenue contribution should not be interpreted as profitability because product costs and margins were not available in the dataset.

## Discount & Order Analysis

Discount levels and order outcomes were analyzed to understand how discounts relate to order value and how orders are distributed across different statuses.

### Key Analysis

* Examined the distribution of discount percentages.
* Compared AOV and revenue per unit across different discount levels.
* Analyzed average quantity per order at different discount levels.
* Calculated the relationship between discount, quantity, and net revenue.
* Analyzed the distribution of Delivered, Shipped, Cancelled, and Returned orders.
* Compared order-status patterns across categories and discount levels.

### Key Findings

* The most common discount levels were **0%, 5%, and 10%**.
* AOV and revenue per unit generally decreased as discount levels increased.
* Average quantity per order remained relatively stable at approximately **2.1–2.2 units**, indicating that higher discounts did not substantially increase basket size.
* The correlation between discount and net revenue was **−0.07**, indicating a very weak negative linear relationship.
* The overall order distribution was:

  * **Delivered:** 57.33%
  * **Cancelled:** 14.45%
  * **Returned:** 14.35%
  * **Shipped:** 13.87%
* Category-level cancellation and return rates were relatively similar, suggesting that category alone did not explain major differences in order outcomes.
* Discount levels also did not show a clear increasing or decreasing pattern in cancellation and return rates.

> **Note:** These relationships are observational and do not establish that discounts directly cause changes in revenue or order outcomes.

### Business Takeaway

The analysis suggests that **higher discounts are associated with lower AOV and revenue per unit without a meaningful increase in basket size**. Therefore, discounting should be used selectively rather than broadly, while order-status monitoring should remain a separate operational priority.

## Statistical & Outlier Analysis

Statistical techniques were used to understand the distribution of revenue and identify unusually high-value transactions that required further investigation.

### Key Analysis

* Calculated descriptive statistics for customer and transaction-level metrics.
* Used quartiles and the **Interquartile Range (IQR)** method to identify potential revenue outliers.
* Investigated high-value transactions to determine whether they were data-quality issues or legitimate purchases.
* Analyzed correlations between selected numerical variables.

### Key Findings

* The IQR method identified transactions with `Net_Revenue` above approximately **₹46,963.50** as potential high-value outliers.
* Investigation showed that these transactions were primarily associated with **high-priced electronic products purchased in larger quantities**.
* The identified outliers did not appear to be obvious data-entry errors and were therefore retained in the dataset.
* Quantity and net revenue showed a **moderate positive relationship**, while discount and net revenue showed only a **very weak negative relationship**.

### Business Takeaway

High-value transactions can have a significant impact on revenue analysis, but **outliers should be investigated rather than automatically removed**. In this dataset, the unusual transactions appeared to represent legitimate high-value purchases rather than data-quality problems.

## Visualizations

Matplotlib was used to transform the analytical results into clear, business-focused visualizations. The charts were designed to highlight revenue trends, customer behavior, product performance, and operational patterns.

### Visualizations Created

* Revenue by Category
* Monthly Revenue Trend
* Top 10 Products by Revenue
* Order Status Distribution
* Revenue by Payment Method
* Revenue Share vs Order Share by Category
* AOV by Discount Level
* Customer Revenue Distribution
* Customer Order Frequency Distribution
* Quantity vs Net Revenue
* Realized Revenue by Category
* Order Status Distribution by Category
* Top 10 Customers by Realized Revenue
* Revenue by Customer Segment
* Revenue by City
* Discount Distribution
* Revenue Outlier Analysis
* Revenue Concentration by Customer Group

### Visualization Approach

The visualizations were selected according to the type of business question being analyzed:

* **Bar charts** were used for category, product, payment, city, and customer comparisons.
* **Line charts** were used to analyze revenue trends over time.
* **Histograms** were used to understand customer and discount distributions.
* **Scatter plots** were used to examine relationships between numerical variables.
* **Stacked bar charts** were used to compare order-status distributions across categories.
* **Box plots** were used to identify potential revenue outliers.

The visualizations helped convert numerical analysis into patterns that can be interpreted more easily from a business perspective.

## Key Business Insights

The analysis produced the following key business insights:

1. **Electronics is the primary revenue driver**
   Electronics contributed approximately **62.94% of total calculated revenue**, mainly because of its substantially higher product prices and AOV compared with other categories.

2. **Revenue is not highly concentrated among a few customers**
   The top 10 customers contributed only approximately **1.63% of total calculated revenue**, indicating that revenue is distributed across a broad customer base.

3. **Repeat customers dominate the dataset**
   Approximately **98.52% of customers were repeat customers**, and repeat customers accounted for approximately **99.81% of calculated net revenue**. These figures are specific to this dataset and should not be treated as industry benchmarks.

4. **Higher discounts are associated with lower order value**
   AOV and revenue per unit generally decreased as discount levels increased, while average quantity per order remained relatively stable.

5. **Order outcomes require operational attention**
   Only **57.33% of orders were delivered**, while **14.45% were cancelled** and **14.35% were returned**, indicating potential opportunities to improve order fulfillment and reduce unsuccessful orders.

6. **Revenue varies significantly by product value**
   Categories with higher-priced products can generate substantially more revenue even when their order volumes are similar to lower-priced categories.

7. **High-value transactions should be investigated, not automatically removed**
   Outlier analysis identified several unusually large orders, but investigation suggested that these were primarily legitimate purchases of high-priced products in larger quantities.

8. **Revenue trends require careful interpretation when data coverage is low**
   Extremely large month-over-month changes in periods such as July 2026 and December 2026 were associated with very few records and were therefore treated as potential data-coverage issues rather than reliable business trends.


## Business Recommendations

Based on the analysis, the following recommendations can be considered:

1. **Prioritize high-value product categories**
   Electronics contributes the largest share of revenue. Maintaining strong availability and visibility for high-performing electronic products could help protect the primary revenue driver.

2. **Use discounts selectively**
   Since higher discount levels were associated with lower AOV and revenue per unit without a meaningful increase in average basket size, broad discounting should be avoided. Discounts can instead be targeted toward specific products, customer segments, or business objectives.

3. **Focus on reducing cancellations and returns**
   With only 57.33% of orders delivered and a significant proportion cancelled or returned, improving fulfillment and reducing unsuccessful orders could represent an important operational opportunity.

4. **Monitor high-performing products closely**
   Products such as USB-C Hubs, Wireless Earbuds, Headphones, Gaming Mice, and Mechanical Keyboards contribute substantially to revenue. Their inventory and sales performance should be monitored regularly.

5. **Use customer segmentation for targeted strategies**
   High-value customers contribute a substantial share of revenue, making customer segmentation useful for developing targeted retention and engagement strategies.

6. **Improve data monitoring and quality controls**
   Periods with very low transaction volumes produced misleading month-over-month changes. Automated checks for missing data, unusual transaction volumes, and inconsistent dates could improve the reliability of future reporting.

> **Note:** These recommendations are based on patterns observed in the dataset. Actual business decisions would require additional information such as costs, profit margins, inventory levels, customer acquisition costs, and operational data.

## Conclusion

The E-Commerce Customer Intelligence System demonstrates how raw transactional data can be transformed into meaningful business insights using Python, NumPy, Pandas, and Matplotlib.

The project covered the complete analytical workflow, including **data exploration, data cleaning, feature engineering, KPI development, sales analysis, customer analysis, product and category analysis, discount analysis, statistical analysis, outlier detection, and business-focused visualization**.

The analysis showed that **Electronics was the primary revenue driver**, repeat customers represented the majority of the customer base, and higher discount levels were associated with lower AOV and revenue per unit without a significant increase in basket size. The project also highlighted operational considerations around cancellations and returns and demonstrated the importance of investigating unusual transactions before classifying them as data errors.

Overall, this project demonstrates the ability to move beyond basic data manipulation and use analytical techniques to **identify patterns, evaluate business performance, communicate insights, and support data-driven decision-making**.
