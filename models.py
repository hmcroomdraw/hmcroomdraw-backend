from dataclasses import dataclass

Pixel = int

UserId = str
RoomId = str
FloorPlanId = str
ResidenceHallId = str

@dataclass
class Image:
    url: str
    width: Pixel
    height: Pixel

@dataclass
class Coordinate:
    x: int
    y: int

@dataclass
class Room:
    """A single room in a residential building."""
    id: RoomId
    residence_hall_name: str
    floor_number: int
    suite: str
    number: str

@dataclass
class FrontendRoom:
    """A single room in a residential building."""
    id: RoomId
    residence_hall_name: str
    floor_number: int
    suite: str
    number: str
    current_occupant_name: str
    # gender: str
    # frosh_room: bool

@dataclass
class FloorPlan:
    """
    Contains the display information of a floor in a residential building.
    """
    id: FloorPlanId
    residence_hall_name: str
    floor_number: int
    rooms: list[Room]
    image: Image
    room_coordinates: dict[RoomId, Coordinate]

@dataclass
class ResidenceHall:
    id: ResidenceHallId
    name: str
    floors: list[FloorPlan]

@dataclass
class User:
    id: UserId
    first_name: str
    last_name: str
    email: str
    class_year: str
    priority_number: int
    gender: str
