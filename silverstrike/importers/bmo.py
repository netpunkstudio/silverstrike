import csv
import datetime

from silverstrike.importers.import_statement import ImportStatement

# csv Header line
# POSTED DATE,DESCRIPTION,AMOUNT,CURRENCY,TRANSACTION REFERENCE NUMBER,FI TRANSACTION REFERENCE,TYPE,CREDIT/DEBIT,ORIGINAL AMOUNT

def import_transactions(csv_path):
    lines = []
    with open(csv_path, encoding='latin-1') as csv_file:
        for line in csv.reader(csv_file, delimiter=',', quotechar='"'):
            if len(line) < 5:
                continue
            try:
                lines.append(ImportStatement(
                    book_date=datetime.datetime.strptime(line[0], '%m/%d/%Y').date(),
                    transaction_date=datetime.datetime.strptime(line[0], '%m/%d/%Y').date(),
                    account=line[1],
                    amount=float(line[2]),
                    ))
            except ValueError:
                # first line contains headers
                pass
    return lines
