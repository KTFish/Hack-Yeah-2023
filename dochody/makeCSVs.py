import csv


if __name__ == "__main__":
    with open('dochody/output/jednostka.csv', mode='a', newline='') as jednostka:
        csv_writer = csv.writer(jednostka)
        header = ['Id_jednostki', 'Nazwa', 'Typ', 'Regon', 'WK', 'PK', 'GK', 'GT', 'PT']
        csv_writer.writerow(header)
    with open('dochody/output/naglowek.csv', mode='a', newline='') as naglowek:
        csv_writer = csv.writer(naglowek)
        header = ['Id_naglowka', 'Wersja', 'DataSprawozdania']
        csv_writer.writerow(header)
    with open('dochody/output/okres.csv', mode='a', newline='') as okres:
        csv_writer = csv.writer(okres)
        header = ['Id_okresu', 'Rok', 'TypOkresu']
        csv_writer.writerow(header)
    with open('dochody/output/pozycje.csv', mode='a', newline='') as pozycje:
        csv_writer = csv.writer(pozycje)
        header = ['Id_pozycji', 'Dzial', 'Rodzial', 'Paragraf', 'P4', 'PL', 'NA', 'DW', 'NO', 'NZ']
        csv_writer.writerow(header)
    with open('dochody/output/sprawozdanie.csv', mode='a', newline='') as sprawozdanie:
        csv_writer = csv.writer(sprawozdanie)
        header = ['Id_sprawozdania','Id_okresu', 'Id_jednostki', 'Id_naglowka', 'Id_pozycji']
        csv_writer.writerow(header)