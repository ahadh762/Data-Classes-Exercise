import csv
from dataclasses import dataclass, field

class Age(object):
    def __init__(self,amount,unit):
        self.amount = amount
        self.unit = unit
    def __repr__(self):
        return 'Age(%s,%s)' % (self.amount, self.unit)
    def __gt__(self,other):
        print('__gt__ called - self: %s, other: %s' % (self,other))
        if self.unit == other.unit:
            return self.amount > other.amount
        else:
            return False
    def __eq__(self,other):
        print('__eq__ called')
        return self.amount == other.amount if self.unit == other.unit else False

centennial = Age(100,"years")
sesquicentennial = Age(150,"years")
century = Age(100,"years")

print(centennial == century)

# As a dataclass


@dataclass
class Age:
    amount: int
    unit: str
    def __gt__(self,other):
        if self.unit == other.unit:
            return self.amount > other.amount
        return False

centennial = Age(100,"years")
sesquicentennial = Age(150,"years")
century = Age(100,"years")

print(centennial == century)
print(sesquicentennial < century)


@dataclass
class MeteoriteFinding:
    name: str
    id: int
    nametype: str
    meteoriteclass: str
    mass: float = field(metadata={"units":"grams"})
    fall: str
    year: str
    latitude: float = field(metadata={"units":"decimal degrees"})
    longitude: float = field(metadata={"units":"decimal degrees"})



# import from the CSV into a list of meteorite findings
findings = list()
with open("Meteorite_Landings.csv","r",newline='',encoding="utf-8-sig") as csvfile:
    meteorite_reader = csv.DictReader(csvfile)
    for row in meteorite_reader:
        finding = MeteoriteFinding(row['name'],row['id'],row['nametype'],row['recclass'],row['mass (g)'],row['fall'],row['year'],row['reclat'],row['reclong'])
        findings.append(finding)