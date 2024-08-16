from dataclasses import dataclass
from ibgeapi.models.location import Location

@dataclass(frozen=True)
class Country(Location):
    iso_alpha2: str
    iso_alpha3: str
