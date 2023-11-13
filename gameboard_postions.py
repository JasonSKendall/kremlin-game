#!python


class locationOnGameboard():
    def __init__(self, boardLocation=None,
                 politburoLevel=None,
                 kgbPurgePhaseOrder=None,
                 spyInvestigationPhaseOrder=None,
                 funeralCommissionPhaseOrder=None) -> None:
        self._boardLocation = boardLocation
        self.politburoLevel = politburoLevel 
        self.kgbPurgePhaseOrder = kgbPurgePhaseOrder
        self.spyInvestigationPhaseOrder = spyInvestigationPhaseOrder
        self.funeralCommissionPhaseOrder = funeralCommissionPhaseOrder

    @property
    def boardLocation(self):
        return self._boardLocation

    @boardLocation.setter
    def boardLocation(self, value):
        dictBoardLocationNames = {
            1: "Party Chief",
            2: "KGB Head",
            3: "Foreign Minister",
            4: "Defense Minister",
            5: "Ideology Chief",
            6: "Industry Minister",
            7: "Economy Minister",
            8: "Sport Minister",
            9: "Candidates",
            10: "People",
            11: "Siberia",
            12: "Kremlin Wall",
        }
        if value in dictBoardLocationNames.keys():
            self._boardLocation = value
            return(dictBoardLocationNames[self._boardLocation])
        else:
            print("Invalid board location")
            return(None)


    def politburoLevelName(self):
        dictPolitburoLevelNames = {
            1: "Party Chief",
            2: "First Level",
            3: "Second Level",
            4: "Candidates",
            5: "Poeple"
        }
        if self.politburoLevel in dictPolitburoLevelNames.keys():
            return(dictPolitburoLevelNames[self.politburoLevel])
        else:
            return(None)

    def purgeRollBaseNumber(self):
        dictPurgeRollBases = {
        1: 18,
        2: 14,
        3: 10,
        4: 6
        }
        if self.politburoLevel in dictPurgeRollBases.keys():
            return(dictPurgeRollBases[self.politburoLevel])
        else:
            return(None)

    def votingOrder(self):
        if self.boardLocation < 9:
            return(self.boardLocation)
        else:
            return(None)

    def printTitle(self):
        print("Name of Board Location: ", self.boardLocation)

    def printPolitburoLevelName(self):
        print("Politburo Level Name: ", self.politburoLevelName())

    def printPurgeRollBaseNumber(self):
        print("Purge Roll Base Number: ", self.purgeRollBaseNumber())

    def printVotingOrder(self):
        print("Voting Order Number: ", self.votingOrder())

    def printKGBPurgePhaseOrder(self):
        print("KGB Purge Phase Order Number: ", self.kgbPurgePhaseOrder)

    def printSpyInvestigationPhaseOrder(self):
        print("Spy Investigation Phase Order Number: ", self.spyInvestigationPhaseOrder)

    def printFuneralCommissionPhaseOrder(self):
        print("Funeral Commission Phase Order Number: ", self.funeralCommissionPhaseOrder)

    def printAttributes(self):
        print()
        self.printTitle()
        self.printPolitburoLevelName()
        self.printPurgeRollBaseNumber()
        self.printVotingOrder()
        self.printKGBPurgePhaseOrder()
        self.printSpyInvestigationPhaseOrder()
        self.printFuneralCommissionPhaseOrder()








