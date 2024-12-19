docker run -p 8888:8888 --name jupyter-notebook-container jupyter/pyspark-notebook

https://www.kaggle.com/datasets/martinfrederiksen/danish-residential-housing-prices-1992-2024?select=DKHousingPricesSample100k.csv

df = df.withColumn("year", year(col("date")))

# Определение века
df = df.withColumn("century", when((col("year") >= 1900) & (col("year") < 2000), 20).otherwise(when((col("year") >= 2000) & (col("year") < 2100), 21).otherwise(19))

# Показать результат
df.show()
