"""
Repository Test
===============
Use python unitest framework to automate the tests. All of the tests will run
once with in_memory_only set to True and once set to False.

1. Test repository.__init__() and repository.getX()
- Create a local database
- Populate the database with
    - 8 Rooms
    - 2 Residence Hall
    - 3 Floor Plans, (1 residence hall has 1 floor, the other has two)
    - 8 Users (7 assigned, 1 unassigned)
    - Room <-> User that assignes 7 users
- Set up repository to connect to this database.
- Test the following functions
    - repository.get_user(id)
        - returns user
        - no user exception
    - repository.get_room(id)
        - returns room
        - no room exception
    - repository.get_all_room_ids()
        - return list of all room ids
    - repository.get_all_rooms()
        - return list of all rooms
    - repository.get_floor_plan(id)
        - return floor plan
        - no floor plan exception
    - repository.get_residence_hall(id)
        - return residence hall
    - repository.get_all_residence_halls()
        - return list of all residence halls
    - repository.get_all_residence_hall_ids()
        - return list of residence hall ids
    - repository.get_user_in(id)
        - return User
        - return None
        - raise no room exception
    - repository.get_room_of(id)
        - return Room
        - return None
        - raise no user exception
    - getUser_id_to_room_id_dict()
        - return dict from user_id to room_id

2. Test transactions
- Create a local database
- Populate the database with
    - 8 Rooms
    - 2 Residence Hall
    - 3 Floor Plans, (1 residence hall has 1 floor, the other has two)
    - 8 Users (7 assigned, 1 unassigned)
    - Room <-> User that assignes 7 users
- Individual Test
    - For each create method in Transaciton class, test that after we create, we
    can call get on it to get the object.
    - For each update method in Transaction class, test that after we update, we
    can call get on it to get an updated object.
- Multiple Write Test
    - Create 100 concurrent create room transactions
    - Changes are reflected in database (100 rooms created)
- Concurrent Read Test: Can read data while transaction ongoing
    - Create a transaction that reads a User, update the User, wait for 1 sec,
    and commit
    - At the same time, perform repository.get_user(user_id).
    - This should return the stale data.
- Transaction for on different table should not block one another
    - Create a transaction for User that sleeps for 1 sec
    - Create a transaction for Room that sleeps for 1 sec
    - Run the two transactions. It should not take around 1 sec.
- Transaction Race Condition Test: no race conditions among transactions
    - Create a transaction that checks that a user's name matches the default 
      name. Then, wait for 1 sec. If it matches, change the user last name.
    - Create a transaction that changes the user's first name to be different
      from the default name.
    - Verify that both first name and last name cannot be changed at the same
      time.
    - Repeat this test concept with the User <-> Room map.
"""
from app import app
from models import User, Room
from repository import get_db, Repository
import unittest

import pathlib

class TestRepositoryGetMinimal(unittest.TestCase):
    """
    Create one User, one Room, one FloorPlan, and one ResidenceHall.
    Put the user to the room. Check that all the get/modify requests
    work correctly.
    """

    DATBASE_TEST_FILE = './test_database.db'
    DATABASE_SCHEMA = './schema.sql'
    DATABASE_INITIAL = './initial_minimal.sql'

    def setUp(self):
        """
        Create an empty database and populate it according to
        DATABASE_INITIAL sql file.
        """
        # remove database test file
        pathlib.Path(self.DATBASE_TEST_FILE).unlink(missing_ok=True)

        # enter the application context
        self.app_ctx = app.app_context()
        self.app_ctx.__enter__()

        # create a new database test file at the same location
        db = get_db(self.DATBASE_TEST_FILE)
        with app.open_resource(self.DATABASE_SCHEMA, mode='r') as f:
            db.cursor().executescript(f.read())
        with app.open_resource(self.DATABASE_INITIAL, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

        # set repository to read/write to the test file
        self.repo = Repository(db_path=self.DATBASE_TEST_FILE)

    def tearDown(self):
        """
        Remove database created by setUp.
        """
        # remove database test file
        pathlib.Path(self.DATBASE_TEST_FILE).unlink(missing_ok=True)
        # exit the application context and clean up
        self.app_ctx.__exit__(None, None, None)

    def test_get_user(self):
        expected = User(
            id="1",
            first_name="Adi",
            last_name="B",
            email="adib@g.hmc.edu",
            class_year="junior",
            priority_number=1,
            gender="male",
        )
        actual = self.repo.get_user("1")
        self.assertEqual(actual, expected)
    
    def test_get_user_not_found(self):
        with self.assertRaises(KeyError):
            self.repo.get_user("user_id_not_in_db")

    def test_get_room(self):
        expected = Room(
            id="room1",
            residence_hall_name="drinkward",
            floor_number=1,
            suite=None,
            number="121",
        )
        actual = self.repo.get_room("room1")
        self.assertEqual(actual, expected)

    def test_get_room_not_found(self):
        with self.assertRaises(KeyError):
            self.repo.get_room("room_id_not_in_db")

    def test_get_all_room_ids(self):
        expected = ["room1"]
        actual = self.repo.get_all_room_ids()
        self.assertEqual(actual, expected)
    
    def test_get_all_rooms(self):
        expected = [Room(
            id="room1",
            residence_hall_name="drinkward",
            floor_number=1,
            suite=None,
            number="121",
        )]
        actual = self.repo.get_all_rooms()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()