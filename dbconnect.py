import psycopg2 as psql

class Database():
    """A class used to connect to and execute queries on psql databases"""
    def __init__(self) -> None:
        #gets database info (defaults in brackets)
        self.name = input('DB Name (postgres): ')
        self.user = input('User (postgres): ')
        self.pwd = input('Password (1): ')
        if self.name == '':
            self.name = 'postgres'
        if self.user == '':
            self.user = 'postgres'
        if self.pwd == '':
            self.pwd = '1'
        self.connect()
        
    def connect(self):
        """Connects to database using arguments passed on instantiation"""
        try:
            #connects to and adds controller to database
            self.db = psql.connect(dbname=self.name, user=self.user, password=self.pwd)
            self.ctrl = self.db.cursor()
        except:
            #Error code on connection
            return 1
        
    def query(self,queries=['SELECT * FROM raw.game;']):
        """Queries the database

        Parameters:
            queries - SQL queries passed as a list of strings
        Returns:
            The output of the queries as a list of lists of tuples
            1 - if there is any error
        """
        self.output = []
        try:
            for query in queries:
                self.ctrl.execute(query)
                self.output.append(self.ctrl.fetchall())
            return self.output
        except:
            return 2

    def close(self):
        """Close comms"""
        self.ctrl.close()
        self.db.close()
        return 0


if __name__ == '__main__':
    db = Database()
    print(db.query())

