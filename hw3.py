import county_demographics
import build_data
import data
import math

#part 1
'''Part 1 takes the population of each county and adds it up to get a total. This is done by
taking each county in the list, and adding it to the total counter. It does this for each county
from the date 2014 which is called, and then returns the total of the population combined.'''
def population_total(countys : list[data.CountyDemographics])->int:
    total = 0
    for i in range(len(countys)):
        total += countys[i].population["2014 Population"]
    return total

#part 2
'''The goal of this function is to look through the list of countys that are available in the list and check
if they are from the selected state that was chosen. If they are, they are added to the list of countys that are
also in that state selected'''
def filter_by_state(county_list : list[data.CountyDemographics], state : str)->list[data.CountyDemographics]:
    new_list = []
    for i in range(len(county_list)):
        if county_list[i].state == state:
            new_list.append(county_list[i])
    return new_list

#part 3
'''All three of these functions do the same exact thing just with different data. It takes the list of countys
and will check for certain characteristics that the user is searching for. If they are found they are added to
population total and then returned when the entire list of countys is run through'''
def population_by_education(countys : list[data.CountyDemographics], ed : str)->int:
    total = 0
    for i in range(len(countys)):
        county_total = (countys[i].education[ed]/100)*countys[i].population["2014 Population"]
        total += county_total
    total = math.floor(total)
    return total

def population_by_ethnicity(countys : list[data.CountyDemographics], ethnicity : str)->int:
    total = 0
    for i in range(len(countys)):
        county_total = (countys[i].ethnicities[ethnicity] / 100) * countys[i].population["2014 Population"]
        total += county_total
    total = math.floor(total)
    return total

def population_below_poverty_line(countys : list[data.CountyDemographics], poverty : str)->int:
    total = 0
    for i in range(len(countys)):
        county_total = (countys[i].income[poverty] / 100) * countys[i].population["2014 Population"]
        total += county_total
    total = math.floor(total)
    return total

#part 4
'''These functions just like part 3 all do roughly the same thing. They each pull info for certain
groupings of things about countys. They will call the population of the certain grouping from earlier
and will check the percentage of people that are that type for the total population of all
countys'''
def percent_by_education(countys : list[data.CountyDemographics], education : str)->int:
    total = 0
    total += (population_by_education(countys,education)/population_total(countys))*100
    return total
def percent_by_ethnicity(countys : list[data.CountyDemographics], ethnicity : str)->int:
    total = 0
    total += (population_by_ethnicity(countys, ethnicity) / population_total(countys))*100
    return total
def percent_below_poverty_line(countys : list[data.CountyDemographics], below_pov : str)->int:
    total = 0
    total += (population_below_poverty_line(countys, below_pov) / population_total(countys))*100
    return total

#part 5
'''These functions will take the list of countys and check that the education requirment is either greater than
or less than what the county has. If it is greater than, and the call is from education greater than, then the 
county will be added. If the county has a lesser education than the input, then it will be added to the list
if the less than is called. it then returns the new list'''
def education_greater_than(countys : list[data.CountyDemographics], ed : str, val:float)->list[data.CountyDemographics]:
    list = []
    for i in range(len(countys)):
        if countys[i].education[ed] > val:
            list.append(countys[i])
    return list
def education_less_than(countys : list[data.CountyDemographics], ed : str, val:float)->list[data.CountyDemographics]:
    list = []
    for i in range(len(countys)):
        if countys[i].education[ed] < val:
            list.append(countys[i])
    return list
'''These functions will check if the ethnicity value for each county and will sort it if it is greater than
or less than the provided input depending on which one is called. it then returns the new list'''
def ethnicity_greater_than(countys : list[data.CountyDemographics], et : str, val:float)->list[data.CountyDemographics]:
    list = []
    for i in range(len(countys)):
        if countys[i].ethnicities[et] > val:
            list.append(countys[i])
    return list
def ethnicity_less_than(countys : list[data.CountyDemographics], et : str, val:float)->list[data.CountyDemographics]:
    list = []
    for i in range(len(countys)):
        if countys[i].ethnicities[et] < val:
            list.append(countys[i])
    return list
'''These functions will check if the poverty line is greater than or less than the inputed value. It will check the poverty line
for each of the countys in the list. It will then sort it in to either greater than or less than lists depending on the function
that is called. Once this happens, the list is returned'''
def below_poverty_line_greater_than(countys : list[data.CountyDemographics], pov : str, val:float)->list[data.CountyDemographics]:
    list = []
    for i in range(len(countys)):
        if countys[i].income[pov] > val:
            list.append(countys[i])
    return list
def below_poverty_line_less_than(countys : list[data.CountyDemographics], pov : str, val:float)->list[data.CountyDemographics]:
    list = []
    for i in range(len(countys)):
        if countys[i].income[pov] < val:
            list.append(countys[i])
    return list


