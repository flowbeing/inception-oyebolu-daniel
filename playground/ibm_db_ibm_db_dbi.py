
import ibm_db
import ibm_db_dbi
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn


dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = 'BLUDB'
dsn_hostname= 'dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net'
dsn_port = '50000'
dsn_protocol = 'TCPIP'
dsn_uid = 'xsw23585'
dsn_pwd = '89rcxw3964q^n3q5'

dsn =   ("DRIVER = {};"
         "DATABASE = {};"
         "HOSTNAME= {};"
         "PORT= {};"
         "PROTOCOL= {};"
         "UID= {};"
         "PWD= {};").format(dsn_driver, dsn_database,  dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)


# for trials in range(10):

try:
    conn = ibm_db.connect(dsn, "", "")
    print(f"You are connected to {dsn_database}. Your username is {dsn_hostname}")

except:
    print(f"Connection unsuccesful! Error log: {ibm_db.conn_errormsg()}")


# query = "SELECT * FROM INSTRUCTOR"

# execute_selectstmt = ibm_db.exec_immediate(conn, query)


# def fetch_rows(select_stmt):

#     row = ibm_db.fetch_assoc(select_stmt)

#     while row is not False:
#         print(row)
#         row = ibm_db.fetch_assoc(select_stmt)


# fetch_rows(execute_selectstmt)


# --------------------

pd_connection = ibm_db_dbi.Connection(conn)

data_frame = pd.read_sql("SELECT * FROM JOBS", pd_connection)

salary_max = data_frame["MAX_SALARY"].values
salary_min = data_frame["MIN_SALARY"].values

data_frame["RANGE"] = salary_max - salary_min

print(data_frame)

plt.plot('JOB_TITLE', 'MIN_SALARY', data=data_frame)
plt.show()

seaborn.barplot(data_frame['JOB_TITLE'], data_frame['MAX_SALARY'])
plt.show()

ibm_db.close(conn)