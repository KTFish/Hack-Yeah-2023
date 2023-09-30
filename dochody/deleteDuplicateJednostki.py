import csv
import os

if __name__ == "__main__":
    with open('dochody/output/jednostka.csv', mode='r', newline='') as jednostki:
        csv_reader_jed = csv.reader(jednostki)
        regon = set()
        ids = {}
        repeated_names = []
        for row_jed in csv_reader_jed:
            if row_jed[4] not in regon:
                regon.add(row_jed[4])
                ids[row_jed[4]] = row_jed[0]
            else:
                with open('dochody/output/sprawozdanie.csv', mode='r', newline='') as sprawozdania:
                    csv_reader_spr = csv.reader(sprawozdania)
                    for row_spr in csv_reader_spr:
                        if row_spr[2] == row_jed[1]:
                            row_spr[2] = ids[row_jed[4]]

        with open('dochody/output/temp.csv', mode='a', newline='') as tmp:
            csv_writer_tmp = csv.writer(tmp)
            for row_jed in csv_reader_jed:
                if ids[row_jed[4]] == row_jed[0]:
                    csv_writer_tmp.writerow(row_jed)

    os.remove("dochody/output/jednostka.csv")
    os.rename("dochody/output/temp.csv", "dochody/output/jednostka.csv")
