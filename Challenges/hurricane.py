# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages():
    for damage_data in damages:
        if damage_data == "Damages not recorded":
            pass
        else:
            if damage_data.endswith("M"):
                damages[damages.index(damage_data)] = float(damage_data[:len(damage_data)-1]) * conversion["M"]
            else:
                damages[damages.index(damage_data)]  = float(damage_data[:len(damage_data)-1]) * conversion["B"]


# test function by updating damages

update_damages()
# print(damages)

# 2 
# Create a Table


def construct_hurricane_dict():
    #zip all lists(not as a list of tuples but as a list of lists)
    zipped_lists = [list(a) for a in zip(names, months,years,max_sustained_winds,areas_affected,damages, deaths)]
    # list for key values
    key_list = ["Name","Month","Year","Max Sustained Wind","Areas Affected","Damage","Death"]
    # an empty list to store constructed dictionaries
    main_list = []
    #loop zipped lists and zip them with key_list values in dictionary
    for x in zipped_lists:
        main_list.append({key:value for key, value in zip(key_list,x)})  
    hurricane_dict = {key:value for key, value in zip(names, main_list)}
    
    return hurricane_dict



# Create and view the hurricanes dictionary

hurricanes = construct_hurricane_dict()

#print(hurricanes)


# 3
# Organizing by Year
def organize_by_year():
    main_list = []
    for index in range(len(years)):
        temp_list = []
        for value in hurricanes.values():
            if value["Year"] == years[index]:
                temp_list.append(value)
            else:
                pass
        main_list.append(temp_list)
    
    return {key:value for key, value in zip(years, main_list)}



hurricanes_by_year = organize_by_year()

#print(hurricanes_by_year)

# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas
def count_damaged_areas():
    damage_count = {}
    for area_list in areas_affected:
        for area in area_list:
            if area not in damage_count:
                damage_count[area] = 0
            else:
                pass

    for value in hurricanes_by_year.values():
        for hurricane in value:
            for x in hurricane["Areas Affected"]:
                damage_count[x] += 1
    
    return damage_count


damage_count_dict = count_damaged_areas()
print(damage_count_dict)

            
# create dictionary of areas to store the number of hurricanes involved in


# 5 
# Calculating Maximum Hurricane Count
def get_most_frequent_area():
    score_list = [["Dummy Var",0]]
    for key, value in damage_count_dict.items():
        if value > score_list[-1][1]:
            score_list.append([key,value])
        else:
            pass
    print(score_list[-1][0] + " was hit by hurricanes for " + str(score_list[-1][1]) + " times which makes it the most!")


get_most_frequent_area()

# find most frequently affected area and the number of hurricanes involved in



# 6
# Calculating the Deadliest Hurricane

def get_most_death():
    score_list = [["Dummy Var",0]]
    for value in hurricanes_by_year.values():
        for hurricane in value:
            if hurricane["Death"] > score_list[-1][1]:
                score_list.append([hurricane["Name"], hurricane["Death"]])
            else:
                score_list.insert(0, [hurricane["Name"],hurricane["Death"]])
    score_list.remove(["Dummy Var",0])
    print("Deadliest hurricane was " + score_list[-1][0] + " with " + str(score_list[-1][1]) + " deaths.")
    return score_list


# find highest mortality hurricane and the number of deaths

score_list = get_most_death()
# 7
# Rating Hurricanes by Mortality

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key

def mortality_rating():
    mortality_dict = {}
    for x in range(6):
        mortality_dict[x] = []
    
    for x in range(len(score_list)):
        if score_list[x][1] < mortality_scale[0]:
            mortality_dict[0].append({score_list[x][0]:score_list[x][1]})

        elif score_list[x][1] < mortality_scale[1]:
            mortality_dict[1].append({score_list[x][0]:score_list[x][1]})

        elif score_list[x][1] < mortality_scale[2]:
            mortality_dict[2].append({score_list[x][0]:score_list[x][1]})
        elif score_list[x][1] < mortality_scale[3]:
            mortality_dict[3].append({score_list[x][0]:score_list[x][1]})

        elif score_list[x][1] < mortality_scale[4]:
            mortality_dict[4].append({score_list[x][0]:score_list[x][1]})

        else:
            mortality_dict[5].append({score_list[x][0]:score_list[x][1]})
    
    print(mortality_dict)
    return mortality_dict
    
mortality_rating()
# 8 Calculating Hurricane Maximum Damage

def get_most_damage():
    score_list = [["Dummy Var",0]]
    for value in hurricanes_by_year.values():
        for hurricane in value:
            if hurricane["Damage"] == "Damages not recorded":
                score_list.insert(0,[hurricane["Name"], hurricane["Damage"]])
            elif hurricane["Damage"] > score_list[-1][1]:
                score_list.append([hurricane["Name"], hurricane["Damage"]])
            else:
                score_list.insert(0, [hurricane["Name"], hurricane["Damage"]])
    score_list.remove(["Dummy Var",0])
    print("The hurricane caused the most damage was " + score_list[-1][0] + " with " + str(score_list[-1][1]) + " dollars.")
    return score_list

# find highest damage inducing hurricane and its total cost
damage_list = get_most_damage()

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def damage_rating():
    damage_dict = {}
    for x in range(6):
        damage_dict[x] = []
    
    for x in range(len(damage_list)):
        try:
            if damage_list[x][1] <= damage_scale[0]:
                damage_dict[0].append({damage_list[x][0]:damage_list[x][1]})

            elif damage_list[x][1] < damage_scale[1]:
                damage_dict[1].append({damage_list[x][0]:damage_list[x][1]})

            elif damage_list[x][1] < damage_scale[2]:
                damage_dict[2].append({damage_list[x][0]:damage_list[x][1]})
            elif damage_list[x][1] < damage_scale[3]:
                damage_dict[3].append({damage_list[x][0]:damage_list[x][1]})

            elif damage_list[x][1] < damage_scale[4]:
                damage_dict[4].append({damage_list[x][0]:damage_list[x][1]})

            else:
                damage_dict[5].append({damage_list[x][0]:damage_list[x][1]})
        except:
            damage_dict[0].append({damage_list[x][0]:damage_list[x][1]})

            
    
    print(damage_dict)

damage_rating()