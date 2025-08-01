# holds classes 

# importing datetime module 
# this allows to automatially tag each expense with the current date 
import datetime 

# defining expense class and __init__() method 
# new learning: ="" means that note is optional for the user, avoids errors if missing 
# reusable blueprint to represent each expense, this is OPP Object Oriented Programming 
# datetime.datetime.now() gets current time 
# .strftime() formats into readable string 
class Expense: 
    def __init__(self, amount, category, note=""): 
        self.amount = amount 
        self.category = category 
        self.note = note 
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

    # converting object into dictionary of key value pairs to save in json format later
    # can't directly save objects to a .json file need to turn them into plain data types like dict 
    def to_dict(self): 
        return {
            "amount": self.amount, 
            "category": self.category, 
            "note": self.note,
            "date": self.date
        }