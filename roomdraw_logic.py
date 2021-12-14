"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic and Action
=====================
The HMC Room Draw Logic and Action processes digital draw rules, 
users, permissions, and pulls
"""
from roomdraw_repository import *
from dataclasses import dataclass
from typing import Optional

class DrawLogic:
    """
    Performs the logic functions of the HMC Room Draw Backend.
    """
    @staticmethod
    def compare_priority(self, user1: User, user2: User) -> User:
        """
        Compares class year and priority numbers of user1 and user2.
        Returns the user that has higher priority
        """
        # Compares the class_year attribute of user1 and user2 
        if user1.class_year < user2.class_year:
            return user1
        elif user1.class_year > user2.class_year:
            return user2
        else:
            # Compares the priority_number attribute of user1 and user2
            if user1.priority_number > user2.priority_number:
                return user2
            else:
                return user1
    
class DrawAction:
    """
    Actions a user can perform
    """
    def __init__(self,roomdraw_repository: Repository):
        self.roomdraw_repository = roomdraw_repository

    def can_pull_into(self, desired_room: Room, user: User) -> bool:
        """
        can_pull_into takes in a user and a desiredRoom and returns 
        whether or not the user can pull into the room
        """
        # desired_room is currently empty
        if self.roomdraw_repository.get_users_in(desired_room.id) == None:
            return True
        
        # desired_room is currently occupied
        else:
            user_in_room = self.roomdraw_repository.get_users_in(desired_room.id)
            if DrawLogic.compare_priority(user,user_in_room) != user:
                return False
            return True
    
    def pull_into(self, desired_room_id: RoomId, user_id: UserId):
        """
        pull_into takes in a user_id and a desired_room_id and pulls the user 
        into a room.
        """
        # Open transaction
        with self.roomdraw_repository.create_transaction() as transaction:
            desired_room = transaction.get_room(desired_room_id)
            user = transaction.get_user(user_id)

            # Checks if the desired_room is allowed to be pulled by the user
            if DrawAction.can_pull_into(desired_room,user):

                # desired_room is currently empty
                if transaction.get_users_in(desired_room.id) == None:
                    transaction.set_user_to_room(user_id,desired_room_id)

                # desired_room is currently occupied           
                else:
                    # Retrieve the previous user
                    previous_user_id = transaction.get_user_in(desired_room_id)
                    # Set the previous user to no room
                    transaction.set_user_to_no_room(previous_user_id)
                    # Set the user to the desired_room
                    transaction.set_user_to_room(user_id,desired_room_id)
    
    def undo_pull(self, user_id: UserId):
        """
        undo_pull takes in a user and undos their pull.
        """
        # Open transaction 
        with self.roomdraw_repository.create_transaction() as transaction:
            # Retreives the user from the database
            user = transaction.get_user(user_id)
            # Set the user to no room
            transaction.set_user_to_no_room(user_id)

    def get_all_possible_rooms(self, user_id: UserId):
        """
        get_all_possible_rooms takes in a user and returns a list of rooms the
        user can pull into 
        """
        # Open transaction
        with self.roomdraw_repository.create_transaction() as transaction:
            # Retrieve the user and list of rooms from the database 
            user = transaction.get_user(user_id)
            listOfRooms = self.roomdraw_repository.get_all_rooms()

            acceptableRooms = []
            for room in listOfRooms:
                if self.can_pull_into(room,user):
                    acceptableRooms.append(room)
            return acceptableRooms


