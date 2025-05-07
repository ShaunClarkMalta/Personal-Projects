import random
import os

#Declare and Create the Tuples containing the spells by Class and Level.
#These will be turned into a full archive as nested tuples
#Need to add the rest of the spells

#Artificer Class
artificer_lv1 = ("Absorb Elements", "Alarm", "Catapult", "Cure Wounds", "Detect Magic", "Disguise Self", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Grease", "Identify", "Jump", "Longstrider", "Purify Food And Drink", "Sanctuary", "Snare", "Tasha's Caustic Brew")
artificer_lv2 = ("Aid", "Air Bubble", "Alter Self", "Arcane Lock", "Blur", "Continual Flame", "Darkvision", "Enhance Ability", "Enlarge/Reduce", "Heat Metal", "Invisibility", "Kinetic Jaunt", "Lesser Restoration", "Levitate", "Magic Mouth", "Magic Weapon", "Protection from Poison", "Pyrotechnics", "Rope Trick", "See Invisibility", "Skywrite", "Spider Climb", "Vortex Warp", "Web")
artificer_lv3 = ()
artificer_spelllist = (artificer_lv1, artificer_lv2, artificer_lv3)

#Bard Class
bard_lv1 = ("Animal Friendship", "Bane", "Charm Person", "Color Spray", "Command", "Comprehend Languages", "Creeping Touch", "Cure Wounds", "Daydream", "Detect Magic", "Disguise Self", "Dissonant Whispers", "Distort Value", "Earth Tremor", "Elf Shot", "Faerie Fire", "Feather Fall", "Healing Word", "Heroism", "Identify", "Illusory Script", "Longstrider", "Pratfall", "Silent Image", "Silvery Barbs", "Sleep", "Speak with Animals", "Tashas Hideous Laughter", "Thunderwave", "Unseen Servant")
bard_lv2 = ("Aid", "Animal Messenger", "Blindness/Deafness", "Borrowed Knowledge", "Calm Emotions", "Cloud Of Daggers", "Crown of Madness", "Detect Thoughts", "Drayfns Blunted Blade", "Dreamwalk", "Enhance Ability", "Enlarge/Reduce", "Enthrall", "Gift Of Gab", "Heat Metal", "Hold Person", "Invisibility", "Kinetic Jaunt", "Knock", "Lesser Restoration", "Locate Animals Or Plants", "Locate Object", "Magic Mouth", "Mirror Image", "Nathairs Mischief", "Ominous Winds", "Phantasmal Force", "Pyrotechnics", "See Invisibility", "Shatter", "Silence", "Skywrite", "Spray Of Cards", "Suggestion", "Ugly Duckling", "Warding Wind", "Zone Of Truth")
bard_lv3 = ()
bard_spelllist = (bard_lv1, bard_lv2, bard_lv3)

#Cleric Class
cleric_lv1 = ("Bane", "Bless", "Ceremony", "Command", "Create Or Destroy Water", "Cure Wounds", "Detect Evil And Good", "Detect Magic", "Detect Poison And Disease", "Elevated Sight", "Fireflies", "Guiding Bolt", "Healing Word", "Inflict Wounds", "Protection From Evil And Good", "Purify Food And Drink", "Sanctuary", "Shield Of Faith")
cleric_lv2 = ("Aid", "Augury", "Blindness/Deafness","Bloodletter", "Borrowed Knowledge", "Calm Emotions", "Continual Flame", "Drayfns Blunted Blade", "Enhance Ability", "Find Traps", "Gentle Repose", "Hold Person", "Lesser Restoration", "Life Tether", "Locate Object", "Ominous Winds", "Protection", "Shielding Word", "Prayer of Healing", "Preserve")
cleric_lv3 = ()
cleric_spelllist = (cleric_lv1, cleric_lv2, cleric_lv3)

#Druid Class
druid_lv1 = ("Absorb Elements", "Animal Friendship", "Beast Bond", "Charm Person", "Create Or Destroy Water", "Cure Wounds", "Daydream", "Detect Magic", "Detect Poison and Disease", "Earth Tremor", "Elevated Sight", "Entangle", "Faerie Fire", "Fireflies", "Fog Cloud", "Goodberry", "Healing Word", "Ice Knife", "Jump", "Longstrider", "Protection From Evil And Good", "Purify Food And Drink", "Snare", "Speak With Animals", "Spint Shield", "Thunderwave", "Veil of Dusk")
druid_lv2 = ("Aid", "Air Bubble", "Animal Messenger", "Augury", "Barkskin", "Beast Sense", "Continual Flame", "Darkvision", "Dreamwalk", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/ Reduce", "Find Traps", "Flame Blade", "Flaming Sphere", "Gust Of Wind", "Healing Spirit", "Heat Metal", "Hibernation", "Hold Person", "Krails Maggot", "Krails Rapture", "Lesser Restoration", "Locate Animals Or Plants", "Locate Object", "Moonbeam", "Ominous Winds", "Pass Without Trace", "Protection", "Protection From Poison", "Riptide", "Skywrite", "Spike Growth", "Summon Beast", "Warding Wind", "Wither And Bloom")
druid_lv3 = ()
druid_spelllist = (druid_lv1, druid_lv2, druid_lv3)

#Paladin Class
paladin_lv1 = ("Blade Of Blood And Bone", "Bless", "Ceremony", "Command", "Compelled Duel", "Cure Wounds", "Detect Evil And Good", "Detect Magic", "Detect Poison And Disease", "Divine Favor", "Divine Smite", "Heroism", "Protection From Evil And Good", "Purify Food And Drink", "Searing Smite", "Shield of Faith", "Thunderous Smite", "Wrathful Smite")
paladin_lv2 = ("Aid", "Bloodletter", "Drayfns Blunted Blade", "Find Steed", "Gentle Repose", "Krails Rupture", "Lesser Restoration", "Locate Object", "Magic Weapon", "Prayer of Healing", "Protection", "Protection From Poison", "Shielding Word", "Shining Smite", "Warding Bond", "Zone Of Truth")
paladin_lv3 = ()
paladin_spelllist = (paladin_lv1, paladin_lv2, paladin_lv3)

#Ranger
ranger_lv1 = ("Absorb Elements", "Air Bubble", "Alarm", "Animal Friendship", "Beast Bond", "Blade Of Blood And Bone", "Cure Wounds", "Detect Magic", "Detect Poison And Disease", "Elevated Sight", "Ensnaring Strike", "Entangle", "Fog Cloud", "Goodberry", "Hail Of Thorns", "Hunters Mark", "Jump", "Longstrider", "Snare", "Speak With Animals", "Spiny Shield", "Zephyr Strike")
ranger_lv2 = ("Aid", "Air Bubble", "Ambush Prey", "Animal Messenger", "Barkskin", "Beast Sense", "Bloodsense", "Cordon Of Arrows", "Darkvision", "Drayfns Blunted Blade", "Dreamwalk", "Enhance Ability", "Find Traps", "Gust Of Wind", "Healing Spirit", "Hibernation", "Krails Maggot", "Krails Rupture", "Lesser Restoration", "Locate Animals Or Plants", "Locate Object", "Magic Weapon", "Pass Without Trace", "Protection", "Protection From Poison", "Silence", "Spike Growth", "Summon Beast")
ranger_lv3 = ()
ranger_spelllist = (ranger_lv1, ranger_lv2, ranger_lv3)

#Sorcerer
sorcerer_lv1 = ("Absorb Elements", "Black Ribbons", "Burning Hands", "Catapult", "Chaos Bolt", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Creeping Touch", "Delerium Orb", "Detect Magic", "Disguise Self", "Earth Tremor", "Elf Shot", "Expeditious Retreat", "False Life", "Feather Fall", "Fog Cloud", "Gloaming", "Grease", "Ice Knife", "Jump", "Mage Armor", "Magic Missile", "Pratfall", "Ray Of Sickness", "Shadow Armor", "Shield", "Silent Image", "Silvery Barbs", "Sleep", "Spiny Shield", "Tashas Caustic Brew", "Thunderwave", "Witch Bolt")
sorcerer_lv2 = ("Agnazzars Scorcher", "Air Bubble", "Alter Self", "Arcane Vigor", "Blindness/Deafness", "Blur", "Cloud Of Daggers", "Crown Of Madness", "Dark Path", "Darkbolt", "Darkness", "Darkvision", "Detect Thoughts", "Dragons Breath", "Drayfns Blunted Blade", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/Reduce", "Flame Blade", "Flaming Sphere", "Gust Of Wind", "Hold Person", "Invisibility", "Kinetic Jaunt", "Knock", "Krails Rupture", "Levitate", "Life Tether","Magic Weapon", "Maximilians Earthen Grasp", "Mind Spike", "Mirror Image", "Misty Step", "Nathairs Mischief", "Negative Image", "Ominous Winds", "Phantasmal Force", "Pyrotechnics", "Rimes Binding Ice", "Riptide", "Scorching Ray", "See Invisibility", "Shadow Adaptation", "Shadow Puppets", "Shatter", "Shielding Word", "Snillocs Snowball Swarm", "Spider Vlimb", "Spray Of Cards", "Suggestion", "Tashas Mind Whip", "Ugly Duckling", "Vortex Warp", "Warding Wind","Warp Bolt", "Warp Sense", "Web", "Wither And Bloom")
sorcerer_lv3 = ()
sorcerer_spelllist = (sorcerer_lv1, sorcerer_lv2, sorcerer_lv3)

#Warlock
warlock_lv1 = ("Armor Of Agathys", "Arms Of Hadar", "bane", "Black Ribbons", "Blade of Blood And Bone", "Cause Fear", "Charm Person", "Comprehend Languages", "Creeping Touch", "Daydream", "Delerium Orb", "Detect Magic", "Elevated Sight", "Expeditious Retreat", "Gloaming", "Hellish Rebuke", "Hex", "Illusory Script", "Peppermint Plate", "Pratfall", "Protection From Evil And Good", "Shadow Armor", "Shadow Hands", "Speak With Animals", "Tashas Hideous Laughter", "Unseen Servant", "Veil Of Dusk", "Witch Bolt")
warlock_lv2 = ("Borrowed Knowledge", "Cloud of Daggers", "Crown of Madness", "Dark Path", "Darkbolt", "Darkness", "Drayfns Blunted Blade", "Dreamwalk", "Earthbind", "Enthrall", "Flock Of Familiars", "Hold Person", "Invisibility", "Krais Maggot", "Krails Rupture", "Life Tether", "Mind Spike", "Mirror Image", "Misty Step", "Negative Image", "Ray Of Enfeeblement", "Riptide", "Shadow Adaptation", "Shadow Blade", "Shdow Puppets", "Spider Climb", "Spray Of Cards", "Suggestion", "Warp Bolt", "Warp Sense")
warlock_lv3 = ()
warlock_spelllist = (warlock_lv1, warlock_lv2, warlock_lv3)

#Wizard Class
wizard_lv1 = ("Absorb Elements", "Alarm", "Black Ribbons", "Burning Hands", "Catapult", "Cause Fear", "Charm Person", "Chromatic Orb", "Cloak Of Shadow", "Color Spray", "Comprehend Languages", "Creeping Touch", "Delerium Orb", "Detect Magic", "Disguise Self", "Earth Tremor", "Elevated Sight", "Elf Shot", "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Flipperform", "Fog Cloud", "Frost Fingers", "Grease", "Ice Knife", "Identify", "Illusory Script", "Jims Magic Missile", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Pratfall", "Protection From Evil And Good", "Shadow Armour", "Shadow Hands", "Shield", "Silent Image", "Silvery Barbs", "Sleep", "Snare", "Spiny Shield", "Tashas Caustic Brew", "Tashas Hideous Laughter", "Tensers Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt")
wizard_lv2 = ("Agnazzars Scorcher", "Air Bubble", "Alter Self", "Arcane Lock", "Arcane Vigor", "Arcomagnetic Repulsion", "Augury", "Blindness/Deafness", "Blur", "Borrowed Knowledge", "Cloud Of Daggers", "Continual Flame", "Crown Of Madness", "Dark Path", "Darkbolt", "Darkness", "Darkvision", "Detect Thoughts", "Dragons Breath", "Drayfns Blunted Blade", "Dreamwalk", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/ Reduce", "Flaming Sphere", "Flock Of Familiars", "Gentle Repose", "Gift Of Gab", "Gust Of Wind", "Hold Person", "Invisibility", "Jims Glowing Coin", "Kinetic Jaunt", "Knock", "Krails Rupture", "Levitate", "Life Tether", "Locate Object", "Maddening Whispers", "Magic Mouth", "Magic Weapon", "Maximillians Earthen Grasp", "Melfs Acid Arrow", "Mind Spike", "Mirror Image", "Misty Step", "Nathairs Mischief", "Negative Image", "Nystuls Magic Aura", "Ominous Winds", "Phantasmal Force", "Protection", "Pyrotechnics", "Ray Of Enfeeblement", "Rimes Binding Ice",  "Riptide", "Rope Trick", "Scorching Ray", "See Invisibility", "Shadow Adaptation", "Shadow Blade", "Shadow Puppet", "Shatter", "Shielding Word", "Skywrite", "Slither", "Snillocs Snowball Swarm", "Spider Climb", "Spray of Cards", "Suggestion", "Tashas Mind Whip","Ugly Duckling", "Vortex Warp", "Warding Wind", "Warp Sense", "Web", "Wither And Bloom")
wizard_lv3 = ()
wizard_spelllist = (wizard_lv1, wizard_lv2, wizard_lv3)

spellbook = []

def clear_console():
    #Clears the screen. 'cls' for Windows, 'clear' for Linux/ Mac
    os.system("cls" if os.name == "nt" else "clear")

def print_spell_list(char_class):
    # Prints out a Spell List, Ordered by Level
    spelllist_name = f"{char_class}_spelllist"
    spelllist = globals().get(spelllist_name, [])
    if spelllist:
        for index, level in enumerate(spelllist,1):
            text = (f" {char_class.title()} Spells - Level {index} ").center(50,"=")
            print("\n",text)
            for spell in level:
                print(f"{spell}")
    else:
        print(f"{char_class.title()} Spell List does not Exist")

def input_spells(char_class):
    #Creates the list of known Spells. Ask user which school, and how many spells they know, and appends them to the array 'Spellbook'
    spelllist_name = f"{char_class}_spelllist"
    spelllist = globals().get(spelllist_name, [])
    if not spelllist:
        print(f"The {char_class.title()} Spell List has not yet been Implemented")
    else:
        spell_count = int(input("How many spells do you know in total?: "))
        i = 0
        while i < spell_count:
            spell_input = input("Please Enter the Spell Name: ").title()
            valid_spell = False
            if spell_input in spellbook:
                print("This Spell is already in your Spellbook")
            else:
                for spells in spelllist:
                    if spell_input in spells:
                        spellbook.append(spell_input.title())
                        valid_spell = True
                        break
                if (valid_spell == False):
                    print(f"This Spell does not appear in the {char_class.title()} Spell List")
                else:
                    print(f"{spell_input} has correctly been recorded.")
                    i += 1
        print(f"We have entered {i} Spells to your Spellbook!")

def display_spellbook():
    spellbook.sort()
    for i in spellbook:
        print(i)

def delete_spell():
    remove_spell = input("Please Enter the Name of the Spell to Remove: ").title()
    try:
        spellbook.remove(remove_spell)
        print(f"Spell {remove_spell} has been removed.")
    except ValueError:
        print(f"The Spell {remove_spell} did not exist in your Spellbook.")
    print("Your Updated Spellbook is as follows;")
    display_spellbook()

def random_spells(char_class):
    spellist_name = f"{char_class}_spelllist"
    spelllist = globals().get(spellist_name,[])
    if not spelllist:
        print(f"The {char_class.title()} Spell List has not yet been Implemented")
    else:
        level = int(input("What is the Maximum Level Spell you can Learn?: "))
        num = int(input("How Many Spells to Randomise?: "))
        sliced_spelllist = list(spelllist[:level])          #Slices the selected Spell List up to the Level Required (Remember, Spells Level 1 are at position 0, etc)
        flattened_spells = []                               #Creates an empty list which will be used to unpack the tuples
        for levelled_spells in sliced_spelllist:            #Levelled_spells will be the tuple level
            for spell in levelled_spells:                   #Looks at the individual spell per level
                if spell not in spellbook:
                    flattened_spells.append(spell)          #If this spell is NOT already in the spellbook, it is added as a possibility for random selection
        if (len(flattened_spells) < num):
            print(f"There are only {len(flattened_spells)} available! Adjusting accordingly.")
            num = len(flattened_spells)
        add_spells = random.sample(flattened_spells, num)
        add_spells.sort(reverse=True)
        conf_spells = ""
        for spell in add_spells:
            spellbook.append(spell)
            conf_spells = ", ".join(add_spells)
        print(f"The Spells that have been added are; {conf_spells}")

def random_scrolls(char_class):
    spellist_name = f"{char_class}_spelllist"
    spelllist = globals().get(spellist_name, [])
    if not spelllist:
        print(f"The {char_class.title()} Spell List has not yet been Implemented")
    else:
        level = int(input("What is the Maximum Level Spell you can Learn?: "))
        num = int(input("How Many Spells to Randomise?: "))
        sliced_spelllist = list(spelllist[:level])  # Slices the selected Spell List up to the Level Required (Remember, Spells Level 1 are at position 0, etc)
        flattened_spells = []  # Creates an empty list which will be used to unpack the tuples
        for levelled_spells in sliced_spelllist:  # Levelled_spells will be the tuple level
            for spell in levelled_spells:  # Looks at the individual spell per level
                flattened_spells.append(spell)
        add_spells = random.choices(flattened_spells, k=num)
        conf_spells = ""
        for spell in add_spells:
            spellbook.append(spell)
            conf_spells = ", ".join(add_spells)
        print(f"The Scrolls that have been found are; {conf_spells}")




choice = ""
while choice != 0:
    #Main Menu
    print("Main Menu".center(50,"-"))
    print("Option 1 - Print Entire Spell List")
    print("Option 2 - Add to Your Known Spells")
    print("Option 3 - Display Spellbook")
    print("Option 5 - Add Random Unknown Spells")
    print("Option 6 - Random Spell Scrolls")
    print("Option 9 - Remove Spells from Your Spellbook")
    print("Option 0 - Quit")

    try:
        choice = int(input("Please Make Your Choice: "))
    except:
        pass #Placeholder to be filled in

    clear_console()
    match choice:
        case 1:
            #Menu for Viewing Spell Lists
            print("Print Spell List".center(50,"-"))
            print("Option 1 - Artificer Spell List")
            print("Option 2 - Bard Spell List")
            print("Option 3 - Cleric Spell List")
            print("Option 4 - Druid Spell List")
            print("Option 5 - Paladin Spell List")
            print("Option 6 - Ranger Spell List")
            print("Option 7 - Sorcerer Spell List")
            print("Option 8 - Warlock Spell List")
            print("Option 9 - Wizard Spell List")
            print("Option 0 - Quit")

            try:
                choice = int(input("Please Make Your Choice: "))
            except:
                pass  # Placeholder to be filled in

            match choice:
                case 1:
                    print_spell_list("artificer")
                case 2:
                    print_spell_list("bard")
                case 3:
                    print_spell_list("cleric")
                case 4:
                    print_spell_list("druid")
                case 5:
                    print_spell_list("paladin")
                case 6:
                    print_spell_list("ranger")
                case 7:
                    print_spell_list("sorcerer")
                case 8:
                    print_spell_list("warlock")
                case 9:
                    print_spell_list("wizard")
                case 0:
                    choice = ""
                    clear_console()
                    pass
                case _:
                    print("Please Enter a Valid Number")
        case 2:
            #Menu for Adding Spells to your Spellbook
            print("Adding Spells to Your Spellbook".center(50,"-"))
            print("Option 1 - Artificer Spell List")
            print("Option 2 - Bard Spell List")
            print("Option 3 - Cleric Spell List")
            print("Option 4 - Druid Spell List")
            print("Option 5 - Paladin Spell List")
            print("Option 6 - Ranger Spell List")
            print("Option 7 - Sorcerer Spell List")
            print("Option 8 - Warlock Spell List")
            print("Option 9 - Wizard Spell List")
            print("Option 0 - Quit")

            try:
                choice = int(input("Please Make Your Choice: "))
            except:
                pass  # Placeholder to be filled in

            match choice:
                case 1:
                    input_spells("artificer")
                case 2:
                    input_spells("bard")
                case 3:
                    input_spells("cleric")
                case 4:
                    input_spells("druid")
                case 5:
                    input_spells("paladin")
                case 6:
                    input_spells("ranger")
                case 7:
                    input_spells("sorcerer")
                case 8:
                    input_spells("warlock")
                case 9:
                    input_spells("wizard")
                case 0:
                    choice = ""
                    clear_console()
                    pass
                case _:
                    print("Please Enter a Valid Number")
            input("Press Enter to Continue")
        case 3:
            print("Displaying your Spellbook.")
            display_spellbook()
            input("Press Enter to Continue")
        case 5:
            print("Add Random Unknown Spells".center(50, "-"))
            print("Option 1 - Artificer Spell List")
            print("Option 2 - Bard Spell List")
            print("Option 3 - Cleric Spell List")
            print("Option 4 - Druid Spell List")
            print("Option 5 - Paladin Spell List")
            print("Option 6 - Ranger Spell List")
            print("Option 7 - Sorcerer Spell List")
            print("Option 8 - Warlock Spell List")
            print("Option 9 - Wizard Spell List")
            print("Option 0 - Quit")

            try:
                choice = int(input("Please Make Your Choice: "))
            except:
                pass  # Placeholder to be filled in

            match choice:
                case 1:
                    random_spells("artificer")
                case 2:
                    random_spells("bard")
                case 3:
                    random_spells("cleric")
                case 4:
                    random_spells("druid")
                case 5:
                    random_spells("paladin")
                case 6:
                    random_spells("ranger")
                case 7:
                    random_spells("sorcerer")
                case 8:
                    random_spells("warlock")
                case 9:
                    random_spells("wizard")
                case 0:
                    choice = ""
                    clear_console()
                    pass
                case _:
                    print("Please Enter a Valid Number")
            input("Press Enter to Continue")
        case 6:
            print("Random Spell Scrolls.".center(50, "-"))
            print("Option 1 - Artificer Spell List")
            print("Option 2 - Bard Spell List")
            print("Option 3 - Cleric Spell List")
            print("Option 4 - Druid Spell List")
            print("Option 5 - Paladin Spell List")
            print("Option 6 - Ranger Spell List")
            print("Option 7 - Sorcerer Spell List")
            print("Option 8 - Warlock Spell List")
            print("Option 9 - Wizard Spell List")
            print("Option 0 - Quit")

            try:
                choice = int(input("Please Make Your Choice: "))
            except:
                pass  # Placeholder to be filled in

            match choice:
                case 1:
                    random_scrolls("artificer")
                case 2:
                    random_scrolls("bard")
                case 3:
                    random_scrolls("cleric")
                case 4:
                    random_scrolls("druid")
                case 5:
                    random_scrolls("paladin")
                case 6:
                    random_scrolls("ranger")
                case 7:
                    random_scrolls("sorcerer")
                case 8:
                    random_scrolls("warlock")
                case 9:
                    random_scrolls("wizard")
                case 0:
                    choice = ""
                    clear_console()
                    pass
                case _:
                    print("Please Enter a Valid Number")
            input("Press Enter to Continue")
        case 9:
            print("Remove Spells from Your Spellbook".center(50,"-"))
            delete_spell()
            input("Press Enter to Continue")
        case 0:
            print("Have a Good Day!")
        case _:
            print("Please Enter a Valid Number")
