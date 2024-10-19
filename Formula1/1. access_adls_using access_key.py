# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using access keys
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

formula1dl_sccount_key = dbutils.secrets.get(scope='fotmula1-scope',key='formula1dl2001-account-key')

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.formula1dl2001.dfs.core.windows.net",
    formula1dl_sccount_key)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dl2001.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dl2001.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


