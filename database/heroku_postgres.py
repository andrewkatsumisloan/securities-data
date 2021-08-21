import os
import psycopg2

DATABASE_URL = 'postgres://pspqgsogfliqxw:cbce6c2ef946625313f028d941ba3b7fb53547dc86be3c4625968efa7739721c@ec2-18-233-83-165.compute-1.amazonaws.com:5432/db6g31aia4umng'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


print(conn)

