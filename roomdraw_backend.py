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

Pixel = int

@dataclass
class Image:
    url: str
    width: Pixel
    height: Pixel

@dataclass
class Room:
    """A single room in a residential building."""
    residence_hall_name: str
    floor_number: int
    suite: str
    number: str

@dataclass
class Floor:
    """
    Contains the display information of a floor in a residential building.
    """
    residence_hall_name: str
    floor_number: int
    rooms: list[Room]
    image: Image

@dataclass
class ResidenceHall:
    name: str
    floors: list[Floor]

class DrawState:
    def __init__(self):
        pass

class APIServices:
    def __init__(
        self,
        # authenticator: GoogleAuthenticator,
        # draw_engine: DigitalDrawEngine,
        # residence_halls_service: ResidenceHallsService,
        # users_service: UsersService,
        ):
        pass

    def residence_halls(self) -> list[ResidenceHall]:
        """
        
        """
        pass
