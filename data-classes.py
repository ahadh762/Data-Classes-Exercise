# import csv
from dataclasses import dataclass, field
import datetime
from xxlimited import foo

# @dataclass
# class Age:
#     amount: int
#     unit: str
#     def __gt__(self,other):
#         if self.unit == other.unit:
#             return self.amount > other.amount
#         return False

# centennial = Age(100,"years")
# sesquicentennial = Age(150,"years")
# century = Age(100,"years")

# print(centennial == century)
# print(sesquicentennial < century)


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


@dataclass
class Orders:
    OrderID: int
    CustomerID: int
    OrderDate: datetime.datetime()
    
    def __gt__(self,other):
        return self.OrderDate > other.OrderDate

    def __ge__(self,other):
        return self.OrderDate >= other.OrderDate        


@dataclass
class Invoices:
    InvoiceID: int
    OrderID: int
    CustomerID: int
    InvoiceDate: datetime.datetime(foo,foo,foo,foo)

    def __gt__(self,other):
        return self.InvoiceDate > other.InvoiceDate

    def __ge__(self,other):
        return self.InvoiceDate >= other.InvoiceDate     


@dataclass
class Customers:
    orderID: int
    CustomerID: int
