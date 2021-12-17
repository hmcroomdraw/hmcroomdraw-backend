"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic And Action Testing
=====================
The HMC Room Draw Logic And Action tests the 
functionality, implementation, anddesign specifications of the 
HMC Room Draw Logic and Action.
"""

from roomdraw_logic_and_action import *
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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE")
        # User2 is returned because he graduates earlier
        self.assertEqual(DrawLogic.compare_priority(User1,User2),User2)
    
    def test_compare_priority_2(self):
        """
        test_compare_priority_2 tests the implementation 
        of the compare_priority function with 
        different graduation years and same priority numbers 
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User3 = User("3", "Eli", "Pregerson", "pregersone@g.hmc.edu", 2024, 42, "MALE")
        # User1 is returned because he graduates earlier
        self.assertEqual(DrawLogic.compare_priority(User1,User3),User1)

    def test_compare_priority_3(self):
        """
        test_compare_priority_3 tests the implementation 
        of the compare_priority function with 
        same graduation year and different priority number
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42,"MALE")
        User4 = User("4", "Sid", "Rastogi", "srastogi@g.hmc.edu", 2023, 22, "MALE")
        # User4 is returned because he has a lower priority number
        self.assertEqual(DrawLogic.compare_priority(User1,User4),User4)

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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        Room1 = Room("2", "Case", 2, None, 202, True, [User1],2,"MALE")
        self.assertEqual(DrawLogic.is_room_gender_locked(Room1),True)

    def test_is_room_gender_locked_2(self):
        """
        test_is_room_gender_locked2 tests the implementation of the 
        is_room_gender_locked function with a room that is not gender locked"""
        User2 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        Room2 = Room("2", "Case", 2, None, 202, True, [User2],2,None) 
        self.assertEqual(DrawLogic.is_room_gender_locked(Room2),False)

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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        Room1 = Room("2", "Case", 2, None, 202, True,None,2,None) 
        self.assertEqual(DrawLogic.does_gender_of_room_match(Room1,User1), True)
    
    def test_does_gender_of_room_match_2(self):
        """
        test_does_gender_of_room_match_2 tests the implementation of 
        the does_gender_of_room_match function with a room that is gender 
        locked and matches the gender of the user
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        Room1 = Room("2", "Case", 2, None, 202, True,[User1],2,"MALE") 
        self.assertEqual(DrawLogic.does_gender_of_room_match(Room1,User2), True)
    
    def test_does_gender_of_room_match_3(self):
        """
        test_does_gender_of_room_match_3 tests the implementation of 
        the does_gender_of_room_match function with a room that is 
        gender locked but does not match the gender of the user 
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User3 = User("1", "Anya", "Bhargava", "abhargava@g.hmc.edu", 2026, 42, "FEMALE")
        Room1 = Room("2", "Case", 2, None, 202, True,[User1],2,"MALE") 
        self.assertEqual(DrawLogic.does_gender_of_room_match(Room1,User3), False)

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
        desired_room_1 = Room("2", "Case", 2, None, 202, False, None, 2, None) 
        proposed_room_1 = Room("3", "Case", 2, None, 203, False, None, 2, None) 
        self.assertEqual(DrawLogic.is_frosh_bump_legal(desired_room_1,proposed_room_1),True)

    def test_is_frosh_bump_legal_2(self):
        """
        test_is_frosh_bump_legal_2 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is a frosh_room and the proposed_room being a valid room in Case 
        """
        desired_room_2 = Room("2", "Case", 2, None, 202, True, None, 2, None) 
        proposed_room_2 = Room("3", "Case", 2, None, 203, False, None, 2, None) 
        self.assertEqual(DrawLogic.is_frosh_bump_legal(desired_room_2,proposed_room_2),True)

    def test_is_frosh_bump_legal_3(self):
        """
        test_is_frosh_bump_legal_3 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is a frosh_room and the proposed_room in another dorm
        """
        desired_room_3 = Room("2", "Case", 2, None, 202, True, None, 2, None) 
        proposed_room_3 = Room("3", "Atwood", 2, None, 203, False, None, 2, None) 
        self.assertEqual(DrawLogic.is_frosh_bump_legal(desired_room_3,proposed_room_3),False)
    
    def test_is_frosh_bump_legal_4(self):
        """
        test_is_frosh_bump_legal_4 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is a frosh_room and the proposed_room being reserved for frosh
        """
        desired_room_4 = Room("2", "Case", 2, None, 202, True, None, 2, None) 
        proposed_room_4 = Room("3", "Case", 2, None, 203, True, None, 2, None) 
        self.assertEqual(DrawLogic.is_frosh_bump_legal(desired_room_4,proposed_room_4),False)
    
    def test_is_frosh_bump_legal_5(self):
        """
        test_is_frosh_bump_legal_5 tests the implementation of the is_frosh_bump_legal function
        with a desired_room that is a frosh_room and the proposed_room being reserved for frosh
        and in another dorm
        """
        desired_room_5 = Room("2", "Case", 2, None, 202, True, None, 2, None) 
        proposed_room_5= Room("3", "West", 2, None, 203, True, None, 2, None) 
        self.assertEqual(DrawLogic.is_frosh_bump_legal(desired_room_5,proposed_room_5),False)

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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42,"MALE")
        desired_room_1 = Room("2", "Case", 2, None, 202, False, None, 2, None) 
        self.assertEqual(DrawAction.can_pull_into(desired_room_1,None,User1),True)
    
    def test_can_pull_into_2(self):
        """
        test_can_pull_into_2 tests the implementation of the can_pull_into function
        as the user is attempting to pull into an empty room that is reserved for frosh.
        The proposed_room is invalid and can_pull_into should return False 
        """
        User2 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu",2023,42,"MALE")
        desired_room_2 = Room("2", "Case", 2, None, 202,True,None,2,None)
        proposed_room_2 = Room("2", "Atwood", 2, None, 202,False,None,2,None) 
        self.assertEqual(DrawAction.can_pull_into(desired_room_2,proposed_room_2,User2),False)

    def test_can_pull_into_3(self):
        """
        test_can_pull_into_3 tests the implementation of the can_pull_into function
        as the user is attempting to pull into an empty room that is reserved for frosh.
        The proposed_room is valid and can_pull_into should return True 
        """
        User3 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu",2023,42,"MALE")
        desired_room_3 = Room("2", "Case", 2, None, 202,True,None,2,None)
        proposed_room_3 = Room("3", "Case", 2, None, 203,False,None,2,None) 
        self.assertEqual(DrawAction.can_pull_into(desired_room_3,proposed_room_3,User3),True)

    def test_can_pull_into_4(self):
        """
        test_can_pull_into_4 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a non-gender locked room that is occupied 
        and has capacity for an additional user. 
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42,"MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_4 = Room("2", "Case", 2, None, 202,True,[User1],2,None)
        self.assertEqual(DrawAction.can_pull_into(desired_room_4,None,User2),True)
    
    def test_can_pull_into_5(self):
        """
        test_can_pull_into_5 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a gender-matchinhg room that is occupied 
        and has capacity for an additional user
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu",2023,42,"MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_5 = Room("2", "Case", 2, None, 202,True,[User1],2,"MALE")
        self.assertEqual(DrawAction.can_pull_into(desired_room_5,None,User2),True)
    
    def test_can_pull_into_6(self):
        """
        test_can_pull_into_6 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a non-gender-matching room that is occupied 
        and has capacity for an additional user
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu",2023,42,"MALE")
        User2 = User("2", "Anya", "Bhargava", "abhargava@g.hmc.edu", 2026, 42, "FEMALE") 
        desired_room_6 = Room("2", "Case", 2, None, 202,True,[User1],2,"MALE")
        self.assertEqual(DrawAction.can_pull_into(desired_room_6,None,User2),False)
    
    def test_can_pull_into_7(self):
        """
        test_can_pull_into_7 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a room that is full (the user pulling into the room
        has higher priority than the current user)
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023,42,"MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE")
        desired_room_7 = Room("2", "Case", 2, None, 202,True,[User1],1,"MALE")
        self.assertEqual(DrawAction.can_pull_into(desired_room_7,None,User2),True)
    
    def test_can_pull_into_8(self):
        """
        test_can_pull_into_8 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a room that is full (the user pulling into the room
        has lower priority than the current user)
        """
        User1 = User("1", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE")
        User2 = User("2", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023,42,"MALE")
        desired_room_8 = Room("2", "Case", 2, None, 202,True,[User1],1,"MALE")
        self.assertEqual(DrawAction.can_pull_into(desired_room_8,None,User2),False)

    def test_can_pull_into_9(self):
        """
        test_can_pull_into_9 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a room that is full (the user pulling into the room
        has higher priority than the current users)
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023,42,"MALE")
        User2 = User("2", "Anya", "Bhargava", "abhargava@g.hmc.edu", 2026, 42, "FEMALE") 
        User3 = User("3", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE")
        desired_room_9 = Room("2", "Case", 2, None, 202,True,[User1,User2],2,"MALE")
        self.assertEqual(DrawAction.can_pull_into(desired_room_9,None,User3),True)

    def test_can_pull_into_10(self):
        """
        test_can_pull_into_10 tests the implementation of the can_pull_into function
        as the user is attempting to pull into a room that is full (the user pulling into the room
        has lower priority than the current users)
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023,42,"MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE")
        User3 = User("3", "Sid", "Rastogi", "srastogi@g.hmc.edu", 2023,22, "MALE")
        desired_room_10 = Room("2", "Case", 2, None, 202,True,[User1,User2],2,"MALE")
        self.assertEqual(DrawAction.can_pull_into(desired_room_10,None,User3),False)

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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        desired_room_1 = Room("2", "Case", 2, None, 202, True, [User1], 2, None)
        self.assertEqual(DrawAction.can_room_be_gender_locked(desired_room_1),True)

    def test_can_room_be_gender_locked_2(self):
        """
        test_can_room_be_gender_locked_2 tests the implementation of the 
        can_room_be_gender_locked by checking if a room of multiple users of the
        same gender can be gender locked
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_2 = Room("2", "Case", 2, None, 202, True, [User1,User2], 2, None)
        self.assertEqual(DrawAction.can_room_be_gender_locked(desired_room_2),True)
    
    def test_can_room_be_gender_locked_3(self):
        """
        test_can_room_be_gender_locked_3 tests the implementation of the 
        can_room_be_gender_locked by checking if a room of multiple users of
        different gender can be gender locked
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Anya", "Bhargava", "abhargava@g.hmc.edu", 2026, 42, "FEMALE") 
        desired_room_3 = Room("2", "Case", 2, None, 202, True, [User1,User2], 2, None)
        self.assertEqual(DrawAction.can_room_be_gender_locked(desired_room_3),False)

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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_1 = Room("2", "Case", 2, None, 202,False,[User2], 1, None)
        DrawAction.pull_into(desired_room_1,None,User1)
        self.assertEqual(desired_room_1.users,[User2])
    
    def test_pull_into_2(self):
        """
        test_pull_into_2 tests the implementation of the pull_into by having a user pull into an empty room
        that is not frosh reserved
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        desired_room_2 = Room("2", "Case", 2, None, 202,False,None, 1, None)
        DrawAction.pull_into(desired_room_2,None,User1)
        self.assertEqual(desired_room_2.users,[User1])
    
    def test_pull_into_3(self):
        """
        test_pull_into_3 tests the implementation of the pull_into by having a user pull into an empty room
        that is frosh reserved with the proposed room being invalid
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        desired_room_3 = Room("2", "Case", 2, None, 202,True,None, 1, None)
        proposed_room_3 = Room("2", "Atwood", 2, None, 202,False,None, 1, None)
        DrawAction.pull_into(desired_room_3,proposed_room_3,User1)
        self.assertEqual(desired_room_3.users,None)

    def test_pull_into_4(self):
        """
        test_pull_into_4 tests the implementation of the pull_into by having a user pull into an empty room
        that is frosh reserved with the proposed room being valid
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        desired_room_4 = Room("2", "Case", 2, None, 202,True,None, 1, None)
        proposed_room_4 = Room("3", "Case", 2, None, 203,False,None, 1, None)
        DrawAction.pull_into(desired_room_4,proposed_room_4,User1)
        self.assertEqual(desired_room_4.users,[User1])
        self.assertEqual(desired_room_4.frosh_room,False)
        self.assertEqual(proposed_room_4.frosh_room,True)

    def test_pull_into_5(self):
        """
        test_pull_into_5 tests the implementation of the pull_into by having a user pull into a room that is occupied
        but has capacity
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_5 = Room("2", "Case", 2, None, 202,False,[User2],2, None)
        DrawAction.pull_into(desired_room_5,None,User1)
        self.assertEqual(desired_room_5.users,[User2,User1])
    
    def test_pull_into_6(self):
        """
        test_pull_into_6 tests the implementation of the pull_into by having a user pull into a non-gender-locked 
        room that is occupied and is over capacity. The user pulling into the room has higher priority. 
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_6 = Room("2", "Case", 2, None, 202,False,[User1],1, None)
        DrawAction.pull_into(desired_room_6,None,User2)
        self.assertEqual(desired_room_6.users,[User2])
    
    def test_pull_into_7(self):
        """
        test_pull_into_7 tests the implementation of the pull_into by having a user pull into a gender-locked 
        room that is occupied and is over capacity. The user pulling into the room has higher priority. 
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_7 = Room("2", "Case", 2, None, 202,False,[User1],1, "MALE")
        DrawAction.pull_into(desired_room_7,None,User2)
        self.assertEqual(desired_room_7.users,[User2])
        self.assertEqual(desired_room_7.gender,None)

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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_1 = Room("2", "Case", 2, None, 202,False,[User2], 1, None)
        DrawAction.undo_pull(User1,desired_room_1)
        self.assertEqual(desired_room_1.users,[User2])
    
    def test_undo_pull_2(self):
        """
        test_undo_pull_2 tests the implementation of undo_pull by having the user not be
        the only one in the gender-locked room
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_2 = Room("2", "Case", 2, None, 202,False,[User2,User1], 2, "MALE")
        DrawAction.undo_pull(User1,desired_room_2)
        self.assertEqual(desired_room_2.users,[User2])
        self.assertEqual(desired_room_2.gender,"MALE")
    
    def test_undo_pull_3(self):
        """
        test_undo_pull_3 tests the implementation of undo_pull by having the user not be    
        the only one in a non gender-locked room
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_3 = Room("2", "Case", 2, None, 202,False,[User1,User2], 1, None)
        DrawAction.undo_pull(User1,desired_room_3)
        self.assertEqual(desired_room_3.users,[User2])
        self.assertEqual(desired_room_3.gender,None)
    
    def test_undo_pull_4(self):
        """
        test_undo_pull_4 tests the implementation of undo_pull by having the user be the only
        one in the gender-locked room
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        desired_room_4= Room("2", "Case", 2, None, 202,False,[User1], 1, "MALE")
        DrawAction.undo_pull(User1,desired_room_4)
        self.assertEqual(desired_room_4.users,[])
        self.assertEqual(desired_room_4.gender,None)
    
    def test_undo_pull_5(self):
        """
        test_undo_pull_4 tests the implementation of undo_pull by having the user be the only
        one in a non gender-locked room
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        desired_room_5 = Room("2", "Case", 2, None, 202,False,[User1], 1, None)
        DrawAction.undo_pull(User1,desired_room_5)
        self.assertEqual(desired_room_5.users,[])
        self.assertEqual(desired_room_5.gender,None)

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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Anya", "Bhargava", "abhargava@g.hmc.edu", 2026, 42, "FEMALE") 
        desired_room_1 = Room("2", "Case", 2, None, 202,False,[User1,User2], 1, None)
        DrawAction.declare_gender_locking(User1,desired_room_1)
        self.assertEqual(desired_room_1.gender,None)

    def test_declare_gender_locking_2(self):
        """
        test_declare_gender_locking_2 tests the implementation of declare_gender_locking by having 
        the user declaring gender locking not be one of the current users of the room
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_2 = Room("2", "Case", 2, None, 202,False,[User1], 1,None)
        DrawAction.declare_gender_locking(User2,desired_room_2)
        self.assertEqual(desired_room_2.gender,None)
    
    def test_declare_gender_locking_3(self):
        """
        test_declare_gender_locking_2 tests the implementation of declare_gender_locking by having 
        the user declaring gender locking be one of the current users of the room
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_3 = Room("2", "Case", 2, None, 202,False,[User1,User2], 1,None)
        DrawAction.declare_gender_locking(User1,desired_room_3)
        self.assertEqual(desired_room_3.gender,"MALE")

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
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        desired_room_1 = Room("2", "Case", 2, None, 202,False,[User1], 1, None)
        DrawAction.undo_gender_locking(User1,desired_room_1)
        self.assertEqual(desired_room_1.gender,None)

    def test_undo_gender_locking_2(self):
        """
        test_undo_gender_locking_2 tests the implementation of undo_gender_locking by having 
        the user not be one of the current users of the room
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        User2 = User("2", "Kripesh", "Ranabhat", "kranabhat@g.hmc.edu", 2022, 52, "MALE") 
        desired_room_2 = Room("2", "Case", 2, None, 202,False,[User1], 1,"MALE")
        DrawAction.undo_gender_locking(User2,desired_room_2)
        self.assertEqual(desired_room_2.gender,"MALE")
    
    def test_undo_gender_locking_3(self):
        """
        test_undo_gender_locking_3 tests the implementation of undo_gender_locking 
        by having the user be in the room and the room be gender locked
        """
        User1 = User("1", "Adi", "Bhargava", "abhargava@g.hmc.edu", 2023, 42, "MALE")
        desired_room_3 = Room("2", "Case", 2, None, 202,False,[User1], 1, "MALE")
        DrawAction.undo_gender_locking(User1,desired_room_3)
        self.assertEqual(desired_room_3.gender,None)

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
        desired_room_1 = Room("2", "Case", 2, None, 202,False,None,2,None) 
        proposed_room_1 = Room("3", "Case", 2, None, 203,False,None,2,None) 
        DrawAction.bump_frosh(desired_room_1,proposed_room_1)
        self.assertEqual(desired_room_1.frosh_room,False)
    
    def test_bump_frosh_2(self):
        """
        test_bump_frosh_2 tests the implementation of bump_frosh by having 
        the desired_room be reserved for frosh but the proposed room not
        be valid
        """
        desired_room_2 = Room("2", "Case", 2, None, 202,True,None,2,None) 
        proposed_room_2 = Room("3", "Case", 2, None, 203,True,None,2,None) 
        DrawAction.bump_frosh(desired_room_2,proposed_room_2)
        self.assertEqual(desired_room_2.frosh_room,True)
        self.assertEqual(proposed_room_2.frosh_room,True)

    def test_bump_frosh_3(self):
        """
        test_bump_frosh_3 tests the implementation of bump_frosh by having 
        the desired_room be reserved for frosh and the proposed room be valid
        """
        desired_room_3 = Room("2", "Case", 2, None, 202,True,None,2,None) 
        proposed_room_3 = Room("3", "Case", 2, None, 203,False,None,2,None) 
        DrawAction.bump_frosh(desired_room_3,proposed_room_3)
        self.assertEqual(desired_room_3.frosh_room,False)
        self.assertEqual(proposed_room_3.frosh_room,True)
        
    
if __name__ == '__main__':
    unittest.main()




