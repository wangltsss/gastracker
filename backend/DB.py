from DataTypes import Fuel, Date
from log_config import get_logger

logger = get_logger(__name__)

class Query:
    def __init__(self, price: float, fuel: Fuel, station: str, address: str, area: str, date: Date):
        self._price = price
        self._fuel = fuel
        self._station = station
        self._address = address
        self._area = area
        self._date = date
        logger.debug(f"Query object created: {self.pretty_print()}")
        
    def pretty_print(self):
        return f"Price: {self.price}, Fuel: {self.fuel}, Station: {self.station}, Address: {self.address}, Area: {self.area}, Date: {self.date}"
        
    def __eq__(self, other: "Query") -> bool:
        return self.price == other.price
        
    def __ne__(self, other: "Query") -> bool:
        return not self.__eq__(other)
    
    def __lt__(self, other: "Query") -> bool:
        return self.price < other.price
    
    def __gt__(self, other: "Query") -> bool:
        return self.price > other.price
    
    def __str__(self) -> str:
        return self.pretty_print()
        
    @property    
    def price(self) -> float:
        return self._price
    
    @property
    def fuel(self) -> Fuel:
        return self._fuel
    
    @property
    def station(self) -> str:
        return self._station
    
    @property
    def address(self) -> str:
        return self._address
    
    @property
    def area(self) -> str:
        return self._area
    
    @property
    def date(self) -> Date:
        return self._date
    
    
# a = Query(1.0, Fuel.Diesel, "station", "address", "area", Date(2021, 1, 1))
# b = Query(2.0, Fuel.Diesel, "station", "address", "area", Date(2021, 1, 1))
# c = Query(1.0, Fuel.Diesel, "station", "address", "area", Date(2021, 1, 1))

# print(a == b)
# print(a == c)
# print(a < b)
# print(a > b)
    