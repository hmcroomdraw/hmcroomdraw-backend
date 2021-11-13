"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic
=====================
The HMC Room Draw Logic processes digital draw rules, users, permissions, and 
pulls.

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

    @staticmethod
    def comparePriority(self, student1:User, student1ID: UserId, student2:User, 
        student2ID: UserId) -> User:
        """Compares class year and priority numbers of student1 and student2.
           Returns the student that has higher priority
        """
        # Retrieves the student1 and student2 object from the database
        # Compares the class_year attribute of student 1 and student 2 
        # (Error-checking for valid class year)
        # Compares the priority_number attribute of student 1 and student 2
        # (Error-checking for valid priority numbers)
        # Returns the student that has higher priority
        return None

class DrawAction:
    """
    Potential actions a user can perform (frequently interacts with DrawState)
    """
    def __init__(self,repository):
        self.repository = repository

    def canPullInto(self, student: UserId, desired_room: RoomId) -> bool:
        """
        canPullInto takes in a student and a desiredRoom and returns 
        whether or not the student can pull into the room
        """
        # Check if the desired_room is pullable from the DrawLogic class
        # 1) Retrieve the student object (given the UserId argument) from the 
        # database 
        # (Error-checking for making sure the user object is valid)
        # 2) Determine the user that is present in the desired_room by calling 
        #    getUserIn(desired_room: RoomId)
        # (Error-checking for making sure the user object is valid)
        # 3) If there is a user in the room, then we compare priority numbers 
        #    of the two students and return True if the student that wants to
        #    pull into the room has higher priority 
        # (Error-checking for making sure the priority numbers are valid)
        return False
    
    def pullInto(self, student: UserId, desired_room: RoomId):
        """
        pullInto takes in a student and a desiredRoom and pulls the student into a room. 
        Returns None if the action is completed and an Exception if the action fails.
        """
        # 1) Checks if the desired_room is allowed to be pulled by the student
        # 2) Creates a transaction by calling self.repository.create_transaction()
        # 3) Call transaction.getUserIn (room: RoomId) to retrieve the previous user
        # 3) If the desired_room is allowed to be pulled by the student and there 
        # was a previous student, then we set the previous user to no Room by
        # calling transaction.set_user_to_room(user,None)
        # 4) Set the student to the desired_room by calling 
        # transaction.set_user_to_room(user,desired_room)
        return None
    
    def undoPull(self, student: UserId):
        """
        undoPull takes in a student and undos their pull. 
        Returns None if the action is completed and an Exception if the action fails
        """
        # Create a transaction by calling self.repository.create_transaction()
        # Set the student to no room by
        #    1. Calling getRoomOf(user:UserId)
        #    2. Calling getUser(id:UserId) 
        #    3. Calling setUserToRoom(user: User, room: Room)
        # Error-checking for making sure there actually is a user in the room 
        pass