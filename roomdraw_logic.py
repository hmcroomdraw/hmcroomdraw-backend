"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic and Action
=====================
The HMC Room Draw Logic and Action processes digital draw rules, 
users, permissions, and pulls
"""
from models import *
from dataclasses import dataclass
from typing import Optional

class DrawLogic:
    """
    performs the logic functions of HMC Room Draw
    """
    @staticmethod
    def compare_priority(user1:User, user2:User) -> User:
        """
        compares class year and priority numbers of user1 and user2.
        returns the user that has higher priority
        """
        # compares the class_year attribute of user1 and user2 
        if user1.class_year < user2.class_year:
            return user1
        elif user1.class_year > user2.class_year:
            return user2
        else:
            # compares the priority_number attribute of user1 and user2
            if user1.priority_number > user2.priority_number:
                return user2
            else:
                return user1
    
    @staticmethod
    def is_room_gender_locked(desired_room: Room) -> bool:
        """
        determines if a room is gender locked
        """
        return desired_room.gender != None
        
    @staticmethod
    def does_gender_of_room_match(desired_room: Room, user: User) -> bool:
        """
        determines if user's gender matches the gender of a desired_room
        """
        # determine if the desired_room is gender locked
        if DrawLogic.is_room_gender_locked(desired_room):
                # determine if the desired_room matches the gender of the user
                return user.gender == desired_room.gender
        return True

    @staticmethod
    def is_frosh_bump_legal(desired_room: Room, proposed_room: Room) -> bool:
        """
        determines if a frosh bump is legal by ensuring that the proposed_room follows
        the simplified Room Draw rules: 1) proposed_room is in the same residence hall 
        as the desired_room 2) the proposed_room is not reserved for frosh
        """
        # checks if the proposed_room is in the same residence hall as the desired_room
        # and the proposed_room is not reserved for frosh
        if desired_room.residence_hall_name != proposed_room.residence_hall_name or proposed_room.frosh_room:
            return False
        else:
            return True

class DrawAction:
    """
    actions a user can perform in HMC Room Draw
    """
    @staticmethod
    def can_pull_into(desired_room: Room, proposed_room: Room, user: User) -> bool:
        """
        can_pull_into takes in a desired_room, proposed_room, user and returns 
        whether or not the user can pull into the room
        """
        # desired_room is currently empty 
        if not desired_room.users:
            # Determine if the desired_room is reserved for frosh 
            if desired_room.frosh_room:
                # Determine if the proposed_room is valid by calling isFroshBumpLegal()
                return DrawLogic.is_frosh_bump_legal(desired_room,proposed_room)
            return True
        # desired_room can fit an additional user
        elif desired_room.capacity >= len(desired_room.users)+1:
            # check if the gender of the student matches the gender of the room
            return DrawLogic.does_gender_of_room_match(desired_room,user)
        # desired_room is over capacity (check if bumping is necessary)
        else:
            for user_in_room in desired_room.users:
                if DrawLogic.compare_priority(user,user_in_room) != user:
                    return False
            return True
    
    @staticmethod
    def can_room_be_gender_locked(desired_room: Room) -> bool:
        """
        determine if a room can be gender locked: all the genders of the 
        current users in the desired_room have to be the same for gender 
        locking to occur
        """
        # list of genders of current users
        genders = []
        for user in desired_room.users:
            genders.append(user.gender)
        # determines if all the genders are the same
        return len(set(genders)) == 1

    @staticmethod
    def pull_into(desired_room: Room, proposed_room: Room, user: User):
        """
        pull_into takes in a desired_room, proposed_room and user and 
        pulls the user into a room.
        """
        # checks if the desired_room is allowed to be pulled by the user
        if DrawAction.can_pull_into(desired_room,proposed_room,user):
            # checks if desired_room is currently empty
            if not desired_room.users:
                # checks if desired room is reserved for frosh
                if desired_room.frosh_room:
                    DrawAction.bump_frosh(desired_room,proposed_room)
                desired_room.users = [user]
            # desired_room is occupied but is not at capacity
            elif desired_room.capacity >= len(desired_room.users)+1:
                desired_room.users.append(user)
            # desired_room is over capacity
            else:
                # Update the users in the room to the user
                desired_room.users = [user]
                # Undo gender locking
                DrawAction.undo_gender_locking(user,desired_room)
    
    @staticmethod
    def undo_pull(user: User, room: Room):
        """
        undo_pull takes in a user and undos their pull if they are 
        a current user in the room.
        """
        # checks the validity of the room and its users
        if room != None and room.users != None:
            # checks if the user is a current user of the room
            if user in room.users:
                # removes user from the users attribute of room
                room.users.remove(user)
                # undoes gender locking if no one is in the room
                if room.users == []:
                    room.gender = None
    
    @staticmethod
    def declare_gender_locking(user: User, desired_room: Room):
        """
        declare_gender_locking declares a room to be gender locked if the
        user is one of the current users in the desired_room
        """
        # determine if room can be gender locked and if the user is a current user 
        if DrawAction.can_room_be_gender_locked(desired_room) and user in desired_room.users:
            # set room of gender to user gender
            desired_room.gender = user.gender
    
    @staticmethod
    def undo_gender_locking(user: User, desired_room: Room):
        """
        undo_gender_locking undos the gender locking of a room
        if the user is a current user in the desired_room
        """
        # checks if the user is a current user of the desired_room
        if user in desired_room.users:
            # sets the gender of the desired_room to None
            desired_room.gender = None
            
    @staticmethod
    def bump_frosh(desired_room: Room, proposed_room: Room):
        """
        bump_frosh bumps a frosh out of the desired_room to a proposed_room
        if the process is legal
        """
        # checks if the desired_room is reserved for frosh
        if desired_room.frosh_room:
            # checks if the proposed_room is valid
            if DrawLogic.is_frosh_bump_legal(desired_room,proposed_room):
                # Set the desired_room frosh_room status to False
                desired_room.frosh_room = False
                # Set the desired_room frosh_room status to True
                proposed_room.frosh_room = True
