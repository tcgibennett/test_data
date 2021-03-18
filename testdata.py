"""
This was built using the library at the following location https://github.com/joke2k/faker

The docs.md contains a list of all the providers and possible calls with outputs.
It is recommended to setup a virtual environment before running python3 -m pip install Faker
"""

from faker import Faker
import csv
import re


def createFile(name):
  return open(name, 'w', newline='')

def writeRow(fh, row):
  fh.writerow(row)

def closeFile(fh):
  fh.close()

def main():
  fake = Faker()
  file = createFile('test.dat')
  csvf = csv.writer(file,delimiter="|") 
  header = ["SSN","Name","Address","Latitude","Longitude","Phone", "Job","BirthDate","Email","CreditCardProvider","CreditCardNumber","Company","CompanyAddress","CreatedOn"]
  writeRow(csvf, header)
  for _ in range(100000000):
    l = []
    l.append(fake.ssn())
    l.append(fake.name())
    l.append(fake.address().replace("\n", " "))
    latlng = fake.local_latlng()
    l.append(latlng[0])
    l.append(latlng[1])
    l.append(fake.phone_number())
    l.append(fake.job())
    l.append(fake.date())
    l.append(fake.email())
    l.append(re.sub('( \d{2} \w+| \/ Carte Blanche)','',fake.credit_card_provider()))
    l.append(fake.credit_card_number())
    l.append(fake.company())
    l.append(fake.address().replace("\n", " "))
    l.append(fake.date_time())
    writeRow(csvf, l)
    l.clear()
  closeFile(file)

if __name__ == "__main__":
    main()