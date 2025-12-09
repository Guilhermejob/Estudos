from datetime import datetime, timedelta

from exeptinons import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


DATE_FORMAT = '%Y-%m-%d'

data_1 = {
    'name':'França',
    'titles':-2,
    'top_scorer':'Zidane',
    'fifa_code':'FRA',
    'first_cup':'1911-10-18'
}

data_2 = {
    'name':'França',
    'titles':2,
    'top_scorer':'Zidane',
    'fifa_code':'FRA',
    'first_cup':'2000-10-18'
}

data_3 = {
    'name':'França',
    'titles':9,
    'top_scorer':'Zidane',
    'fifa_code':'FRA',
    'first_cup':'2002-10-18'
}




def data_processing(team:dict):
    
    if team['titles'] < 0:
        raise NegativeTitlesError('titles cannot be negative')
    
    ano_atual = datetime.now().year
    
    cup_years = [ano for ano in range(1930, ano_atual+1, 4)]
    
    first_cup_year = datetime.strptime(team['first_cup'], DATE_FORMAT).year
    
    if first_cup_year not in cup_years:
        raise InvalidYearCupError('There was no world cup this year')
    
    index_of_cup = cup_years.index(first_cup_year)
    
    
    if team['titles'] > len(cup_years[index_of_cup::]):
        raise ImpossibleTitlesError('impossible to have more titles than disputed cups')
        
        

    
    
try:
    data_processing(data_1)
except NegativeTitlesError as err:
    print(err.message)
except InvalidYearCupError as err:
    print(err.message)
except ImpossibleTitlesError as err:
    print(err.message)
    
try:
    data_processing(data_2)
except NegativeTitlesError as err:
    print(err.message)
except InvalidYearCupError as err:
    print(err.message)
except ImpossibleTitlesError as err:
    print(err.message)
    
try:
    data_processing(data_3)
except NegativeTitlesError as err:
    print(err.message)
except InvalidYearCupError as err:
    print(err.message)
except ImpossibleTitlesError as err:
    print(err.message)    
    