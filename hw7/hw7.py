"""
INTRO
"""
from functools import reduce

class Plant:
    """
    A representation of a plant. Implements a constructor with defaulting values(except one),
     a represent overload and 2 more methods:
    # get_maintenance_cost.
    # purchase_decision.
    """
    def __init__(self, name: str,
                 aesthetics: int = 1,
                 water_consumption_month: int = 1,
                 average_month_yield: int = 1,
                 seasonal: bool = False):
        """
        Initializes an instance of Plant.
        :param name: (str) the name of the plant.
        :param aesthetics: (int) the level of aesthetics the plant is valued at.
        :param water_consumption_month: (int) the plant's monthly consumption of water amount
        :param average_month_yield: (int) the value the plant creates every month
        :param seasonal: (bool) whether the plant is year-round (True) plantation or only 6 months (False).
        """
        self.name = name
        self.aesthetics = aesthetics
        self.water_consumption_month = water_consumption_month
        self.average_month_yield = average_month_yield
        self.seasonal = seasonal

    def get_maintenance_cost(self, func1):
        """
        Invokes the given argument as a function with the instance itself (self) as input argument.
        :param func1: a function object.
        :return:
        """
        return func1(self)

    def purchase_decision(self, func1, func2):
        """
        Invokes the first given argument as a function with two inputs (by order):
         the instance itself, and the result of the second argument invoked as a function with the instance
         itself (self) as input argument.
        :param func1: a function object.
        :param func2: a function object.
        :return:
        """
        return func1(self, func2(self))

    def __repr__(self):
        """
        overloads the python object __repr__ method.
        :return: str
        """
        return "name={}".format(self.name)


class GardenManager:
    """
    A representation of a garden management system. Implements a constructor with no defaulting values,
     a represent overload and 1 more methods:
     # action.
    """
    def __init__(self, plants_in_garden: list):
        """
        Initializes an instance of GardenManager.
        :param plants_in_garden: a list of the plants which are in the garden.
        """
        self.plants_in_garden = plants_in_garden

    def action(self, func1):
        """
        Invokes the given argument as a function with the instance itself (self) as input argument.
        :param func1: a function object.
        :return:
        """
        return func1(self)

    def __repr__(self):
        """
        overloads the python object __repr__ method.
        :return: str
        """
        return "Number of plants = {0}".format(len(self.plants_in_garden))
#

"""
PART A - Lambda functions
"""

# Q1
get_cost_lmbd = lambda x: x.water_consumption_month

# Q2
get_yearly_cost_lmbd = lambda x: x.water_consumption_month * 6 if x.seasonal else x.water_consumption_month * 12

# Q3
worth_investing_lmbd = lambda x: x.average_month_yield > x.water_consumption_month

# Q4
declare_purchase_lmbd = lambda x, worth: x.name + ":yes" if worth or (not worth and x.aesthetics >= x.get_cost_lmbd) else x.name + ":no"

# Q5

get_plants_names_lmbd = lambda x: list(map(lambda x: x.name, sorted(x.plants_in_garden, key=lambda x: x.name)))

"""
PART B - High order functions
"""

# Q1 -
def retrospect(garden_manager):
    """
    Function that get a garden manger and return a list of flowers name that worth investing
    :param garden_manager: garden manager
    :return: return a list of flowers name that worth investing
    """
    l = list(filter(lambda x: worth_investing_lmbd(x), garden_manager.plants_in_garden))
    return list(map(lambda x: x.name, l))

# Q2 -
def get_total_yearly_cost(garden_manager):
    """
    Function that get a garden manger and return total yearly cost of all the flowers
    :param garden_manager:garden manger
    :return: return total yearly cost of all the flowers
    """
    return reduce(lambda x,y: x+y, list(map(lambda x: get_yearly_cost_lmbd(x), garden_manager.plants_in_garden)))

# Q3 -
def get_aesthetics(garden_manager):
    """
    Function that get a garden manger and return list of all aesthetics
    :param garden_manager: garden manger
    :return: return list of all aesthetics
    """
    return list(map(lambda x: x.aesthetics, garden_manager.plants_in_garden))

"""
PART C - University gate
"""

class GateLine:
    def __init__(self, max_capacity):
        self.max_capacity=max_capacity
        self.q = []

    def new_in_line(self, student_id, priority_id_holder):
        """
        Function that add a new student to the queue
        :param student_id: student id
        :param priority_id_holder:bool if has priority or not
        """
        i = len(self.q) - 1
        if len(self.q) < self.max_capacity: #check if theres room in line
            self.q.append((student_id, priority_id_holder)) #if so append
        elif priority_id_holder: #else check if the student has priority
            while len(self.q) >= self.max_capacity: #if so remove all students without priority untill he has room in line
                if not self.q[i][1]:
                    self.q.pop(i)
                i -= 1
            self.q.append((student_id, priority_id_holder)) #in the end append anyway

    def open_gate(self):
        """
        Function that takes out students by priority and return their id
        :return: return their id
        """
        if self.q == []:
            return None
        b = False
        for j in self.q: #check if priority in list
            if j[1]==True:
                b = True
        if b: #if so, remove first priority and return
            for i in self.q:
                if i[1] == True:
                    x = i[0]
                    self.q.remove(i)
                    return x
        else: #else remove first
            x = self.q[0]
            self.q.pop(0)
            return x


    def is_empty(self):
        """
        Function that check if queue is empty
        :return:bool true / false
        """
        if self.q == []:
            return True
        else:
            return False

    def show_who_is_in_line(self):
        """
        Function that shows who is next in line by priority
        :return: list of ids ordered by who is first in line
        """
        first = list(filter(lambda x:x[1] == True, self.q)) #filer list by priority == True
        last = list(filter(lambda x:x[1] == False, self.q))#filer list by priority == Flase
        final = first + last #add the priority list and than the not priority list to a new list
        return list(map(lambda x:x[0], final)) #return new list of ids by priority
