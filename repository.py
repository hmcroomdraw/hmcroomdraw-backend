"""
Repository
==========

The repository stores all persistent information of the application in one
place. It stores one copy of data as in memory, and stores another copy in a 
remote SQL database. When the user wants to read data, the repository returns a
copy of the data from the in-memory database. This is done by calling get
functions on the repository such as repository.get_user(id) or
repository.get_all_room_ids(). When the user wants to write data, the repository
tries to write the data to the remote database. If it succeeds, it updates the
in-memory database to reflect that. When the user wants to write data, they have
to create a transaction by calling repository.create_transaction(). This returns
a transaction object that performs a set of operations atomically. Here's an
example on how to create and use a transaction:

# if user is in room1, put the user in room2 instead, else do nothing.
with repository.create_transaction() as transaction:
    current_room = transaction.get_room_of(user_id)
    if current_room.id == room1_id:
        transaction.set_user_to_room(user_id, room2_id)

We will use SQLite MEMORY storage for the in-memory database. We planned to use
python objects and locks, but because python web servers create a new process
for each request (due to CPython's global interpreter lock), we cannot use locks
in the thread level to share memory across processes. The MEMORY storage can
process read requests quickly, but does not allow row-level locking. We believe
this is a good trade-off since our application is write heavy. (In a real
application, we have to perform a performance test to see whether this is the
right choice.)

For the presistent remote database, we will also use SQLite so that we don't
have to work with mutiple types of databases.

The SQL queries will be managed by SQLAlchamy.
"""

from models import *
from typing import Optional

from app import app
from flask import g
import sqlite3

import pathlib

DATABASE = './database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    pathlib.Path('./database.db').unlink(missing_ok=True)
    with app.app_context():
        db = get_db()
        with app.open_resource('initial.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

class Repository:
    def __init__(self, in_memory_only=True):
        """
        Initialize the repository from the remote database.
        If in_memory_only is True, create an empty repository that operates
        solely in-memory.
        Raise DatabaseConnectionError if cannot connect to database.
        """
        if not in_memory_only:
            raise NotImplementedError()
        
        self.cursor = get_db().cursor()

    def get_user(self, id: UserId) -> User:
        """
        Get a copy of User from UserId.
        Raise KeyError if id does not exist.
        Raise DatabaseConnectionError if cannot connect to database.
        """
        # Read user from in-memory database.
        cursor = self.cursor
        cursor.execute('select * from users where id = ?', ('1',))
        result = cursor.fetchall()[0]
        print(result)
        return User(*result)

    def get_room(self, id: RoomId) -> Room:
        """
        Get a copy of Room from RoomId.
        Raise KeyError if id does not exist.
        Raise DatabaseConnectionError if cannot connect to database.
        """
        # Read room from in-memory database.
        pass

    def get_all_room_ids(self) -> list[RoomId]:
        pass

    def get_all_rooms(self) -> list[Room]:
        pass

    def get_floor_plan(self, id: FloorPlanId) -> FloorPlan:
        pass

    def get_residence_hall(self, id: ResidenceHallId) -> ResidenceHall:
        pass

    def get_all_residence_halls(self) -> list[ResidenceHall]:
        pass

    def get_all_residence_hall_ids(self) -> list[ResidenceHallId]:
        pass

    def get_user_in(self, room_id: RoomId) -> Optional[User]:
        pass

    def get_room_of(self, user_id: UserId) -> Optional[Room]:
        pass

    def getUser_id_to_room_id_dict(self) -> dict[UserId, RoomId]:
        pass

    def create_transaction(self) -> 'Repository.Transaction':
        return
    
    class Transaction:
        def __init__(self):
            """
            Create a transaction. When a resource is read from the table,
            that table is locked until the transaction is complete (due to
            MySQL MEMORY database's lack of row-level lock).
            """
            # Bind the repository object to this class
            # Create a transaction in the in-memory repository
            # Create a transaction in the remote repository
            
            pass

        def __enter__(self):
            """
            Starts the transaction. Automatically gets called when object goes
            into `with` scope.

            For example, you can write:
            with repository.create_transaction() as transaction:
                current_room = transaction.get_room_of(user_id)
                if current_room.id == room1_id:
                    transaction.set_user_to_room(user_id, room2_id)
            
            For more information about the with statement, see:
            https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
            """
            # do nothing
            return

        def __exit__(self):
            """
            Ends the transaction. Autometically gets called when object goes
            out of `with` scope.
            """
            # Commit the transaction to the in-memory repository
            # If success,
            # Commit the transaction to the remote repository
            # If fail,
            # Rollback changes in both the remote and in-memory repository
            pass

        def get_user(self, id: UserId) -> User:
            """Get a copy of User from UserId"""
            # read from in-memory repository only
            pass

        def create_user(self, user: User) -> User:
            """
            Create a user from information in the user object. The id of the
            User object in the argument must be None. The id will be provided
            in the returned object.

            Raises Exception if user.id is not None.
            Raises Exception if user already exists.
            Assigns new a id to user object.
            Returns the modified user object.
            """
            # write to both in-memory and remote repository
            pass
            
        def update_user(self, user: User):
            """
            Update the user associated with user.id to have the
            new information.
            """
            # write to both in-memory and remote repository
            pass

        def get_room(self, id: RoomId) -> Room:
            """Get a copy of Room from RoomId"""
            pass

        def create_room(self, room: Room) -> Room:
            pass

        def update_room(self, room: Room):
            pass

        def get_all_room_ids(self) -> list[RoomId]:
            pass

        def get_all_rooms(self) -> list[Room]:
            pass

        def get_floor_plan(self, id: FloorPlanId) -> FloorPlan:
            pass
        
        def create_floor_plan(self, floor_plan: FloorPlan) -> FloorPlan:
            pass

        def update_floor_plan(self, floor_plan: FloorPlan):
            pass

        def get_residence_hall(self, id: ResidenceHallId) -> ResidenceHall:
            pass

        def create_residence_hall(self, residence_hall: ResidenceHall
        ) -> ResidenceHall:
            pass

        def update_residence_hall(self, residence_hall: ResidenceHall
        ) -> ResidenceHall:
            pass

        def get_all_residence_halls(self) -> list[ResidenceHall]:
            pass

        def get_all_residence_hall_ids(self) -> list[ResidenceHallId]:
            pass

        def get_user_in(self, room_id: RoomId) -> Optional[User]:
            pass

        def set_user_to_room(self, user_id: UserId, room_id: RoomId):
            pass

        def set_user_to_no_room(self, user_id: UserId):
            pass

        def get_room_of(self, user_id: UserId) -> Optional[Room]:
            pass

        def set_room_to_user(self, room_id: RoomId, user_id: Optional[User]):
            pass

        def set_room_to_no_user(self, room_id: RoomId):
            pass

        def get_user_to_room_dict(self) -> dict[UserId, RoomId]:
            pass