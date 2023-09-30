import xml.etree.ElementTree as ET
import csv


def get_data(file, header, xml):
    with open(file, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # get last row to check, whether it contains data or not
        last_row = get_data_from_last_row(file)
        try:
            int(last_row[0])
            id = int(last_row[0])
        except ValueError:
            id = -1

        row = [id+1]
        # get data
        for string in header[1:]:
            try:
                data = xml.find(string).text
            except AttributeError:
                data = ''
            row.append(data)

        # check if data is already in the database
        criteria = []
        for i, s in enumerate(row[1:]):
            criteria.append((i+1, s))

        find_row = find_row_in_csv(file, criteria)
        if not find_row:
            csv_writer.writerow(row)
            return row[0]
        else:
            return find_row[0]


def get_data_from_last_row(csv_file_path):
    with open(csv_file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        last_row = None
        for row in csv_reader:
            last_row = row
        return last_row


def find_row_in_csv(csv_file_path, criteria):
    with open(csv_file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader, None)
        for row in csv_reader:
            if all(row[i] == value for i, value in criteria):
                return row

        return None


def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    jednostki = root.find('Jednostki')

    with open('wydatki/output/sprawozdanie.csv', mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        last_row = get_data_from_last_row('wydatki/output/sprawozdanie.csv')
        for jednostka in jednostki:
            try:
                int(last_row[0])
                id = int(last_row[0])
            except ValueError:
                id = -1

            row = []
            spr = jednostka.find('Sprawozdania')
            rb = spr.find('Rb-28s')

            # okres
            okres = rb.find('Okres')
            row.append(get_data('wydatki/output/okres.csv', ['Id_okresu', 'Rok', 'TypOkresu', 'Okres'], okres))

            # jednostka
            jednostka = rb.find('Jednostka')
            row.append(get_data('wydatki/output/jednostka.csv', ['Id_jednostki', 'Nazwa', 'Typ', 'Regon', 'WK', 'PK', 'GK', 'GT', 'PT'], jednostka))

            # naglowek
            naglowek = rb.find('Naglowek')
            row.append(get_data('wydatki/output/naglowek.csv', ['Id_naglowka', 'Wersja', 'DataSprawozdania', 'DostepneGrupyParagrafow'], naglowek))

            # pozycje
            pozycje = rb.find('Pozycje')
            for pozycja in pozycje:
                id += 1
                id_pozycji = get_data('wydatki/output/pozycje.csv', ['Id_pozycji', 'Dzial', 'Rodzial', 'Grupa', 'Paragraf', 'P4', 'PL', 'ZA', 'WW', 'ZO'], pozycja)
                csv_writer.writerow([id] + row + [id_pozycji])

if __name__ == "__main__":
    parseXML('wydatki/input/Sprawozdania[2023][IIKwartał] Wydatki.xml')
    parseXML('wydatki/input/Sprawozdania[2022][IVKwartał] Wydatki.xml')
