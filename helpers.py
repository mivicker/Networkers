from math import sqrt, log

class Player:
    def __init__(self, name, starting_money, level):
        self.name = name
        self.starting_money = starting_money
        self.level = level
        self.location = [0,0]
        self.cash = 1000

    def approach_customer(self, customer):
        squares  = [(pin - perch) ** 2 for pin, perch in zip(self.location, customer.location)]
        distance = sqrt(sum(squares))
        if distance > 10:
            return "You're too far away."
        print(f"{self.name}: Would you like to sign up for our internet?")
        customer.tell_enrolled() if customer.enrolled else customer.sign_up()

    def set_up_node(self, nodes, customers):
        if self.cash < 500:
            return "Can't afford this."
        self.cash -= 500
        nodes.append(Node(self.location, 100, customers))

    def move(self, direction):
        self.location = [dim + drec for dim, drec in zip(self.location, direction)]

class Node:
    def __init__(self, location, strength, customers):
        self.location = location
        self.strength = strength
        for customer in customers:
            customer.test_connection(location, strength)

        print(f"Node set at: {self.location}")

class Customer:
    def __init__(self, name, interest_level, connection_need, location, enrolled = False):
        self.name = name
        self.interest_level = interest_level
        self.enrolled = enrolled
        self.connection_need = connection_need
        self.location = location
        self.connection_strength = -500

    def tell_enrolled(self):
        print(f"{self.name}: What are you asking me for, I'm already signed up!")

    def sign_up(self):
        if self.connection_strength >= self.connection_need:
            print(f"{self.name}: Okay, yeah, hook me up!")
            self.enrolled = True
            print(f"{self.name} was successfully connected at {self.connection_strength * 100} percent power.")
        else:
            print(f"{self.name}: You're not providing enough connection strength here.")

    @staticmethod
    def connection_test(power, d):
        return max( (-(1/power) * d + 1), 0)

#Need logic to add connections together, or replace with max connection, or to subtract if a node is removed. 

    def test_connection(self, node_location, equipment_power):
        squares  = [(pin - node) ** 2 for pin, node in zip(self.location, node_location)]
        distance = sqrt(sum(squares))
        self.connection_strength = self.connection_test(equipment_power, distance)
