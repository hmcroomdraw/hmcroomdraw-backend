"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic Black Box Testing
=====================
The HMC Room Draw Logic Black Box test file tests the 
functionality and design specifications of the HMC Room Draw Logic.

"""

from roomdraw_logic import *
import unittest

# There is no special set-up required before we run the tests
# Tests requriement 3 and 7 from the final archietcural proposal
class TestDrawLogic(unittest.TestCase):
    """
    Tests the Room Draw Logic of the HMC Room Draw Backend
    """
    def testComparePriority1(self):
        """
        testComparePriority tests the implementation 
        of the comparePriority function
        """
        # Pre-conditions are two student objects
        # Santi and I will create a mock database that has the user and room objects
        # Different graduation years and different priority numbers
        User1 = User("98923", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        User2 = User("93933", 'XXXXX', "XXXXX", "XXXXXXX@g.hmc.edu", "2024",81)

        # Different graduation years and same priority numbers
        self.assertEqual(DrawLogic.comparePriority(User1,"98923",User2,"93933"),User1)

        # Different graduation years and different priority numbers
        User3 = User("97383", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",45)
        User4 = User("98234", 'XXXXX', "XXXXX", "XXXXXXX@g.hmc.edu", "2024",81)
        self.assertEqual(DrawLogic.comparePriority(User3,"97383",User4,"98234"),User3)

        # Same graduation years and different priority numbers 
        User5 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        User6 = User("99101", 'XXXXX', "XXXXX", "XXXXXXX@g.hmc.edu", "2023",32)
        self.assertEqual(DrawLogic.comparePriority(User5,User6),User6)

class TestDrawAction(unittest.TestCase):
    """Tests the potential actions a user can utilize when using the Room Draw App"""
    def testCanPullInto(self):
        """
        testCanPullInto tests the design of the canPullInto function
        """
        # Pre-conditions are one User object, one Room object, and  
        # getUserIn is complete
        # More tests would include testing the student object from the database,
        # and making sure the priority numbers is valid

        # User1 has higher priority than CurrentUserInRoom1 
        User1 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        Room1 = Room("78878", "Case", 2, None, 202, True)
        CurrentUserInRoom1 = User("67333", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100)
        self.assertEquals(DrawAction.canPullInto("96782","78878"),True)

        # User2 has higher priority than CurrentUserInRoom2
        User2 = User("44456", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2022",100)
        Room2 = Room("78878", "Case", 2, None, 202, True)
        CurrentUserInRoom2 = User("12345", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",1)
        self.assertEquals(DrawAction.canPullInto("44456","78878"),True)

        # User3 has lower priority than CurrentUserInRoom3
        User3 = User("55589", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        Room3 = Room("78878", "Case", 2, None, 202, True)
        CurrentUserInRoom3 = User("77222", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100)
        self.assertEquals(DrawAction.canPullInto("55589","78878"),False)

        # User4 has lower priority than CurrentUserInRoom4
        User4 = User("38383", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2025",1)
        Room4 = Room("78878", "Case", 2, None, 202, True)
        CurrentUserInRoom4 = User("63734", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100)
        self.assertEquals(DrawAction.canPullInto("38383","78878"),False)

        # User5 is attempting to pull into a room with no user
        User5 = User("55589", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        RoomHasNoUser = Room("78878", "Case", 2, None, 202, True)
        self.assertEquals(DrawAction.canPullInto("55589","78878"),True)

    def testPullInto(self):
        """
        testPullInto tests the design of the PullInto function
        """
        # Pre-conditions are two User objects, one Room object, and DrawState is complete
        # User1 has higher priority than CurrentUserInRoom1 
        User1 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        Room1 = Room("78878", "Case", 2, None, 202, True)
        CurrentUserInRoom1 = User("67333", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100)
        self.assertEquals(DrawAction.pullInto("96782","78878"),None)
        self.assertEquals(DrawState.getUserIn("78878"), User1)
        self.assertEquals(DrawState.getRoomOf("96782"),Room1)
        # Error when asserting the last test
        #self.assertEquals(DrawState.getRoomOf("67333",None)

        # User2 has higher priority than CurrentUserInRoom2
        User2 = User("44456", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2022",100)
        Room2 = Room("78878", "Case", 2, None, 202, True)
        CurrentUserInRoom2 = User("12345", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",1)
        self.assertEquals(DrawAction.pullInto("44456","78878"),None)
        self.assertEquals(DrawState.getUserIn("78878"), User2)
        self.assertEquals(DrawState.getRoomOf("44456"),Room2)
        #self.assertEquals(DrawState.getRoomOf("12345",None)

        # User3 has lower priority than CurrentUserInRoom3
        User3 = User("55589", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        Room3 = Room("78878", "Case", 2, None, 202, True)
        CurrentUserInRoom3 = User("18282", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100)
        self.assertEquals(DrawAction.pullInto("55589","78878"),None)
        self.assertEquals(DrawState.getUserIn("78878"),CurrentUserInRoom3)
        self.assertEquals(DrawState.getRoomOf("18282"),Room3)
        #self.assertEquals(DrawState.getRoomOf("55589",None)


        # User4 has lower priority than CurrentUserInRoom4
        User4 = User("38383", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2025",1)
        Room4 = Room("78878", "Case", 2, None, 202, True)
        CurrentUserInRoom4 = User("63734", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100)
        self.assertEquals(DrawAction.pullInto("38383","78878"),None)
        self.assertEquals(DrawState.getUserIn("78878"),CurrentUserInRoom4)
        self.assertEquals(DrawState.getRoomOf("63734"),Room4)
        #self.assertEquals(DrawState.getRoomOf("55589",None)

        # User5 is attempting to pull into a room with no user
        User5 = User("55589", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        RoomHasNoUser5 = Room("78878", "Case", 2, None, 202, True)
        self.assertEquals(DrawAction.PullInto("55589","78878"),None)
        self.assertEquals(DrawState.getUserIn("78878"),User5)
        self.assertEquals(DrawState.getRoomOf("55589"),RoomHasNoUser5)
    
    def testUndoPull(self):
        """"
        testUndoPull tests the design of the UndoPull function
        """
        # Pre-conditions are one room object and one student object
        User1 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        RoomUser1occupies = Room("78878", "Case", 2, None, 202, True)
        self.assertEquals(DrawAction.undoPullInto("96782", "78878"),None)
        self.assertEquals(DrawAction.getRoomOf("96782"),None) 
        self.assertEquals(DrawAction.getUserIn("78878"),None)

        # More testing for when the user has not pulled and is trying to undo
        # their pull