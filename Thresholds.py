import json


## Offense
offense_champion = "Katarina"
offense_items = ["Boots", '']
offense_level = 18
physical_Damage_Raw = 100


## Defense
defense_champion = "Syndra"
defense_items = ["Boots", '']
defense_level = 18


#Amor formula
def main():
    #Defense level/health/amor/mr
    defense_champion_Data = get_champion_Data(defense_champion)
    defense_stats_At_Level = get_stats_At_Level(defense_champion_Data, defense_level)

    #Offense level/abilities/ability power/attack damage
    offense_champion_Data = get_champion_Data(offense_champion)
    offense_stats_At_Level = get_stats_At_Level(offense_champion_Data, offense_level)
    offense_abilities_At_Level = get_abilities_At_Level(offense_champion_Data, offense_stats_At_Level, offense_level)



    #print(defense_champion, "\n", defense_stats_At_Level, "\n", offense_champion, "\n", offense_stats_At_Level)





    #Physical Damage Calculation
    # physical_Damage_Post_Mitigation = get_physical_Damage_Post_Mitigation(defense_stats_At_Level["armor"], physical_Damage_Raw)


    # print(physical_Damage_Post_Mitigation)

    return




# def get_physical_Damage_Post_Mitigation(armor, physical_Damage_Raw):

#     if armor >= 0:
#         physical_Damage_Post_Mitigation = physical_Damage_Raw * (100/(100 + armor))
#     else:
#         physical_Damage_Post_Mitigation = physical_Damage_Raw * (2 - (100/(100-armor)))



#     return physical_Damage_Post_Mitigation



def get_champion_Data(champion):

    champions_json = open('champions.json', encoding='utf-8')

    champions_Data = json.load(champions_json)

    champion_Data = champions_Data[champion]

    return champion_Data


def get_stats_At_Level(champion_Data, level):
    stats_At_Level = {}

    for stat_name, stat_data in champion_Data["stats"].items():
        flat = stat_data["flat"] + (stat_data["perLevel"] * level)
        percent = stat_data["percent"] + (stat_data["percentPerLevel"] * level)
        stat_At_Level = round(flat + (percent * flat), 2)
        stats_At_Level[stat_name] = stat_At_Level

    return stats_At_Level

def get_abilities_At_Level(champion_Data, stats_At_Level, level):
    abilities_At_Level = []
    skill_points = 5 - 1 
    for ability_name, ability_data in champion_Data["abilities"].items():
        damage_Sum = 0
        if isinstance(ability_data["effects"], (list, tuple)):
            for effect in ability_data["effects"]:  # Iterate over each effect
                if "leveling" in effect and "modifiers" in effect["leveling"]:
                    for modifier in effect["leveling"]["modifiers"]:
                        if modifier["units"] == "":
                            damage_Sum += modifier["values"][skill_points - 1]
                        elif modifier["units"] == "% AP":
                            damage_Sum += modifier["values"][skill_points - 1] * stats_At_Level["ap"]
                        elif modifier["units"] == "% AD":
                            damage_Sum += modifier["values"][skill_points - 1] * stats_At_Level["ad"]
        else:
            print(f"Unexpected structure in effects for ability {ability_name}: {ability_data['effects']}")

        
    print(abilities_At_Level)
        
        
        
        
    abilities_At_Level[ability] = 0








    
    return abilities_At_Level



def get_item_Stats(item):
    return









main()