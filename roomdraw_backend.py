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
    """
    A single room in a residential building.
    """
    id: RoomId
    residence_hall_name: str
    floor_number: int
    suite: str
    number: str

@dataclass
class Floor:
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
    floors: list[Floor]

@dataclass 
class User:
    """
    Contains information about users.
    """
    id: UserId
    first_name: str
    last_name: str
    email: str
    class_year: str
    priority_number: int

class DrawLogic:
    """
    Performs the logic functions of the HMC Room Draw Backend. 
    Satisifies requirement 3 in the Digital Draw Application Requirements.
    """
    def __init__(self):
        None 
    
    def comparePriority(self, student1:UserId, student2:UserId) -> User:
        """Compares class year and priority numbers of student1 and student2.
           Returns the student that has higher priority
        """
        # Retrieves the student1 and student2 object from the database
        # Compares the class_year attribute of student 1 and student 2 
        # (Error-checking for valid class year)
        # Compares the priority_number attribute of student 1 and student 2
        # (Error-checking for valid priority numbers)
        # Returns the student that has higher priority
        return False
    
    def comparePriority(self, student1:User, student2:User) -> User:
        """Compares class year and priority numbers of student1 and student2.
           Returns the student that has higher priority
        """
        # Compares the class_year attribute of student 1 and student 2
        # (Error-checking for valid class year)
        # Compares the priority_number attribute of student 1 and student 2
        # (Error-checking for valid priority numbers)
        # Returns the student that has higher priority
        return None

class DrawState:
    """Returns the total state of what goes on in the digital draw.
    Helps satisfiy requirement 7 in Digital Draw Application Requirements
    """
    def __init__(self):
        None
    
    def getUserIn(self, room: RoomId) -> Optional[User]:
        """getUserIn takes in a RoomId and finds the user at that specific room. 
        Returns the student or None if there is no student.
        """
        # Retrieves the room object from the database by calling getRoom (room:RoomId) 
        # (Error-checking for making sure the room object is valid) 
        # Retrieves the user object from the database by calling getUserIn (room:Room) 
        # (Error-checking for making sure the user object is valid) 
        return None
    
    def getRoomOf(self, user: UserId) -> Optional[Room]:
        """getRoomOf takes in a UserId and finds the room the user is currently living in. 
        Returns the student or None if there is no student. 
        """
        # Retrieves the user object from the database by calling getUser (id:UserId) 
        # (Error-checking for making sure the user object is valid)
        # Retrieves the room object from the database by calling getRoomOf (user:User)
        # # (Error-checking for making sure the room object is valid) 
        return None

class DrawAction:
    """
    Potential actions a user can perform (frequently interacts with DrawState)
    """
    def __init__(self):
        None

    def canPullInto(self, student: UserId, desired_room: RoomId) -> bool:
        """
        canPullInto takes in a student and a desiredRoom and returns 
        whether or not the student can pull into the room
        """
        # Check if the desired_room is pullable from the DrawLogic class
        # 1) Retrieve the student object (given the UserId argument) from the database 
        # (Error-checking for making sure the user object is valid)
        # 2) Determine the user that is present in the desired_room by calling 
        #    getUserIn(desired_room: RoomId)
        # (Error-checking for making sure the user object is valid)
        # 3) If there is a user in the room, then we compare priority numbers 
        #    of the two students and return the student with the highest priority 
        # (Error-checking for making sure the priority numbers are valid)
        return False
    
    def pullInto(self, student: UserId, desired_room: RoomId):
        """
        pullInto takes in a student and a desiredRoom and pulls the student into a room. 
        Returns None if the action is completed and an Exception if the action fails.
        """
        # 1) Checks if the desired_room is allowed to be pulled by the student
        # 2) Call getUserIn (room: RoomId) to retrieve the previous user
        # 3) If the desired_room is allowed to be pulled by the student and there 
        # was a previous student, then we set the previous user to no Room
        # and the Room to no user. 
        # 4) Set the student to the desired_room and set the desired_room to the student
        return None
    
    def undoPull(self, student: UserId):
        """
        undoPull takes in a student and undos their pull. 
        Returns None if the action is completed and an Exception if the action fails
        """
        # 1) Set the student to no room by
        #    1. Calling getRoomOf(user:UserId)
        #    2. Calling getUser(id:UserId) 
        #    3. Calling setUserToRoom(user: User, room: Room)
        # 2) Set the room to no user by
        #    1. Calling setRoomToNoUser(room: Room)
        # Error-checking for making sure there actually is a user in the room 
        pass