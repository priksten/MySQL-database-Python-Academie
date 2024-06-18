import csv
import mysql.connector

# Functies voor het maken en bewerken van tabellen
def create_table(database, table_name, column_tuple):
    """
    Deze functie maakt binnen een database (naar keuze) een tabel aan met een door de gebruiker gekozen naam en kolomnamen.
    Argumenten:
    - database
    - tabelnaam
    - kolomnamen
    """
    sql = "CREATE TABLE " + table_name + " (" + column_tuple + ")"
    mycursor = database.cursor()
    mycursor.execute(sql)

    database.commit()

def delete_table(database, table_name):
    """
    Met behulp van deze functie kunnen we een tabel naar keueze uit de datbase verwijderen
    """
    sql = "DROP TABLE " + table_name

    mycursor = database.cursor()
    mycursor.execute(sql)

    database.commit()

def add_column(database, table, column_name):
    """
    Deze functie voegt een kolom toe aan tabel(naar keuze) binnen een database (naar keuze)
    Argumenten:
    databasenaam
    tabelnaam
    kolomnaam
    """
    sql = "ALTER TABLE " + table + " ADD " + column_name 

    mycursor = database.cursor()
    mycursor.execute(sql)

    database.commit()

def remove_column(database, table, column_name):
    """
    Met behulp van deze functie kunnen we een kolom naar keuze in een tabel naar keuze verwijderen
    """
    sql = "ALTER TABLE " + table + " DROP COLUMN " + column_name

    mycursor = database.cursor()
    mycursor.execute(sql)

    database.commit()

def add_data(database, table, name, age):
    """
    Deze functie voegt data toe aan een tabel (naar keuze) binnen een database (naar keuze) 
    Argumenten:
    - database
    - tabel
    - data: data die relevant zijn voor de database
    """
    sql = "INSERT INTO " + table + " (naam, leeftijd) VALUES (%s, %s)"
    val = (name, age)
    
    mycursor = database.cursor()
    mycursor.execute(sql, val)

    database.commit()
    
def change_data(database, table, property_name, value1, value2):
    """
    Deze functie verandert data in een tabel (naar keuze) binnen een database (naar keuze)
    Argumenten:
    - database
    - tabel
    - kolom die gewijzigd moet worden
    - value1: de nieuwe waarde
    - value2: de oude waarde
    """ 
    sql = "UPDATE " + table + " SET "+ property_name + "= %s WHERE " + property_name + "=%s"
    val = (value1, value2)
    
    mycursor = database.cursor()
    mycursor.execute(sql, val)

    database.commit()

def delete_data(database, table, property_name, value):
    """
    Deze functie verwijdert data in een tabel (naar keuze) binnen een database (naar keuze)
    """
    # Deleten van entries uit de studenten database
    sql = "DELETE FROM " + table + " WHERE " + property_name + "=%s"
    val = (value,)

    mycursor = database.cursor()
    mycursor.execute(sql, val)
    
    database.commit()

def add_data_to_column(database_name, table_name, column_name, value_list):
    """
    Deze functie voegt waarden toe aan een kolom naar keuze binnen een tabel (naar keuze) in de database.
    Argumenten:
    - database-naam
    - tabel-naam
    - kolomnaam
    - lijst met data
    - lijst waarin aangegeven wordt in welke rij de data aangepast moet worden
    """
    sql = "UPDATE " + table_name + " SET " + column_name + "=%s" + " WHERE id =%s"  
    val = (value_list[0], 1)

    mycursor = database_name.cursor()
    mycursor.execute(sql, val)
    
    database_name.commit()

def add_multiple_data_to_column(database_name, table_name, column_name, value_list):
    """
    Deze functie voegt waarden toe aan een kolom naar keuze binnen een tabel (naar keuze) in de database.
    Argumenten:
    - database-naam
    - tabel-naam
    - kolomnaam
    - lijst met data
    - lijst waarin aangegeven wordt in welke rij de data aangepast moet worden
    """
    mycursor = database_name.cursor()    
    index = 0
    while index != len(value_list):
        sql = "UPDATE " + table_name + " SET " + column_name + "=%s" + " WHERE id =%s"  
        val = (value_list[index], index + 1)
        mycursor.execute(sql, val)

        index += 1
    
    database_name.commit()

# Functies voor het importeren van data uit csv-bestanden
def read_information(file):
    """
    Deze functie accepteert als invoer een csv-bestand en retourneert een lijst waarin ieder element een lijst is met persoonseigenschappen"
    """
    with open(file, newline='') as f:
        reader = csv.reader(f)
        person_list = []
        for row in reader:
            var = row[0].split(";")
            person_list.append(var)
        # print(var)
    
    return person_list



#----------------------------------------------------------------------------------------------------
# Ruimte voor het testen van bovenstaande functies
# Verbinden met de database python_academie

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  database="python_academie"
)

mycursor = mydb.cursor()

# table_names = ['studenten', 'docenten']

# for table in table_names:
#     create_table(mydb, table, ("id INT AUTO_INCREMENT PRIMARY KEY, naam VARCHAR(255), leeftijd INT") )

# studenten_list = read_information('Student.csv')
# studenten_list = read_information('Student.csv')

# for student in studenten_list:
#    naam = student[0]
#    age = student[1]

#    add_data(mydb, 'studenten', naam, age)

# docenten_list = read_information('Docent.csv')

# for docent in docenten_list:
#    naam = docent[0]
#    age = docent[1]

#    add_data(mydb, 'docenten', naam, age)

# add_column(mydb, 'studenten', 'opleiding VARCHAR(255)')
# value_list = ['wiskunde', 'wiskunde', 'wiskunde', 'wiskunde']
# add_multiple_data_to_column(mydb, 'studenten', 'opleiding', value_list)

# remove_column(mydb, 'studenten', 'opleiding')
# delete_table(mydb, 'studenten')
# delete_table(mydb, 'docenten')