"""
CS 181AA Software Engineering
Author: Aditya Bhargava (HMC '23)
HMC Room Draw Logic Black Box Testing
=====================
The HMC Room Draw Logic Black Box tests the 
functionality and design specifications of the HMC Room Draw Logic.
"""

from roomdraw_logic import *
import unittest

# There is no special set-up required before we run the tests
# Tests requriement 3 and 7 from the final architecural proposal
class TestDrawLogic(unittest.TestCase):
    """
    Tests the Room Draw Logic of the HMC Room Draw Backend
    """
    def testComparePriority1(self):
        """
        testComparePriority tests the implementation 
        of the comparePriority function with 
        different graduation years and different priority numbers 
        """
        # Pre-conditions are two student objects
        User1 = User("98923", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        User2 = User("93933", 'XXXXX', "XXXXX", "XXXXXXX@g.hmc.edu", "2024",81, "MALE")

        self.assertEqual(DrawLogic.comparePriority(User1,"98923",User2,"93933"),User1)
    
    def testComparePriority2(self):
        """
        testComparePriority tests the implementation 
        of the comparePriority function with 
        different graduation years and same priority numbers 
        """
        # Pre-conditions are two student objects
        User3 = User("97383", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2024",45, "MALE")
        User4 = User("98234", 'XXXXX', "XXXXX", "XXXXXXX@g.hmc.edu", "2025",45, "MALE")
        self.assertEqual(DrawLogic.comparePriority(User3,"97383",User4,"98234"),User3)

    def testComparePriority3(self):
        """
        testComparePriority tests the implementation 
        of the comparePriority function with 
        same graduation year and different priority number
        """
        # Same graduation years and different priority numbers 
        User5 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        User6 = User("99101", 'XXXXX', "XXXXX", "XXXXXXX@g.hmc.edu", "2023",32, "FEMALE")
        self.assertEqual(DrawLogic.comparePriority(User5,User6),User6)
    


    def testIsRoomGenderLocked1(self):
        """
        testIsRoomGenderLocked1 tests the implementation of the 
        isRoomGenderLocked function with a room that is gender locked"""
        Room1 = Room("78878", "Case", 2, None, 202, "MALE", True)
        self.assertEqual(DrawLogic.isRoomGenderLocked(Room1, True))

    def testIsRoomGenderLocked2(self):
        """
        testIsRoomGenderLocked2 tests the implementation of the 
        isRoomGenderLocked function with a room that is not gender locked"""
        Room2 = Room("78878", "Case", 2, None, 202, None, True)
        self.assertEqual(DrawLogic.isRoomGenderLocked(Room2,False))
    


    def testDoesRoomMatchWithStudentGender1(self):
        """
        testDoesRoomMatchWithStudentGender1 tests the implementation of 
        the doesRoomMatchWithStudentGender function with a room that is not gender locked
        """
        Room1 = Room("78878", "Case", 2, None, 202, None, True)
        User1 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        self.assertEqual(DrawLogic.doesRoomMatchStudentGender(Room1,User1), True)
    
    def testDoesRoomMatchWithStudentGender2(self):
        """
        testDoesRoomMatchWithStudentGender2 tests the implementation of 
        the doesRoomMatchWithStudentGender function with a room that is gender 
        locked and matches the gender of the user
        """
        Room2 = Room("78878", "Case", 2, None, 202, "MALE", True)
        User2 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        self.assertEqual(DrawLogic.doesRoomMatchStudentGender(Room2,User2), True)
    
    def testDoesRoomMatchWithStudentGender3(self):
        """
        testDoesRoomMatchWithStudentGender3 tests the implementation of 
        the doesRoomMatchWithStudentGender function with a room that is 
        gender locked and matches the gender of the user
        """
        Room3 = Room("78878", "Case", 2, None, 202, "MALE", True)
        User3 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "FEMALE")
        self.assertEqual(DrawLogic.doesRoomMatchStudentGender(Room3,User3), False)
    

# The testIsFroshBumpLegal2 and 3 functions will be written for the other 8 dorms 
# (North, West, South, East, Drinkward, Atwood, Linde, and Sontag). We will use this 
# PDF to write more tests for each dorm 
# https://drive.google.com/drive/u/1/folders/11ewpgrXwwK2AjPxUZkr-TjYfKv8E-Bty (
# For example, In Atwood frosh may be bumped into an equivalent room on the same floor
# but not bumped into certain doubles)

    def testIsFroshBumpLegalCase1(self):
        """
        testIsFroshBumpLegal1 tests the implentation of the isFroshBumpLegal function
        with a desired_room that is not a frosh room
        """
        DesiredRoom1 = Room("78878", "Case", 2, None, 202, "MALE", False)
        ProposedRoom1 = Room("78878", "Case", 2, None, 203, "MALE", False) 
        user1 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "FEMALE")
        self.assertEqual(DrawLogic.isFroshBumpLegal(DesiredRoom1,ProposedRoom1,user1),True)

    def testIsFroshBumpLegalCase2(self):
        """
        testIsFroshBumpLegal2 tests the implentation of the isFroshBumpLegal function
        with a desired_room that is a frosh_room and the proposed_room being a valid room in Case 
        """
        DesiredRoom2 = Room("78878", "Case", 2, None, 202, "MALE", True)
        ProposedRoom2 = Room("78878", "Case", 2, None, 203, "MALE", False) 
        user2 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "FEMALE")
        self.assertEqual(DrawLogic.isFroshBumpLegal(DesiredRoom2,ProposedRoom2,user2),True)

    def testIsFroshBumpLegalCase3(self):
        """
        testIsFroshBumpLegal3 tests the implentation of the isFroshBumpLegal function
        with a desired_room that is a frosh_room and the proposed_room being an
        invalid room in Case (different floor). The rules states that "In Case,
        frosh may only be bumped within corridors"
        """
        DesiredRoom3 = Room("78878", "Case", 2, None, 202, "MALE", True)
        ProposedRoom3 = Room("78878", "Case", 1, None, 203, "MALE", False) 
        user3 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "FEMALE")
        self.assertEqual(DrawLogic.isFroshBumpLegal(DesiredRoom3,ProposedRoom3,user3), False)

