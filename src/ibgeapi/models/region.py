from dataclasses import dataclass
from ibgeapi.models.location import Location

@dataclass(frozen=True)
class Region(Location):
    acronym: str
