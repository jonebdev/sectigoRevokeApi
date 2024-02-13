import os
import csv
import requests

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
customer_uri = os.environ.get("CUSTOMER_URI")
# you fill this in, idk what your filename is
filename = ""

base_url = "https://cert-manager.com/api/ssl/v1/revoke/"
headers = {
  "login": username,
  "password": password,
  "Content-Type": "application/json",
  "customerUri": customer_uri
}

reason = {
  "reason": "testing"
}

with open(filename) as csv_file:
  ssl = csv.reader(csv_file)
  for row in ssl:
    new_url = base_url + row["id"]
    # expected output should be https://cert-manager.com/api/ssl/v1/revoke/${id}
    req = requests.post(url=new_url, headers=headers, data=reason)
    
    # do optional error checking if you would like if something goes wrong
    