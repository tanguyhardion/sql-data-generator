from random import randint, sample
import names as randnames
import datetime

numsEtu = {}
isbns = []


def genUsager(count):
    insert = "INSERT INTO usager (numEtu, nom, prenom, categorie) VALUES\n"
    numbers = sample(range(40000, 70000), count)
    for i in range(count):
        insert += "("
        numsEtu[str(numbers[i])] = str(randint(1, 3))
        insert += list(numsEtu.keys())[i] + ", "
        insert += "'" + randnames.get_first_name() + "', "
        insert += "'" + randnames.get_last_name() + "', "
        insert += list(numsEtu.values())[i]
        insert += "),\n"
    insert = insert[:-2] + ";"
    return insert


def genOuvrage(count):
    names = open("data/names.txt", "r").readlines()
    editors = open("data/editors.txt", "r").readlines()
    types = open("data/types.txt", "r").readlines()
    languages = open("data/languages.txt", "r").readlines()
    insert = "INSERT INTO ouvrage VALUES\n"
    for i in range(count):
        insert += "("
        isbns.append(str(randint(10**9, 10**10 - 1)))
        insert += str(isbns[i]) + ", "
        insert += str(randint(10**12, 10**13 - 1)) + ", "
        insert += "'" + names[i].strip() + "', "
        insert += "'" + randnames.get_full_name() + "', "
        insert += "'" + editors[randint(0, len(editors) - 1)].strip() + "', "
        insert += str(randint(1900, 2022)) + ", "
        insert += "'" + types[randint(0, len(types) - 1)].strip() + "', "
        insert += "'" + languages[randint(0, len(languages) - 1)].strip() + "', "
        insert += str(randint(1, 10)) + ", "
        insert += "'" + randnames.get_last_name() + "'"
        insert += "),\n"
    insert = insert[:-2] + ";"
    return insert


def genEmprunt(count):
    insert = "INSERT INTO emprunt (numEtu, isbn, dateEmp, rendu) VALUES\n"
    tempNumsEtu = numsEtu.copy()
    tempIsbns = isbns.copy()
    for i in range(count):
        insert += "("
        numEtu = list(tempNumsEtu.keys())[randint(0, len(tempNumsEtu) - 1)]
        categorie = tempNumsEtu[numEtu]
        insert += numEtu + ", "
        tempNumsEtu.pop(numEtu)
        isbn = tempIsbns[randint(0, len(tempIsbns) - 1)]
        insert += isbn + ", "
        tempIsbns.remove(isbn)
        borrowDate = datetime.date(randint(2010, 2021), randint(1, 12), randint(1, 28))
        # match categorie:
        #     case "1":
        #         endBorrowDate = borrowDate + datetime.timedelta(days=10)
        #     case "2":
        #         endBorrowDate = borrowDate + datetime.timedelta(days=15)
        #     case "3":
        #         endBorrowDate = borrowDate + datetime.timedelta(days=20)
        insert += "'" + borrowDate.strftime("%Y-%m-%d") + "', "
        temp = randint(0, 100)
        if temp < 10:
            insert += "0"
        else:
            insert += "1"
        # insert += "'" + endBorrowDate.strftime("%Y-%m-%d") + "'"
        insert += "),\n"
    insert = insert[:-2] + ";"
    return insert


def genSuggestion(count):
    insert = (
        "INSERT INTO suggestion_achat (numEtu, titreOuvrage, quantite, etat) VALUES\n"
    )
    otherNames = open("data/otherNames.txt", "r").readlines()
    tempNumsEtu = numsEtu.copy()
    for i in range(count):
        insert += "("
        insert += list(tempNumsEtu.keys())[randint(0, len(tempNumsEtu) - 1)] + ", "
        otherName = otherNames[randint(0, len(otherNames) - 1)]
        insert += "'" + otherName.strip() + "', "
        otherNames.remove(otherName)
        insert += str(randint(1, 10)) + ", "
        insert += str(randint(-1, 1))
        insert += "),\n"
    insert = insert[:-2] + ";"
    return insert


def genAll(countUsager, countOuvrage, countEmprunt, countSuggestion):
    output = open("sql/output.sql", "w")
    output.write(genUsager(countUsager))
    output.write("\n\n" + genOuvrage(countOuvrage))
    output.write("\n\n" + genEmprunt(countEmprunt))
    output.write("\n\n" + genSuggestion(countSuggestion))
    output.close()

genAll(7, 5, 3, 2)
