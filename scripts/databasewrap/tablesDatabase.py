from tables import *
import numpy
import LogParseFunc
import os

class Molecule(IsDescription):
    name      = StringCol(32)
    energy    = Float32Col()

def createDatabase():
    dataFile = open_file('Database.h5',mode='w',title='Database')
    table = dataFile.create_table(dataFile.root,'Molecules',Molecule,'molecule table')

def insertMolecule(jsonDict,table):
    molecule = table.row
    
    molecule['name'] = jsonDict['name']
    molecule['energy'] = jsonDict['E(RHF)']
    molecule.append()

    table.flush()

def debugDisplay():
    dataFile = open_file('Database.h5',mode='a')
    table = dataFile.root.Molecules
    for row in table:
        print(row['name'])

if os.path.isfile('./Database.h5') == False:
    createDatabase()
else:
    dataFile = open_file('Database.h5',mode='a')
    table = dataFile.root.Molecules

string = LogParseFunc.jsonParse('LOG.log')
insertMolecule(string,table)