"""
HMC Room Draw Backend
=====================
CS181AA Software Engineering Class Project
------------------------------------------

The HMC Room Draw Backend Server provides a JSON API for a client to participate
in the HMC Digital Draw process. It stores and processes authentication logic, 
digital draw rules, users, permissions, and pulls. It also notifies a person via
email when they get bumped from their room.
"""

from dataclasses import dataclass
from typing import Optional

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
class Room:
    """A single room in a residential building."""
    id: RoomId
    residence_hall_name: str
    floor_number: int
    suite: str
    number: str

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

class Repository:
    def __init__(self):
        """
        Initialize the repository from database.
        """
        pass

    def getUser(self, id: UserId) -> User:
        """
        Get a copy of User from UserId
        Raises KeyError if id does not exist.
        """
        pass

    def getRoom(self, id: RoomId) -> Room:
        """Get a copy of Room from RoomId"""
        pass

    def getAllRoomIds(self) -> list[RoomId]:
        pass

    def getAllRooms(self) -> list[Room]:
        pass

    def getFloorPlan(self, id: FloorPlanId) -> FloorPlan:
        pass

    def getResidenceHall(self, id: ResidenceHallId) -> ResidenceHall:
        pass

    def getAllResidenceHalls(self) -> list[ResidenceHall]:
        pass

    def getAllResidenceHallIds(self) -> list[ResidenceHallId]:
        pass

    def getUserIn(self, room: Room) -> Optional[User]:
        pass

    def getRoomOf(self, user: User) -> Optional[Room]:
        pass

    def getUserIdToRoomIdDict(self) -> dict[UserId, RoomId]:
        pass

    def create_transaction(self) -> 'Repository.Transaction':
        return
    
    class Transaction:
        def __init__(self):
            """
            Create a transaction. This locks the resources in the repository.
            """
            pass

        def __enter__(self):
            """
            Starts the transaction. Automatically gets called when object goes
            into `with` scope.
            """
            pass

        def __exit__(self):
            """
            Ends the transaction. Autometically gets called when object goes
            out of `with` scope.
            """
            pass

        def getUser(self, id: UserId) -> User:
            """Get a copy of User from UserId"""
            pass

        def createUser(self, user: User) -> User:
            """
            Create a user from information in the user object.
            Raises Exception if user.id is not None.
            Raises Exception if user already exists.
            Assigns new a id to user object.
            Returns the modified user object.
            """
            pass
            
        def updateUser(self, user: User):
            """
            Update the user associated with user.id to have the
            new information.
            """

        def getRoom(self, id: RoomId) -> Room:
            """Get a copy of Room from RoomId"""
            pass

        def createRoom(self, room: Room) -> Room:
            pass

        def updateRoom(self, room: Room):
            pass

        def getAllRoomIds(self) -> list[RoomId]:
            pass

        def getAllRooms(self) -> list[Room]:
            pass

        def getFloorPlan(self, id: FloorPlanId) -> FloorPlan:
            pass
        
        def createFloorPlan(self, floor_plan: FloorPlan) -> FloorPlan:
            pass

        def updateFloorPlan(self, floor_plan: FloorPlan):
            pass

        def getResidenceHall(self, id: ResidenceHallId) -> ResidenceHall:
            pass

        def createResidenceHall(self, residence_hall: ResidenceHall
        ) -> ResidenceHall:
            pass

        def updateResidenceHall(self, residence_hall: ResidenceHall
        ) -> ResidenceHall:
            pass

        def getAllResidenceHalls(self) -> list[ResidenceHall]:
            pass

        def getAllResidenceHallIds(self) -> list[ResidenceHallId]:
            pass

        def getUserIn(self, room: Room) -> Optional[User]:
            pass

        def setUserToRoom(self, user: User, room: Room):
            pass

        def setUserToNoRoom(self, user: User):
            pass

        def getRoomOf(self, user_id: UserId) -> Optional[Room]:
            pass

        def setRoomToUser(self, room: Room, user: Optional[User]):
            pass

        def setRoomToNoUser(self, room: Room):
            pass

        def getUserToRoomDict(self) -> dict[UserId, RoomId]:
            pass