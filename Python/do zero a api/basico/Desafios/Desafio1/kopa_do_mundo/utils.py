from datetime import datetime
from .exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError

DATE_FORMAT = '%Y-%m-%d'

def data_processing(team:dict):
    
    if team['titles'] < 0:
        raise NegativeTitlesError('titles cannot be negative')
    
    ano_atual = datetime.now().year
    
    cup_years = [1930, 1934, 1938, 1950] + list(range(1954, ano_atual+1, 4))
    
    first_cup_year = datetime.strptime(team['first_cup'], DATE_FORMAT).year
    
    if first_cup_year not in cup_years:
        raise InvalidYearCupError('there was no world cup this year')
    
    index_of_cup = cup_years.index(first_cup_year)
    
    
    if team['titles'] > len(cup_years[index_of_cup::]):
        raise ImpossibleTitlesError('impossible to have more titles than disputed cups')
    
    return team
        