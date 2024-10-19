# Databricks notebook source
# MAGIC %md
# MAGIC ### Mount Azure Data Lake Containers for the Project

# COMMAND ----------

def mount_adls(storage_account_name,container_name):
    client_id= dbutils.secrets.get(scope='fotmula1-scope',key='formula1-app-client-id')
    tanent_id= dbutils.secrets.get(scope='fotmula1-scope',key='formula1-app-tanent-id')
    client_secret= dbutils.secrets.get(scope='fotmula1-scope',key='formula1-app-client-secret')

    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tanent_id}/oauth2/token"}

    if any(mount.mountPoint == f"/mnt/{storage_account_name}/{container_name}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storage_account_name}/{container_name}")

    dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

    display(dbutils.fs.mounts())



# COMMAND ----------

mount_adls('formula1dl2001','raw')

# COMMAND ----------

mount_adls('formula1dl2001', 'processed')

# COMMAND ----------

mount_adls('formula1dl2001', 'presentation')
