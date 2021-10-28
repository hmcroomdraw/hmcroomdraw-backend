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
    """
    A single room in a residential building.
    """
    residence_hall_name: str
    gender_locked: str
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

@dataclass 
class User:
    """
    Contains information about users.
    """
    name: str
    email: str
    phone_number: str
    draw_priority_number: int

class DrawLogic:
    """
    Performs the logic functions of the HMC Room Draw Backend. 
    Satisifies requirement 3 in the Digital Draw Application Requirements.
    """
    def __init__(self):
        None 
    

    def comparePriorityNumbers(self, student1:User, student2:User) -> bool:
        """Compares priority numbers of student1 and student2.
            Returns True if student 1 has higher priority 
            (greater seniority or lower Room Draw number) than student2
        """
        return False


    def isGenderLocked(self, desiredRoom: Room, student: User) -> bool:
        """
        Determines if a room is gender locked and if the student's gender
        agrees with the gender lock
        """
        return False
    

    def isFroshRoom(self, desiredRoom: Room) -> bool:
        """
        Determines if a desired room is reserved for freshman. 
        If so the student must complete, a frosh bump and choose a 
        valid room for the frosh to live in
        """ 
        return False
    

    def isFroshBumpLegal(self, bumpedRoom: Room) -> bool:
        """  
        Based on the rules of frosh bumping in the Room Draw Regulations
        we can determine if a frosh bump is legal
        """ 
        return False


class DrawState:
    """Stores the total state of what goes on in the digital draw"""
    def __init__(self):
        # rooms is a dictionary with keys representing rooms and values 
        # representing the current user 
        self.map = {}
    

    def userAtRoom(self, room: Room) -> User:
        """ userAtRoom takes in a room and finds the user at that specific room. 
        Returns the student or None if there is no student. 
        Helps satisfiy requirement 7 in Digital Draw Application Requirements
        """
        return None

    
    def allRooms(self) -> list [Room]:
        """
        allRooms returns all the rooms the student can pull into
        """
        return []
    
    
    def allRoomsPossible(self, student: User) -> list [Room]:
        """
        allRooms returns all the possible rooms the student can pull into based
        on the DrawLogic
        """
        return []
    
    
    def allResidenceHalls(self) -> list [ResidenceHall]:
        """
        allResidenceHalls returns all the residence halls the student can pull into
        """
        return []
    
    
    def allResidenceHallsPossible(self, student: User) -> list [ResidenceHall]:
        """
        allRooms returns all the possible residence halls the student can pull 
        into based on the DrawLogic
        """ 
        return []
    

class DrawAction:
    """
    Potential actions a user can perform (frequently interacts with DrawState)
    """
    def __init__(self):
        None
    def canPullInto(self, student: User, desiredRoom: Room) -> bool:
        """
        canPullInto takes in a student and a desiredRoom and returns 
        whether or not the student can pull into the room
        """
        return False
    

    def pullInto(self, student: User, desiredRoom: Room) -> None:
        """
        pullInto takes in a student and a desiredRoom and pulls the student into a room. 
        Returns None if the action is completed and an Exception if the action fails.
        """
        pass
    

    def undoPullForStudent(self, student: User) -> None:
        """
        undoPullForStudent takes in a student and undos their pull. 
        Returns None if the action is completed and an Exception if the action fails
        """
        pass

class DrawNotifier:
    """Notifies a student that they have been bumped through email (using gmail API)"""
    def __init__(self):
        None

    def sendEmail(self, student: User) -> None:
        """Sends an email to a student if they have been bumped by a student with a better priority number.
           Returns None if the email is sent and an Exception if the action fails
        """
        return None