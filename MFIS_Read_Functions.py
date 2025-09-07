#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from MFIS_Classes import *


def readFuzzySetsFile(fleName):
    """
    This function reads a file containing fuzzy set descriptions
    and returns a dictionary with all of them
    """
    fuzzySetsDict = FuzzySetsDict() # dictionary to be returned
    inputFile = open(fleName, 'r')
    line = inputFile.readline()
    while line != '':
        fuzzySet = FuzzySet()   # just one fuzzy set
        elementsList = line.split(', ')
        setid = elementsList[0]
        var_label=setid.split('=')
        fuzzySet.var=var_label[0]
        fuzzySet.label=var_label[1]        

        xmin = int(elementsList[1])
        xmax = int(elementsList[2])
        a = int(elementsList[3])
        b = int(elementsList[4])
        c = int(elementsList[5])
        d = int(elementsList[6])
        x = np.arange(xmin,xmax+1,1) # xmax +1 para que incluya el valor xmax
        y = sustitutoFuzzy(x, [a, b, c, d])
        fuzzySet.x = x
        fuzzySet.y = y
        fuzzySetsDict.update( { setid : fuzzySet } )

        line = inputFile.readline()
    inputFile.close()
    return fuzzySetsDict

'''Esta función es una sustituta el import de la función de la librería 
skfuzzy, que estaba anteriormente en el código. La función skfuzzy.trimf 
hace lo mismo que esto'''
def sustitutoFuzzy(x, abcd):
    a, b, c, d = abcd
    y = np.zeros(len(x))
    y[(a < x) & (x < b)] = (x[(a < x) & (x < b)] - a) / (b - a)
    y[(b <= x) & (x <= c)] = 1
    y[(c < x) & (x < d)] = (d - x[(c < x) & (x < d)]) / (d - c)
    return y

'''Hace lo mismo que la siguiente función, solo que con Rules.txt. 
rules, es lo que devuelve que es una lista de muchas rule. Una rule esta 
compuesta de un nombre, un antecedente y un consecuente. El antecedente es 
una lista de strings y el consecuente es un string. Por ejemplo, 
si el archivo tiene la siguiente línea: 
Rule05, Risk=HighR, Age=Young, Amount=Big;
la rule será un objeto con los siguientes valores:
ruleName = 'Rule05', antecedent = ['Age=Young', 'Amount=Big'], 
                    consecuent = 'Risk=HighR' '''
def readRulesFile():
    inputFile = open('Files/Rules.txt', 'r')
    rules = RuleList()
    line = inputFile.readline()
    while line != '':
        rule = Rule()
        line = line.rstrip()
        elementsList = line.split(', ')
        rule.ruleName = elementsList[0]
        rule.consequent = elementsList[1]
        lhs = []
        for i in range(2, len(elementsList), 1):
            lhs.append(elementsList[i])
        rule.antecedent = lhs
        rules.append(rule)
        line = inputFile.readline()
    inputFile.close()
    return rules


'''Esta función lee el archivo de aplications.txt y devuelve una lista de 
objetos de la clase Application. Esa lista contiene tantos objetos como 
filas haya en el archivo. Cada objeto Application contiene un identificador,
y una lista de pares de valores, cada par de valores contiene un nombre de a lo que se refiere el valor 
y el valor en sí. Por ejemplo, si el archivo contiene la siguiente línea: 
0001, Age, 35, IncomeLevel, 82, Assets, 38, Amount, 8, Job, 0, History, 1, 
se almacenará en la lista de objetos de la clase Application un objeto con los siguientes valores:
appId = '0001', lista = [['Age', 35], ['IncomeLevel', 82], ['Assets', 38], ['Amount', 8], ['Job', 0], ['History', 1]]'''
def readApplicationsFile():
    inputFile = open('Files/Applications.txt', 'r')
    applicationList = []
    line = inputFile.readline()
    while line != '':
        elementsList = line.split(', ')
        app = Application()
        app.appId = elementsList[0]
        app.data = []
        for i in range(1, len(elementsList), 2):
            app.data.append([elementsList[i], int(elementsList[i+1])])
        applicationList.append(app)
        line = inputFile.readline()
    inputFile.close()
    return applicationList

def readApplicationsAux():
    inputFile = open('Files/AuxiliaryApplications.txt', 'r')
    applicationList = []
    line = inputFile.readline()
    while line != '':
        elementsList = line.split(', ')
        app = Application()
        app.appId = elementsList[0]
        app.data = []
        for i in range(1, len(elementsList), 2):
            app.data.append([elementsList[i], elementsList[i+1]])
        applicationList.append(app)
        line = inputFile.readline()
    inputFile.close()
    return applicationList