# Finish the uefaEuro2016() function so it return string just like in the examples below:

# uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
# uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
# uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."

def uefa_euro_2016(teams, scores):
    if scores[0] == scores[1]:
        result = "teams played draw."
    elif scores[0] > scores[1]:
        result = f'{teams[0]} won!'
    else:
        result = f'{teams[1]} won!'
    
    return f'At match {teams[0]} - {teams[1]}, ' + result
