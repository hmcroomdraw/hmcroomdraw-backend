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
class User:
    id: UserId
    first_name: str
    last_name: str
    email: str
    class_year: int
    priority_number: int
    gender: str
    #RoomId: RoomId

@dataclass
class Room:
    """
    A single room in a residential building.
    """
    id: RoomId
    residence_hall_name: str
    floor_number: int
    suite: str
    number: int
    #gender: str
    #frosh_room: bool

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