import random

def create_npc(json_input, context):
    allRaces=['Dwarf','Elf','Human','Halfling','Gnome','Dragonborn','Tiefling','Air Genasi','Water Genasi','Earth Genasi','Fire Genasi','Half-Orc','Half-Elf']
    allBackgrounds=['Acolyte','Charlatan','City Watch','Clan Crafter','Cloistered Scholar','Courtier','Criminal','Entertainer','Faction Agent','Far Traveler','Folk Hero','Guild Artisan','Hermit','Inheritor','Knight of the Order','Mercenary Veteran','Noble','Outlander','Sage','Sailor','Soldier','Urban Bounty Hunter','Uthgardt Tribe Member','Waterdhavian Noble']
    allClasses=['Acolyte','Archmage','Assassin','Bandit','Bandit Captain','Berserker','Commoner','Cult Fanatic','Cultist','Druid','Gladiator','Guard','Knight','Mage','Noble','Priest','Scout','Spy','Thug','Tribal Warrior','Veteran']

    info=[random.choice(allBackgrounds),random.choice(allRaces),random.choice(allClasses)]
    statBlock = str("Background: {}\nRace: {}\nClass: {}".format(info[0],info[1],info[2]))
    return {
    'statusCode': 200,
    'headers': { 'Content-Type': 'application/json' },
    'body': statBlock
    }