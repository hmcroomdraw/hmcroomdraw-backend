"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic White Box Testing
=====================
The HMC Room Draw Logic White Box tests the implementation of the HMC Room 
Draw Logic.
"""

from roomdraw_logic import *
import unittest

# There is no special set-up required before we run the tests
class TestDrawLogic(unittest.TestCase):
    """
    Tests the Room Draw Logic of the HMC Room Draw Backend using White Box testing
    """
    def testComparePriority(self):
        """
        testComparePriority makes sure
        1) invalid student objects raise an error
        2) invalid class_year attributes raise an error
        3) invalid priority_number attributes raise an error
        """
        pass
    
    def testisRoomGenderLocked(self):
        """
        testIsRoomGenderLocked makes sure
        1) invalid room object raises an error
        2) invalid gender_locked of desired_room attributes raise an error
        """
        pass

    def testDoesRoomMatchStudentGender(self):
        """
        No white box testing necessary"""
        pass

    def testIsFroshBumpLegal(self):
        """
        testIsFroshBumpLegal makes sure
        1) Invalid desired_room and proposed_room raises an error
        2) Each room in the 9 dorms follow the right "path" when checking the 
        proposed room
        """
        pass
    
class TestDrawAction(unittest.TestCase):
    """Tests the potential actions a user can utilize when using the Room Draw App"""
    def testCanPullInto(self):
        """
        testCanPullInto makes sure
        1) desired_room and student object is valid (right errors are raised if not valid)
        2) priority numbers and year attributes are valid (right errors are raised if not valid)
        3) the front-end API endpoint for the proposed room is only called 
           when applicable
        4) isFroshBumpLegal() is called when applicable
        5) doesRoomMatchStudentGender() is called when applicable
        """
        pass

    def testPullInto(self):
        """
        testPullInto makes sure
        1) canPullInto() is called
        2) A transaction is created
        3) Any previous students are set to no room
        4) The current pullee has his/her room attribute set to the desired room
        5) We exit the transaction 
        """
        pass

    
    def testUndoPull(self):
        """"
        testUndoPull makes sure
        1) A transaction is created
        2) The student undoing the pull is currently in the room
        3) Set the student undoing the pull to no room
        4) All the necessary functions are called
        5) All necessary data and objects are valid
        """
        pass
    
    def testCanRoomsBeGenderLocked(self):
        """"
        testCanRoomsBeGenderLocked makes sure
        1) All the necessary functions are called
        2) All necessary data and objects are valid
        """
        pass

    def testDeclareRoomGenderLocked(self):
        """
        testDeclareRoomGenderLocked makes sure
        1) All the necessary functions are called
        2) All necessary data and objects are valid
        3) A transaction is created
        4) The room has its gender_locked status set to the gender of the user
        """
        pass
    
    def testUndoRoomGenderLocked(self):
        """
        testUndoRoomGenderLocked makes sure
        1) All the necessary functions are called
        2) All necessary data and objects are valid
        3) A transaction is created
        4) The room has its gender_locked status set to None
        """
        pass

    def testBumpFrosh(self):
        """
        testBumpFrosh makes sure
        1) All the necessary functions are called
        2) All necessary data and objects are valid
        3) frosh_room attribute of desired_room is set to False
        4) frosh_room attribute of proposed_room is set to True
        """
        pass 


    





