# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"D410000","system":"readv2"},{"code":"D410011","system":"readv2"},{"code":"D410100","system":"readv2"},{"code":"D410400","system":"readv2"},{"code":"D410z00","system":"readv2"},{"code":"15301.0","system":"med"},{"code":"15311.0","system":"med"},{"code":"17486.0","system":"med"},{"code":"17605.0","system":"med"},{"code":"37129.0","system":"med"},{"code":"44611.0","system":"med"},{"code":"44894.0","system":"med"},{"code":"5086.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('secondary-polycythaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["secondary-polycythaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["secondary-polycythaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["secondary-polycythaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
