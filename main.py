from datetime import date
from application.salary import salary
from application.db.people import people
from application.cow import cow_say

if __name__ == '__main__':    
    print(date.today())
    people()
    salary()
    cow_say('Маловато будет!')