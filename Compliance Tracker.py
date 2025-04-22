Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Compliance Tracking Sytem for GDPR & ISO 27001

# PROJECT STRUCTURE
# Cli/ -> CLI-based tracker
# web/ -> Web-based UI
>>> # db/ -> Database management
>>> # logs/ -> Audit logs
>>> # reports/ -> Compliance reports
>>> # config/ -> Configuration files
>>> 
>>> 
>>> import os
>>> import json
>>> import sqlite3
>>> from datetime import datetime
>>>
>>> def int_db():
...     conn = sqlite3.connect("db/compliance.db")
...     cursor = conn.cursor()
...     cursor.execute(''' CREATE TABLE IF NOT EXISTS compliance (id INTEGER PRIMARY KEY AUTOINCREMENT, requirement TEXT NOT NULL, status TEXT NOT NULL, last_checked TEXT NOT NULL) ''')
...     conn.commit()
...     conn.close()
... 
>>> def log_compliance(requirement, status):
...     conn = sqlite3.connect("db/compliance.db")
...     cursor = conn.cursor()
...     cursor.execute("INSERT INTO compliance (requirement, status, last_checked) VALUES (?, ?, ?)",(requirement, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
...     conn.commit()
...     conn.close()
...     print(f"Logged: {requirement} - {status}")
... 
...     
>>> def generate_report():
...  conn = sqlite3.connect("db/compliance.db")
...  cursor = conn.cursor()
...  cursor.execute("SELECT * FROM compliance")
...  data = cursor.fetchall()
...  conn.close()
...  report_path = "reports/compliance_report.json"
...  with open(report_path, "w") as f:
...      json.dump(data, f, indent=4)
...      print(f"Report generated: {report_path}")
... 
...      
>>> if __name__ == "__main__":
...     os.makedirs("db", exist_ok=True)
...     os.makedirs("reports", exist_ok=True)
...     int_db()
...     log_compliance("GDPR - Data Encryption", "Compliant")
...     log_compliance("ISO 27001 - Access Control", "Non-Compliant")
...     generate_report()
