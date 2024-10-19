# Databricks notebook source
# MAGIC %md
# MAGIC ### Mount Azure Data Lake using Service Principal
# MAGIC #### Steps to follow
# MAGIC 1. Get client_id, tenant_id and client_secret from key vault
# MAGIC 2. Set Spark Config with App/ Client Id, Directory/ Tenant Id & Secret
# MAGIC 3. Call file system utlity mount to mount the storage
# MAGIC 4. Explore other file system utlities related to mount (list all mounts, unmount)

# COMMAND ----------

client_id= dbutils.secrets.get(scope='fotmula1-scope',key='formula1-app-client-id')
tanent_id= dbutils.secrets.get(scope='fotmula1-scope',key='formula1-app-tanent-id')
client_secret= dbutils.secrets.get(scope='fotmula1-scope',key='formula1-app-client-secret')

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tanent_id}/oauth2/token"}


# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://demo@formula1dl2001.dfs.core.windows.net/",
  mount_point = "/mnt/formula1dl/demo",
  extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.ls("/mnt/formula1dl/demo"))

# COMMAND ----------

display(spark.read.csv("/mnt/formula1dl/demo/circuits.csv"))

# COMMAND ----------

display(dbutils.fs.mounts())
