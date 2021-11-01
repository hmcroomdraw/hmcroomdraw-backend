"""
HMC Room Draw Backend White Box Testing
=====================
CS181AA Software Engineering Class Project
------------------------------------------
"""

from roomdraw_backend import *
import unittest

# There is no special set-up required before we run the tests
class TestDrawLogic(unittest.TestCase):
    """
    Tests the Room Draw Logic of the HMC Room Draw Backend
    """
    def testComparePriority1(self):
        """
        testComparePriority tests the design of the 1st comparePriority function
        """
        # Pre-conditions are two student objects
        # Santi and I will create a mock database that has the user and room objects
        # Test the retrieval of student1 and student2 from the database 
        # TypeError if student1 and student2 are null or not the right class 
        # More test cases would include making sure the attributes of 
        # class_year and priority_number are valid before comparing
        # ValueError if class_year and priority_number are not the right values
        pass

    def testComparePriority2(self):
        """
        testComparePriority tests the design of the 2nd comparePriority function
        """
        # Same testing plan as above minus the need for checking the retrieval

class TestDrawState(unittest.TestCase):
    "Tests the DrawState class and the state of the digital draw"
    def testGetUserIn(self):
        """
        testGetUserIn tests the design of the getUserIn function
        """
        # Pre-condition is one Room object and one User object
        # Test the retrieval of student and class objects from the database 
        # TypeError if the objects are null or not the right class
    
    def testGetRoomOf(self):
        """
        testGetRoomOf tests the design of the getRoomOf function
        """
        # Pre-condition is one Room object and one User object
        # Test the retrieval of student and class objects from the database 
        # TypeError if the objects are null or not the right class
    
class TestDrawAction(unittest.TestCase):
    """Tests the potential actions a user can utilize when using the Room Draw App"""
    def testCanPullInto(self):
        """
        testCanPullInto tests the design of the canPullInto function
        """
        # Pre-conditions are one User object, one Room object, and  
        # getUserIn is complete
        # Test the retrieval of student objects from the database 
        # TypeError if the objects are null or not the right class
        # More test cases would include making sure the attributes of 
        # class_year and priority_number are valid before comparing
        # ValueError if class_year and priority_number are not the right values

    def testPullInto(self):
        """
        testPullInto tests the design of the PullInto function
        """
        # Test the UserId and RoomId
        # Pre-conditions are two User objects, one Room object, and DrawState is complete
        # Test the setters and getters of room objects by actually testing the state
        # of the dictionary in the Repo class   

    
    def testUndoPull(self):
        """"
        testUndoPull tests the design of the UndoPull function
        """
        # Test the ability of getRoomOf to withstand errors by actually testing the state
        # of the dictionary in the Repo class
        # Test for when the user has not pulled and is trying to undo their pull


    





