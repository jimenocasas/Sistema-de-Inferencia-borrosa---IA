import matplotlib.pyplot as plt
from MFIS_Read_Functions import readFuzzySetsFile
from MFIS_Read_Functions import readRulesFile, readApplicationsFile, readApplicationsAux
import numpy as np
from MFIS_Read_Functions import readRulesFile

'''def check_rules(application_data):
    # Lee las reglas
    rules = readRulesFile()

    # Para cada regla
    for rule in rules:
        # Cuenta el número de antecedentes de la regla que se cumplen en la aplicación
        antecedents_met = sum([any([pair[0] == antecedent.split('=')[0] and pair[1] == antecedent.split('=')[1] for pair in application_data]) for antecedent in rule.antecedent])
        # Si todos los antecedentes de la regla se cumplen
        if antecedents_met == len(rule.antecedent):
            # Imprime la regla y termina la búsqueda
            print(f'La regla que controla los antecedentes proporcionados es: {rule.ruleName}, {rule.consequent}')
            return

    print('No se encontró ninguna regla que controle todos los antecedentes proporcionados.')

# Datos de la aplicación
application_data = [['Age', 'Young'], ['IncomeLevel', 'Hig'], ['Assets',
                                                           'Moderate'],
                    ['Amount', 'Medium'], ['Job', 'Stable'], ['History',
                                                             'Good']]

# Llama a la función
check_rules(application_data)'''

def generate_fuzzy_graphs():
    # Lee los conjuntos difusos
    fuzzySetsDict1 = readFuzzySetsFile('Files/InputVarSets.txt')
    fuzzySetsDict2 = readFuzzySetsFile('Files/Risks.txt')

    # Combina los dos diccionarios en uno
    fuzzySetsDict = {**fuzzySetsDict1, **fuzzySetsDict2}

    # Inicializa la lista de variables graficadas
    plotted_vars = []

    # Para cada conjunto difuso, genera una gráfica
    for setid, fuzzySet in fuzzySetsDict.items():
        # Si la variable no ha sido graficada, crea una nueva figura
        if fuzzySet.var not in plotted_vars:
            if plotted_vars:
                plt.xlabel(plotted_vars[-1])
                plt.ylabel('Membership Degree')
                plt.grid(True)
                plt.legend()
                plt.show()
            plt.figure()
            plotted_vars.append(fuzzySet.var)
        plt.plot(fuzzySet.x, fuzzySet.y, label=fuzzySet.label)

    # Muestra la última figura
    if plotted_vars:
        plt.xlabel(plotted_vars[-1])
        plt.ylabel('Membership Degree')
        plt.grid(True)
        plt.legend()
        plt.show()


def tranformacion_numeros_Applications():
    # Lee los conjuntos difusos
    fuzzySetsDict = readFuzzySetsFile('Files/InputVarSets.txt')

    # Crea un diccionario que mapea cada variable a sus conjuntos difusos
    var_to_sets = {}
    for setid, fuzzySet in fuzzySetsDict.items():
        if fuzzySet.var not in var_to_sets:
            var_to_sets[fuzzySet.var] = []
        var_to_sets[fuzzySet.var].append(fuzzySet)

    # Lee las aplicaciones
    applications = readApplicationsFile()

    # Abre el archivo auxiliar
    with open('Files/AuxiliaryApplications.txt', 'w') as aux_file:
        # Para cada aplicación
        for app in applications:
            # Para cada par de valores en la aplicación
            for pair in app.data:
                var, value = pair
                # Encuentra el conjunto difuso que tiene el mayor grado de membresía para el valor
                max_mem_degree = -1
                max_mem_set = None
                for fuzzySet in var_to_sets[var]:
                    if min(fuzzySet.x) <= value <= max(fuzzySet.x):
                        # Encuentra el índice del valor más cercano en fuzzySet.x a value
                        closest_index = np.argmin(np.abs(np.array(fuzzySet.x) - value))
                        mem_degree = fuzzySet.y[closest_index]
                        # Si el valor es el límite superior, también considera el grado de membresía del valor anterior
                        if value == max(fuzzySet.x) and closest_index > 0:
                            mem_degree = max(mem_degree, fuzzySet.y[
                                closest_index - 1])
                        if mem_degree > max_mem_degree:
                            max_mem_degree = mem_degree
                            max_mem_set = fuzzySet
                # Reemplaza el valor con el label del conjunto difuso con el mayor grado de membresía
                if max_mem_set is not None:
                    pair[1] = max_mem_set.label
            # Escribe la aplicación modificada en el archivo auxiliar
            aux_file.write(f'{app.appId}, ' + ', '.join([f'{pair[0]}, {pair[1]}' for pair in app.data]) + '\n')

'''def generate_results():
    # Lee las aplicaciones
    applications = readApplicationsAux()

    # Lee las reglas
    rules = readRulesFile()

    # Abre el archivo de resultados
    with open('Files/Results.txt', 'w') as results_file:
        # Para cada aplicación
        for app in applications:
            # Para cada regla
            for rule in rules:
                # Cuenta el número de antecedentes de la regla que se cumplen en la aplicación
                antecedents_met = sum([any([pair[0] == antecedent.split('=')[0] and pair[1] == antecedent.split('=')[1] for pair in app.data]) for antecedent in rule.antecedent])
                # Si todos los antecedentes de la regla se cumplen
                if antecedents_met == len(rule.antecedent):
                    # Escribe el identificador de la aplicación y el consecuente de la regla en el archivo de resultados
                    results_file.write(f'{app.appId}, {rule.consequent}\n')
                    # Salta a la siguiente aplicación
                    break'''

# Llama a la función
'''tranformacion_numeros_Applications()
generate_results()
'''

from MFIS_Read_Functions import readApplicationsAux, readRulesFile

def check_rules(application_data):
    # Lee las reglas
    rules = readRulesFile()

    # Define la jerarquía de riesgos
    risk_hierarchy = {'LowR': 0, 'MediumR': 1, 'HighR': 2}

    # Inicializa la regla con el riesgo más alto
    highest_risk_rule = None
    highest_risk = -1

    # Para cada regla
    for rule in rules:
        # Cuenta el número de antecedentes de la regla que se cumplen en la aplicación
        antecedents_met = sum([any([pair[0] == antecedent.split('=')[0] and pair[1] == antecedent.split('=')[1] for pair in application_data]) for antecedent in rule.antecedent])
        # Si todos los antecedentes de la regla se cumplen
        if antecedents_met == len(rule.antecedent):
            # Si la regla tiene un riesgo más alto que la regla actualmente registrada
            if risk_hierarchy[rule.consequent.split('=')[1]] > highest_risk:
                # Actualiza la regla registrada y el riesgo más alto
                highest_risk_rule = rule
                highest_risk = risk_hierarchy[rule.consequent.split('=')[1]]

    # Devuelve la regla con el riesgo más alto
    return highest_risk_rule

def generate_results():
    # Lee las aplicaciones
    applications = readApplicationsAux()

    # Abre el archivo de resultados
    with open('Files/Results.txt', 'w') as results_file:
        # Para cada aplicación
        for app in applications:
            # Comprueba las reglas
            rule = check_rules(app.data)
            # Si se encontró una regla
            if rule is not None:
                # Escribe el identificador de la aplicación y el consecuente de la regla en el archivo de resultados
                results_file.write(f'{app.appId}, {rule.consequent}\n')
            else:
                # Escribe un mensaje de error en el archivo de resultados
                results_file.write(f'{app.appId}, Error: No rule found\n')

# Llama a la función
tranformacion_numeros_Applications()
generate_results()