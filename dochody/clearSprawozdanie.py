import csv
import os

if __name__ == "__main__":
    os.remove("dochody/output/sprawozdanie.csv")
    with open('dochody/output/sprawozdanie.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        header = ['Id_sprawozdania', 'Id_okresu', 'Id_jednostki', 'Id_naglowka', 'Id_pozycji']
        csv_writer.writerow(header)
