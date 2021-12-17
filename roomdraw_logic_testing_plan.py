"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic Black Box Testing
=====================
The HMC Room Draw Logic tests the functionality, design specifications, and 
implementation of the HMC Room Draw Logic.
"""

from roomdraw_logic import *
import unittest

class test_compare_priority(unittest.TestCase):
    """
    Tests the compare_priority function of the DrawLogic class
    Pre-conditions for the compare priority tests are two user objects
    """
    def test_compare_priority_1(self):
        """
        test_compare_priority_1 tests the implementation 
        of the compare_priority function with 
        different graduation years and different priority numbers 
        """
        pass
    
    def test_compare_priority2(self):
        """
        test_compare_priority2 tests the implementation 
        of the compare_priority function with 
        different graduation years and same priority numbers 
        """
        pass

    def test_compare_priority3(self):
        """
        test_compare_priority3 tests the implementation 
        of the compare_priority function with 
        same graduation year and different priority number
        """
        pass

class test_is_room_gender_locked(unittest.TestCase):
    """
    Tests the is_room_gender_locked function of the DrawLogic class
    Pre-conditions for the is_room_gender_locked tests are one 
    user object and one room object
    """
    def test_is_room_gender_locked_1(self):
        """
        test_is_room_gender_locked_1 tests the implementation of the 
        is_room_gender_locked function with a room that is gender locked"""
        pass

    def test_is_room_gender_locked_2(self):
        """
        test_is_room_gender_locked2 tests the implementation of the 
        is_room_gender_locked function with a room that is not gender locked"""
        pass

class test_does_gender_of_room_match(unittest.TestCase):
    """
    Tests the does_gender_of_room_match function of the DrawLogic class
    Pre-conditions for the does_gender_of_room_match tests are up to two user 
    objects and one room object
    """
    def test_does_gender_of_room_match_1(self):
        """
        test_does_gender_of_room_match_1 tests the implementation of 
        the does_gender_of_room_match function with a room that is 
        not gender locked
        """
        pass
    
    def test_does_gender_of_room_match_2(self):
        """
        test_does_gender_of_room_match_2 tests the implementation of 
        the does_gender_of_room_match function with a room that is gender 
        locked and matches the gender of the user
        """
        pass
    
    def test_does_gender_of_room_match_3(self):
        """
        test_does_gender_of_room_match_3 tests the implementation of 
        the does_gender_of_room_match function with a room that is 
        gender locked but does not match the gender of the user 
        """
        pass

class test_is_frosh_bump_legal(unittest.TestCase):
    """
    Tests the is_frosh_bump_legal function of the DrawLogic class
    Pre-conditions for the is_frosh_bump_legal tests are two room objects
    """ 
    def test_is_frosh_bump_legal_1(self):
        """
        test_is_frosh_bump_legal_1 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is not a frosh room
        """
        pass

    def test_is_frosh_bump_legal_2(self):
        """
        test_is_frosh_bump_legal_2 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is a frosh_room and the proposed_room being a valid room in Case 
        """
        pass

    def test_is_frosh_bump_legal_3(self):
        """
        test_is_frosh_bump_legal_3 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is a frosh_room and the proposed_room in another dorm
        """
        pass
    
    def test_is_frosh_bump_legal_4(self):
        """
        test_is_frosh_bump_legal_4 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is a frosh_room and the proposed_room being reserved for frosh
        """
        pass
    
    def test_is_frosh_bump_legal_5(self):
        """
        test_is_frosh_bump_legal_5 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is a frosh_room and the proposed_room being reserved for frosh
        and in another dorm
        """
        pass

class test_can_pull_into(unittest.TestCase):
    """
    Tests the can_pulll_into function of the DrawAction class
    Pre-conditions for the can_pull_into tests are up to three user objects
    and two room objects
    """ 
    def test_can_pull_into_1(self):
        """
        test_can_pull_into_1 tests the implementation of the can_pull_into function
        as the user is attempting to pull into an empty room. can_pull_into should
        return True
        """
        pass
    
    def test_can_pull_into_2(self):
        """
        test_can_pull_into_2 tests the implementation of the can_pull_into function
        as the user is attempting to pull into an empty room that is reserved for frosh.
        The proposed_room is invalid and can_pull_into should return False 
        """
        pass

    def test_can_pull_into_3(self):
        """
        test_can_pull_into_3 tests the implementation of the can_pull_into function
        as the user is attempting to pull into an empty room that is reserved for frosh.
        The proposed_room is valid and can_pull_into should return True 
        """
        pass

    def test_can_pull_into_4(self):
        """
        test_can_pull_into_4 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a non-gender locked room that is occupied 
        and has capacity for an additional user. 
        """
        pass
    
    def test_can_pull_into_5(self):
        """
        test_can_pull_into_5 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a gender-matchinhg room that is occupied 
        and has capacity for an additional user
        """
        pass
    
    def test_can_pull_into_6(self):
        """
        test_can_pull_into_6 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a non-gender-matching room that is occupied 
        and has capacity for an additional user
        """
        pass

    def test_can_pull_into_7(self):
        """
        test_can_pull_into_7 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a room that is full (the user pulling into the room
        has higher priority than the current user)
        """
        pass
    
    def test_can_pull_into_8(self):
        """
        test_can_pull_into_8 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a room that is full (the user pulling into the room
        has lower priority than the current user)
        """
        pass

    def test_can_pull_into_9(self):
        """
        test_can_pull_into_9 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a room that is full (the user pulling into the room
        has higher priority than the current users)
        """
        pass

    def test_can_pull_into_10(self):
        """
        test_can_pull_into_10 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a room that is full (the user pulling into the room
        has lower priority than the current users)
        """
        pass

class test_can_room_be_gender_locked(unittest.TestCase):
    """
    Tests the can_room_be_gender_locked function of the DrawAction class
    Pre-conditions for the can_room_be_gender_locked tests are up to two user objects
    and one room objects
    """ 
    def test_can_room_be_gender_locked_1(self):
        """
        test_can_room_be_gender_locked_1 tests the implementation of the 
        can_room_be_gender_locked by checking if a room of one user can be gender locked
        """
        pass

    def test_can_room_be_gender_locked_2(self):
        """
        test_can_room_be_gender_locked_2 tests the implementation of the 
        can_room_be_gender_locked by checking if a room of multiple users of the
        same gender can be gender locked
        """
        pass
    
    def test_can_room_be_gender_locked_3(self):
        """
        test_can_room_be_gender_locked_3 tests the implementation of the 
        can_room_be_gender_locked by checking if a room of multiple users of
        different gender can be gender locked
        """
        pass

class test_pull_into(unittest.TestCase):
    """
    Tests the pull_into function of the DrawAction class
    Pre-conditions for the pull_into tests are up to three user objects
    and two room objects
    """ 
    def test_pull_into_1(self):
        """
        test_pull_into_1 tests the implementation of the pull_into by having a user not be
        able to pull into a room and the users in the room staying the same
        """
        pass
    
    def test_pull_into_2(self):
        """
        test_pull_into_2 tests the implementation of the pull_into by having a user pull into an empty room
        that is not frosh reserved
        """
        pass
    
    def test_pull_into_3(self):
        """
        test_pull_into_3 tests the implementation of the pull_into by having a user pull into an empty room
        that is frosh reserved with the proposed room being invalid
        """
        pass

    def test_pull_into_4(self):
        """
        test_pull_into_4 tests the implementation of the pull_into by having a user pull into an empty room
        that is frosh reserved with the proposed room being valid
        """
        pass

    def test_pull_into_5(self):
        """
        test_pull_into_5 tests the implementation of the pull_into by having a user pull into a room that is occupied
        but has capacity
        """
        pass
    
    def test_pull_into_6(self):
        """
        test_pull_into_6 tests the implementation of the pull_into by having a user pull into a non-gender-locked 
        room that is occupied and is over capacity. The user pulling into the room has higher priority. 
        """
        pass
    
    def test_pull_into_7(self):
        """
        test_pull_into_7 tests the implementation of the pull_into by having a user pull into a gender-locked 
        room that is occupied and is over capacity. The user pulling into the room has higher priority. 
        """
        pass

class test_undo_pull(unittest.TestCase):
    """
    Tests the undo_pull function of the DrawAction class
    Pre-conditions for the undo_pull tests are up to two user objects
    and two room objects
    """ 
    def test_undo_pull_1(self):
        """
        test_undo_pull_1 tests the implementation of undo_pull by having the user not
        be a current user of the room
        """
        pass
    
    def test_undo_pull_2(self):
        """
        test_undo_pull_2 tests the implementation of undo_pull by having the user not be
        the only one in the gender-locked room
        """
        pass
    
    def test_undo_pull_3(self):
        """
        test_undo_pull_3 tests the implementation of undo_pull by having the user not be    
        the only one in a non gender-locked room
        """
        pass
    
    def test_undo_pull_4(self):
        """
        test_undo_pull_4 tests the implementation of undo_pull by having the user be the only
        one in the gender-locked room
        """
        pass
    
    def test_undo_pull_5(self):
        """
        test_undo_pull_4 tests the implementation of undo_pull by having the user be the only
        one in a non gender-locked room
        """
        pass

class test_declare_gender_locking(unittest.TestCase):
    """
    Tests the declare_gender_locking function of the DrawAction class
    Pre-conditions for the declare_gender_locking tests are up to two user objects
    and one room object
    """ 
    def test_declare_gender_locking_1(self):
        """
        test_declare_gender_locking_1 tests the implementation of declare_gender_locking 
        by having the gender of the users in the room not be the same
        """
        pass

    def test_declare_gender_locking_2(self):
        """
        test_declare_gender_locking_2 tests the implementation of declare_gender_locking by having 
        the user declaring gender locking not be one of the current users of the room
        """
        pass
    
    def test_declare_gender_locking_3(self):
        """
        test_declare_gender_locking_2 tests the implementation of declare_gender_locking by having 
        the user declaring gender locking be one of the current users of the room
        """
        pass

class test_undo_gender_locking(unittest.TestCase):
    """
    Tests the undo_gender_locking function of the DrawAction class
    Pre-conditions for the undo_gender_locking tests are up to two user objects
    and one room object
    """ 
    def test_undo_gender_locking_1(self):
        """
        test_undo_gender_locking_1 tests the implementation of undo_gender_locking 
        by having the user be in the room and the room not be gender locked
        """
        pass

    def test_undo_gender_locking_2(self):
        """
        test_undo_gender_locking_2 tests the implementation of undo_gender_locking by having 
        the user not be one of the current users of the room
        """
        pass
    
    def test_undo_gender_locking_3(self):
        """
        test_undo_gender_locking_3 tests the implementation of undo_gender_locking 
        by having the user be in the room and the room be gender locked
        """
        pass

class test_bump_frosh(unittest.TestCase):
    """
    Tests the bump_frosh function of the DrawAction class
    Pre-conditions for the bump_frosh tests are two room objects
    """ 
    def test_bump_frosh_1(self):
        """
        test_bump_frosh_1 tests the implementation of bump_frosh by having 
        the desired_room not be reserved for frosh
        """
        pass
    
    def test_bump_frosh_2(self):
        """
        test_bump_frosh_2 tests the implementation of bump_frosh by having 
        the desired_room be reserved for frosh but the proposed room not
        be valid
        """
        pass

    def test_bump_frosh_3(self):
        """
        test_bump_frosh_3 tests the implementation of bump_frosh by having 
        the desired_room be reserved for frosh and the proposed room be valid
        """
        pass