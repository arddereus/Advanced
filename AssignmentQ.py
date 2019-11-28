import csv

with open("Quizans.csv") as handler_csv_file:   #add "w+" if you want to erase the file
    RCF = csv.reader(handler_csv_file)
    table = list(RCF)

Question = input("Come up with a question:")
RA = input("what the answer to this question?")
FA1 = input("what is a first fake, wrong answer?")
FA2 = input("what is a second fake, wrong answer?")
FA3 = input("what is a third fake, wrong answer?")
new_row = list((Question, RA, FA1, FA2, FA3))
table.append(new_row)

with open("Quizans.csv", "w") as handler:
    file_writer = csv.writer(handler)
    for row in table:
        file_writer.writerow(row)

