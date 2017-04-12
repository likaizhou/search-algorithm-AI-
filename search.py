### File: search.py 
### This file includes three class definitions: Queue, Node, Search

from exceptions import * 

class Queue:
    """
    A Queue class to be used in combination with state space
    search. The enqueue method adds new elements to the end. The
    dequeue method removes elements from the front.
    """
    def __init__(self):
        self.queue = []
    def __str__(self):
        result = "Queue contains " + str(len(self.queue)) + " items\n"
        for item in self.queue:
            result += str(item) + "\n"
        return result
    def enqueue(self, node):
        self.queue.append(node)
    def dequeue(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            raise RunTimeError
    def empty(self):
        return len(self.queue) == 0 

class Node:
    """
    A Node class to be used in combination with state space search.
    A node contains a state, a parent node, the name of the operator
    used to reach the current state, and the depth of the node in
    the search tree.  The root node should be at depth 0. The method
    repeatedState can be used to determine if the current state
    is the same as the parent's parent's state. Eliminating such
    repeated states improves search efficiency.
    """
    def __init__(self, state, parent, operator, depth):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
    def __str__(self):
        result = "State: " + str(self.state)
        result += " Depth: " + str(self.depth)
        if self.parent != None:
            result += " Parent: " + str(self.parent.state)
            result += " Operator: " + self.operator
        return result
    def repeatedState(self):
        if self.parent == None: return 0
        if self.parent.parent == None: return 0
        if self.parent.parent.state.equals(self.state): return 1
        return 0 

class Search:
    """
    A general Search class that can be used for any problem domain.
    Given instances of an initial state and a goal state in the
    problem domain, this class will print the solution or a failure
    message.  The problem domain should be implemented as a class
    that represents the state and contains the following methods:
    applyOperators(): returns a list of successors for the state
    instance, some of which may be invalid
    operatorNames(): returns a list of strings representing the names
    of the operators that were applied
    illegal(): tests whether the state instance is valid
    equals(state): tests whether the state instance is equivalent to
    the given state
    __str__(): returns a string representation of the state instance
    
    See the implementation of the missionary and cannibals problem
    as an example.
    """
    def __init__(self, initialState, goalState):
        self.q = Queue()
        self.q.enqueue(Node(initialState, None, None, 0))
        self.goalState = goalState
        solution = self.execute()
        if solution == None:
            print "Search failed"
        else:
            self.showPath(solution)
    def execute(self):
        while not self.q.empty():
            current = self.q.dequeue()
            if self.goalState.equals(current.state):
                return current
            else:
                successors = current.state.applyOperators()
                operators = current.state.operatorNames()
                for i in range(len(successors)):
                    if not successors[i].illegal():
                        n = Node(successors[i],
                                 current,
                                 operators[i],
                                 current.depth+1)
                        if n.repeatedState():
                            del(n)
                        else:
                            self.q.enqueue(n)
        return None
    def showPath(self, node):
        path = self.buildPath(node)
        for current in path:
            if current.depth != 0:
                print "Operator:", current.operator
            print current.state
        print "Goal reached in", current.depth, "steps"
    def buildPath(self, node):
        result = []
        while node != None:
            result.insert(0, node)
            node = node.parent
        return result