class slotPartyChief(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__ (
            boardLocation = 1 ,
            politburoLevel = 1 ,
            kgbPurgePhaseOrder = 3 ,
            spyInvestigationPhaseOrder = 4 ,
            funeralCommissionPhaseOrder = None)
        self.availableSlots = 1
    
    def phase1AddOneSP(self):
        pass

    def phase6ChangeWithinLevel(self):
        pass

    def phase6PromoteAndDemote(self):
        pass

    def phase8Parade(self):
        pass

class slotKgbHead(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__ (
            boardLocation = 2 ,
            politburoLevel = 2 ,
            kgbPurgePhaseOrder = 1 ,
            spyInvestigationPhaseOrder = 3 ,
            funeralCommissionPhaseOrder = 3)
        self.availableSlots = 1

    def phase2Purge(self):
        pass

    def phase6Promote(self):
        pass

class slotForeignMinister(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__ (
            boardLocation = 3,
            politburoLevel = 2,
            kgbPurgePhaseOrder = None,
            spyInvestigationPhaseOrder = 2,
            funeralCommissionPhaseOrder = 1)
        self.availableSlots = 1

    def phase5Action(self):
        pass

    def phase6Promote(self):
        pass

class slotDefenseMinister(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__ (
            boardLocation = 4,
            politburoLevel = 2,
            kgbPurgePhaseOrder = None,
            spyInvestigationPhaseOrder = 1,
            funeralCommissionPhaseOrder = 7)
        self.availableSlots = 1


    def phase3Action(self):
        pass

    def phase6Promote(self):
        pass

class slotIdeologyChief(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__ (
            boardLocation = 5 ,
            politburoLevel = 3 ,
            kgbPurgePhaseOrder = 2 ,
            spyInvestigationPhaseOrder = None ,
            funeralCommissionPhaseOrder = 2)
        self.availableSlots = 1

    def phase6Promote(self):
        pass

class slotIndustryMinister(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__ (
            boardLocation = 6 ,
            politburoLevel = 3 ,
            kgbPurgePhaseOrder = 5 ,
            spyInvestigationPhaseOrder = 4 ,
            funeralCommissionPhaseOrder = 4 )
        self.availableSlots = 1

    def phase6Promote(self):
        pass

class slotEconomyMinister(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__(
            boardLocation = 7 ,
            politburoLevel = 3 ,
            kgbPurgePhaseOrder = None ,
            spyInvestigationPhaseOrder = None ,
            funeralCommissionPhaseOrder = 5 )
        self.availableSlots = 1

    def phase6Promote(self):
        pass

class slotSportMinister(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__(
            boardLocation = 8,
            politburoLevel = 3 ,
            kgbPurgePhaseOrder = None ,
            spyInvestigationPhaseOrder = None ,
            funeralCommissionPhaseOrder = 6)
        self.availableSlots = 1

    def phase6Promote(self):
        pass

class slotCandidate(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__(
            boardLocation = 9 ,
            politburoLevel = 4 ,
            kgbPurgePhaseOrder = None ,
            spyInvestigationPhaseOrder = None ,
            funeralCommissionPhaseOrder = None )
        self.availableSlots = 5

class slotPeople(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__(
            boardLocation = 10 ,
            politburoLevel = None ,
            kgbPurgePhaseOrder = None ,
            spyInvestigationPhaseOrder = None ,
            funeralCommissionPhaseOrder = None)
        self.availableSlots = 25

class slotSibera(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__(
            boardLocation = 11 ,
            politburoLevel = None ,
            kgbPurgePhaseOrder = None ,
            spyInvestigationPhaseOrder = None ,
            funeralCommissionPhaseOrder = None)
        self.availableSlots = 25

class slotKremlinWall(locationOnGameboard):
    def __init__(self) -> None:
        super().__init__(
            boardLocation = 12 ,
            politburoLevel = None ,
            kgbPurgePhaseOrder = None ,
            spyInvestigationPhaseOrder = None ,
            funeralCommissionPhaseOrder = None)
        self.availableSlots = 26


obj1 = slotPartyChief()
# obj1.printAttributes()

obj2 = slotKgbHead()
# obj2.printAttributes()

obj3 = slotForeignMinister()
# obj3.printAttributes()

obj4 = slotDefenseMinister()
# obj4.printAttributes()

obj5 = slotIdeologyChief()
# obj5.printAttributes()

obj6 = slotIndustryMinister()
# obj6.printAttributes()

obj7 = slotEconomyMinister()
# obj7.printAttributes()

obj8 = slotSportMinister()
# obj8.printAttributes()

obj9 = slotCandidate()
# obj9.printAttributes()

obj10 = slotSibera()
# obj10.printAttributes()

obj11 = slotKremlinWall()
# obj11.printAttributes()



def factionNames(faction):
    dictOfFactions = {
        1 : "Hardline Stalinists",
        2 : "Red Army Militarists",
        3 : "Lysenko Evolutionists",
        4 : "Reform Expansionists",
        5 : "Trotskyite Internationalists",
        6 : "Old-line Marxists"
        }
    if faction in dictOfFactions.keys():
        return(dictOfFactions[faction])
    else:
        return(None)
    
# print( factionNames(4) )


class politicianSetup():
    def __init__(self,
                 code=None,
                 politician=None,
                 age=None,
                 strong=None,
                 weak=None) -> None:
        self.code = code
        self.politician = politician
        self.age = age
        self.strong = strong
        self.weak = weak
    



class politicianState(politicianSetup):
    def __init__(self, code, politician, age, strong, weak,
                 stressPoints=0,
                 health=0,
                 suspicion=0,
                 takingCure=False,
                 isDead=False,
                 isInactive=False) -> None:
        super().__init__(code,politician,age,strong,weak)           
        self.stressPoints = stressPoints
        self.health = health
        self.suspicion = suspicion
        self.takingCure = takingCure
        self.isDead = isDead
        self.isInactive = isInactive
    

slotNames = {
    1: "Party Chief",
    2: "KGB Head",
    3: "Foreign Minister",
    4: "Defense Minister",
    5: "Ideology Chief",
    6: "Industry Minister",
    7: "Economy Minister",
    8: "Sport Minister",
    9: "Candidates",
    10: "People",
    11: "Siberia",
    12: "Kremlin Wall"
}


dictPoliticians = {
    'A' : ( "Nestor Aparatschitk", 80, 2, 8),
    'B' : ( "Lech Schukrutoff",    75, 7, 4),
    'C' : ( "Alexej Goferbrok",    74, 4, 2),
    'D' : ( "Petr Niewitko",       73, 6, 3),
    'E' : ( "Karel Krakemheds",    72, 6, 3),
    'F' : ( "Andrej Purgemoff",    71, 4, 7),
    'G' : ( "Diwan Palavrian",     69, 8, 5),
    'H' : ( "Nikolai Shootemdedsky",     68, 6, 4),
    'I' : ( "Anatol Mischif",      67, 2, 4),
    'J' : ( "Antonj Talksalott",     66, 5, 7),
    'K' : ( "Eduard Boremtodev",     65, 3, 8),
    'L' : ( "Igor Doberman",     64, 8, 3),
    'M' : ( "Sergei Eatstumuch",     63, 4, 8),
    'N' : ( "Boris Karrienko",     62, 3, 5),
    'O' : ( "Oleg Satin",     61, 5, 2),
    'P' : ( "Iwan Manjak",     60, 7, 6),
    'Q' : ( "Tigran Zenjarplan",     59, 3, 2),
    'R' : ( "Turi Nikotin",     58, 6, 8),
    'S' : ( "Ludmilla Patina",     57, 3, 4),
    'T' : ( "Mikail Strychnin",     56, 5, 6),
    'U' : ( "Wassily Protzky",     55, 4, 5),
    'V' : ( "Natasha Nogoodnik",     54, 7, 2),
    'W' : ( "Leonid Bungaloff",     53, 8, 6),
    'X' : ( "Boris Badenuff",     52, 8, 7),
    'Y' : ( "Ulan Putschnik",     51, 2, 3),
    'Z' : ( "Viktor Wasolin",     50, 2, 7)
}


# dude01 = politicianDefinitions('A')
# print(dude01)

##########



# Create a set of unique numbers from 1 to 10
available_numbers = set(range(1, 11))
used_numbers = set()

# Create a dictionary to store the politician-number pairs
entry_sheet = {code: (name, None) for code, (name, age, _, _) in dictPoliticians.items()}

# Function to display the entry sheet
def display_entry_sheet():
    entry_format = "{:<4} {:<25} {:<4} {:<12} {:<12} {:<6}"
    print(entry_format.format("Code", "Name", "Age", "Strength", "Weakness", "IP"))
    print("-" * 90)

    print("Entry Sheet:")
    for code, (name, number) in entry_sheet.items():
        age = dictPoliticians[code][1]
        strong = slotNames[ dictPoliticians[code][2] ].split()[0]
        weak = slotNames[ dictPoliticians[code][3] ].split()[0]
        formatted_number = str(number) if number is not None else ''  # Format number as a string if it's not None
        print(entry_format.format( code, name, age, strong, weak, formatted_number))
    print(available_numbers)

# Function to clear the number for a politician and add it back to available numbers
def clear_number(code):
    if code in entry_sheet and entry_sheet[code][1] is not None:
        number = entry_sheet[code][1]
        entry_sheet[code] = (entry_sheet[code][0], None)
        available_numbers.add(number)
        print(f"Number for {code} cleared. {number} added back to available numbers.")


# Function to clear the number for a politician and add it back to available numbers
def swap_numbers(code, new_number):
    if code in entry_sheet and entry_sheet[code][1] is not None:
        entry_sheet[code] = (entry_sheet[code][0], int(number))
        available_numbers.add(old_number)
        print(f"Number for {code} swapped. {number} added back to available numbers.")


# Ask the user for both the politician and the number
while True:
    display_entry_sheet()
    print("Enter the politician's code and number (e.g., 'K 5'), or ('K c') to clear K's IP, or 'quit' to quit:")
    user_input = input().strip()
    if user_input == 'quit' or user_input == 'q':
        break
    elif user_input.startswith('clear '):
        clear_code = user_input.split()[1]
        clear_number(clear_code)
    else:
        try:
            code, number = user_input.split()
            if code in entry_sheet:
                if int(number) in available_numbers:
                    put_it_back = int(number)
                    if entry_sheet[code][1] is not None:
                        put_it_back = entry_sheet[code][1]
                    entry_sheet[code] = (entry_sheet[code][0], int(number))
                    available_numbers.add(int(put_it_back))
                    available_numbers.remove(int(number))
            else:
                print("Invalid politician code or number. Please enter valid values.")
        except ValueError:
            print("Invalid input format. Please enter the politician's code and number separated by a space.")




# Display the updated entry sheet
display_entry_sheet()