class TestDrawAction(unittest.TestCase):
    """Tests the potential actions a user can utilize when using the Room Draw App"""
    def testCanPullInto1(self):
        """
        testCanPullInto1 tests the implementation of the canPullInto function
        as the user attempting to pull has a higher priority than CurrentUserInRoom1
        """
        # Pre-conditions are one User object, one Room object, and  
        # getUserIn is complete

        # User1 has higher priority than CurrentUserInRoom1 
        User1 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        Room1 = Room("78878", "Case", 2, None, 202, "MALE", False)
        CurrentUserInRoom1 = User("67333", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100)
        self.assertEquals(DrawAction.canPullInto("96782","78878"),True)

    def testCanPullInto2(self):
        """
        testCanPullInto2 tests the implementation of the canPullInto function
        as the user attempting to pull has lower priority than CurrentUserInRoom2
        """

        # User2 has lower priority than CurrentUserInRoom2
        User2 = User("55589", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2024",42, "MALE")
        Room2 = Room("78878", "Case", 2, None, 202, False)
        CurrentUserInRoom2 = User("77222", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100)
        self.assertEquals(DrawAction.canPullInto("55589","78878"),False)

    
    def testCanPullInto3(self):
        """
        testCanPullInto3 tests the implementation of the canPullInto function
        as the user is attempting to pull into a room without a user
        """
        # User3 is attempting to pull into a room with no user
        User3 = User("55589", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        RoomHasNoUser = Room("78878", "Case", 2, None, 202, None, False)
        self.assertEquals(DrawAction.canPullInto("55589","78878"),False)
    
    # Testing Plan for froshBumping in canPullInto (step 5):
    # 1) No Frosh Bumping
    # 2) Frosh Bumping but the proposed room is invalid so canPullInto
    #    returns False
    # 3) Frosh Bumping but the proposed room is valid so canPullInto
    #    returns True

    # Testing Plan for doesRoomMatchStudentGender (step 6):
    # 1) No Gender locking declared
    # 2) Gender of room matches the gender of the student so canPullInto
    #    returns True
    # 3) Gender of room does not match the gender of the student so canPullInto
    #    returns False 


    def testPullInto1(self):
        """
        testPullInto tests the implementation of the PullInto function where User1
        has higher priority than CurrentUserInRoom1
        """
        User1 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        Room1 = Room("78878", "Case", 2, None, 202, None, True)
        CurrentUserInRoom1 = User("67333", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100, "MALE")
        self.assertEquals(DrawAction.pullInto("96782","78878"),None)

    def testPullInto2(self):
        """
        testPullInto tests the implementation of the PullInto function where User2
        has lower priority than CurrentUserInRoom2
        """
        # User2 has lower priority than CurrentUserInRoom2
        User2 = User("55589", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        Room2 = Room("78878", "Case", 2, None, 202, None, True)
        CurrentUserInRoom2 = User("18282", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",100, "FEMALE")
        self.assertEquals(DrawAction.pullInto("55589","78878"),None)
    
    def testPullInto3(self):
        """
        testPullInto tests the implementation of the PullInto function where User3
        User3 is attempting to pull into a room with no user
        """
        User3 = User("55589", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42, "MALE")
        RoomHasNoUser3 = Room("78878", "Case", 2, None, 202, None, True)
        self.assertEquals(DrawAction.PullInto("55589","78878"),None)
    
    def testUndoPull1(self):
        """"
        testUndoPull1 tests the implementation of the UndoPull function
        """
        # Pre-conditions are one room object and one student object
        User1 = User("96782", "XXXXX", "XXXXX", "XXXXXXX@g.hmc.edu", "2023",42)
        RoomUser1occupies = Room("78878", "Case", 2, None, 202, True)
        self.assertEquals(DrawAction.undoPullInto("96782", "78878"),None)
    
    def testUndoPull2(self):
        """
        testUndoPull2 tests the implementation of the UndoPull function by testing
        if an error is raised when a user that has not pulled attempts to undo their pull 
        """
        pass
    
    def testCanRoomBeGenderLocked1(self):
        """
        testCanRoomBeGednerLocked1 tests the implementation of the 
        canRoomBeGenderLocked by checking if a room of students with the same 
        gender as the user is already occupying the room. Should return True (
        Mocks the ASHMC petition process)
        """
        pass
    
    def testCanRoomBeGenderLocked2(self):
        """
        testCanRoomBeGednerLocked1 tests the implementation of the 
        canRoomBeGenderLocked by checking if a room of students with a different 
        gender as the user is already occupying the room. Should return False
        """
        pass

    def testDeclareRoomGenderLocked1(self):
        """
        testDeclareRoomGenderLocked1 tests the implementation of the 
        DeclareRoomGenderLocked1 by having a user declare a room to be gender-locked
        for a valid room (return None)
        """
        pass

    def testDeclareRoomGenderLocked2(self):
        """
        testDeclareRoomGenderLocked2 tests the implementation of the 
        DeclareRoomGenderLocked1 by having a user declare a room to be gender-locked
        for an invalid room (return an Error)
        """
        pass
    
    def testundoRoomGenderLocked1(self):
        """
        No Black Box Testing has this is an internal function and updates the state
        of the room (only utilized when a person is bumped out of a room)
        """
        pass

    def testBumpFrosh1(self):
        """
        testBumpFrosh1 tests the implementation of BumpFrosh by having a user pull into
        a room has no frosh_room attribute (return an Error) 
        """
        pass

    def testBumpFrosh2(self):
        """
        testBumpFrosh2 tests the implementation of BumpFrosh by having a user pull into
        a room that has a frosh_room attribute and a valid proposed room (return None)
        """
        pass

    def testBumpFrosh3(self):
        """
        testBumpFrosh3 tests the implementation of BumpFrosh by having a user pull into
        a room that has a frosh_room attribute and an invalid proposed room (return an Error)
        """
        pass




