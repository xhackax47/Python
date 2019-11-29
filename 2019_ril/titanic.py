import csv
with open('titanic.csv') as f:

    csv_reader = csv.reader(f, delimiter=',')
    lines = [row for row in csv_reader] [1:]

    # Ignore first line
    lines = lines[1:]

    males = [line for line in lines if line[4] == "male" and line[1] == '0']
    females = [line for line in lines if line[4] == "female" and line[1] == '0']

"""
    female_count = 0
    male_count = 0
    survived_count = 0
    for row in csv_reader:
        lines.append(row)
        if row[4] == "female":
            female_count += 1
        elif row[4] == "male":
            male_count += 1
        else:
            survived_count += 1
    print("Il y a " + str(female_count) + " femmes mortes, " + str(man_count) + " d'hommes morts et " + str(survived_count) + " de survivants")
"""

print("Hommes morts : " + str(len(males)))
print("Femmes mortes : " + str(len(females)))