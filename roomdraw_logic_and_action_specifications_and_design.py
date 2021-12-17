"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic and Action Specifications and Design
=====================
The HMC Room Draw Logic and Action processes digital draw rules, 
users, permissions, and pulls
"""
# models provides useful objects for HMC Room Draw Logic and Action
from models import *
from dataclasses import dataclass
from typing import Optional

class DrawLogic:
    """
    performs the logic functions of HMC Room Draw
    satisifies requirment 3 as the application
    understands and implements pull action logic
    with automatic validation
    """
    @staticmethod
    def compare_priority(user1:User, user2:User) -> User:
        """
        compares class year and priority numbers of user1 and user2.
        returns the user that has higher priority
        """
        # compares the class_year attribute of user1 and user2 
        # compares the priority_number attribute of user1 and user2 (if neccesary)
        pass
    
    @staticmethod
    def is_room_gender_locked(desired_room: Room) -> bool:
        """
        determines if a room is gender locked
        """
        # checks if desired_room is null
        pass 
        
    @staticmethod
    def does_gender_of_room_match(desired_room: Room, user: User) -> bool:
        """
        determines if user's gender matches the gender of a desired_room
        """
        # determine if the desired_room is gender locked
        # determine if the desired_room matches the gender of the user (if necessary)
        pass

    @staticmethod
    def is_frosh_bump_legal(desired_room: Room, proposed_room: Room) -> bool:
        """
        determines if a frosh bump is legal by ensuring that the proposed_room 
        follows the simplified Room Draw rules: 1) proposed_room is in the same 
        residence hall as the desired_room 2) the proposed_room is not reserved 
        for frosh
        """
        # checks if the proposed_room is in the same residence hall as the 
        # desired_room and the proposed_room is not reserved for frosh
        pass

class DrawAction:
    """
    actions a user can perform in HMC Room Draw
    satsifies requirement 2 as this application supports pulling and having
    many users in a room
    """
    @staticmethod
    def can_pull_into(desired_room: Room, proposed_room: Room, user: User) -> bool:
        """
        can_pull_into returns whether or not the user can pull into the room
        """
        # dcheck if esired_room is currently empty
            # determine if the desired_room is reserved for frosh (if necessary) 
                # Determine if the proposed_room is valid by calling isFroshBumpLegal() (if neccesary)
        # check if desired_room can fit an additional user
            # check if the gender of the student matches the gender of the room (if necessary)
        # check if desired_room is over capacity
            # check if bumping is necessary by comparing priority 
        pass
    
    @staticmethod
    def can_room_be_gender_locked(desired_room: Room) -> bool:
        """
        determine if a room can be gender locked: all the genders of the 
        current users in the desired_room have to be the same for gender 
        locking to occur
        """
        # define list of genders of current users
        # determines if all the genders are the same by converting
        # list of genders to a set
        pass

    @staticmethod
    def pull_into(desired_room: Room, proposed_room: Room, user: User):
        """
        pull_into pulls a user into the desired_room if the move is valid
        """
        # checks if the desired_room is allowed to be pulled by the user
        # checks if desired_room is currently empty (if necessary)
            # checks if desired room is reserved for frosh (if necessary)
        # desired_room is occupied but is not at capacity
        # desired_room is over capacity
            # Update the users in the room to the user
            # Undo gender locking
        pass
    
    @staticmethod
    def undo_pull(user: User, room: Room):
        """
        undo_pull takes in a user and undos their pull if they are 
        a current user in the room.
        """
        # checks the validity of the room and its users
            # checks if the user is a current user of the room
                # removes user from the users attribute of room
                # undoes gender locking if no one is in the room
        pass
    
    @staticmethod
    def declare_gender_locking(user: User, desired_room: Room):
        """
        declare_gender_locking declares a room to be gender locked if the
        user is one of the current users in the desired_room
        """
        # determine if room can be gender locked and if the user is a current user 
            # set room of gender to user gender
        pass
    
    @staticmethod
    def undo_gender_locking(user: User, desired_room: Room):
        """
        undo_gender_locking undos the gender locking of a room
        if the user is a current user in the desired_room
        """
        # checks if the user is a current user of the desired_room
            # sets the gender of the desired_room to None
        pass
            
    @staticmethod
    def bump_frosh(desired_room: Room, proposed_room: Room):
        """
        bump_frosh bumps a frosh out of the desired_room to a proposed_room
        """
        # checks if the desired_room is reserved for frosh
            # checks if the proposed_room is valid
                # set the desired_room frosh_room status to False
                # set the desired_room frosh_room status to True
        pass
