import sqlite3

class OrderHistory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
    
    def viewHistory(self, userID):
        pass
    
    def viewOrder(self, userID, orderID):
        pass
    
    def createOrder(self, userID, quantity, cost, date):
        pass
    
    def addOrderItems(self, userID, orderID):
        pass
