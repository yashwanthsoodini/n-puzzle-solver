
# coding: utf-8

# In[1]:
import resource
import timeit
import numpy #importing numpy to create arrays
from copy import deepcopy


# In[2]:

class state: #creating the class that reresents the state of the game at a given time
    path = []
    cost = 0
    def __init__(self,ar):
        arg = deepcopy(ar)
        if(type(arg)==list):                       #parent state if the argument is a list
            self.parent = numpy.asarray(arg)
            self.parent = self.parent.reshape(3,3)
        else:                                     #parent state if the argument is a numpy array
            self.parent = arg
        path = []
        cost = 0
        self.childup = up(self.parent)            #child states
        self.childdown = down(self.parent)
        self.childleft = left(self.parent)
        self.childright = right(self.parent)
    def __eq__(self,other):
        return (self.parent == other.parent).all()


# In[3]:

def up(ar):
    ar = deepcopy(ar)
    ar = ar.reshape(9)
    for i in range(9):
        if(i>2 and ar[i]==0):
            ar[i] = ar[i-3]
            ar[i-3] = 0
            break
    ar = numpy.asarray(ar)
    ar = ar.reshape(3,3)
    return ar
def down(ar):
    ar = deepcopy(ar)
    ar = ar.reshape(9)
    for i in range(9):
        if(i<6 and ar[i]==0):
            ar[i] = ar[i+3]
            ar[i+3] = 0
            break
    ar = numpy.asarray(ar)
    ar = ar.reshape(3,3)
    return ar
def left(ar):
    ar = deepcopy(ar)
    ar = ar.reshape(9)
    for i in range(9):
        if(i%3!=0 and ar[i]==0):
            ar[i]=ar[i-1]
            ar[i-1]=0
            break
    ar = numpy.asarray(ar)
    ar = ar.reshape(3,3)
    return ar
def right(ar):
    ar = deepcopy(ar)
    ar = ar.reshape(9)
    for i in range(9):
        if((i-2)%3!=0 and ar[i]==0):
            ar[i]=ar[i+1]
            ar[i+1]=0
            break
    ar = numpy.asarray(ar)
    ar = ar.reshape(3,3)
    return ar


# In[4]:

def contains(board,l):
    for i in l:
        if(board == i):
            return True
    return False


# In[5]:

input = [1,2,5,3,4,0,6,7,8]


# In[6]:

from Queue import *


# In[7]:
fringe = Queue(maxsize=0)
max_fringe_size = 0
fringe.put(state(input))


# In[8]:

explored = []


# In[9]:

goalstate1 = numpy.array([[0,1,2],[3,4,5],[6,7,8]])
goalstate2 = numpy.array([[1,2,3],[4,5,6],[7,8,0]])


# In[10]:

max_ram_usage = 0

# In[ ]:

board = fringe.get()

print(board.parent)
# In[ ]:
start_time = timeit.default_timer()

while((board.parent == goalstate1).all() == False):
    clone = deepcopy(board)
    explored = explored + [clone]
    fringelist = list(fringe.queue)
    fringelist = fringelist + explored
    childup = state(clone.childup)
    childdown = state(clone.childdown)
    childleft = state(clone.childleft)
    childright = state(clone.childright)
    #if (contains(childup,explored) and
    if not contains(childup,fringelist):
        print("1st if")
        childup.cost = childup.cost + clone.cost + 1
        childup.path = childup.path + clone.path
        childup.path = childup.path + ['up']
        fringe.put(deepcopy(childup))
    #if (contains(childdown,explored) and
    if not contains(childdown,fringelist):
        print("2nd if")
        childdown.cost = childdown.cost + clone.cost + 1
        childdown.path = childdown.path + clone.path
        childdown.path = childdown.path + ['down']
        fringe.put(deepcopy(childdown))
    #if (contains(childleft,explored) and
    if not contains(childleft,fringelist):
        print("3rd if")
        childleft.cost = childleft.cost + clone.cost + 1
        childleft.path = childleft.path + clone.path
        childleft.path = childleft.path + ['left']
        fringe.put(deepcopy(childleft))
    #if (contains(childright,explored) and
    if not contains(childright,fringelist):
        print("4th if")
        childright.cost = childright.cost + clone.cost + 1
        childright.path = childright.path + clone.path
        childright.path = childright.path + ['right']
        fringe.put(deepcopy(childright))
    if max_fringe_size < fringe.qsize():
        max_fringe_size = fringe.qsize()
    board = fringe.get()
    print(board.parent)
    if max_ram_usage < resource.getrusage(resource.RUSAGE_SELF).ru_maxrss:
        max_ram_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

elapsed = timeit.default_timer() - start_time

print 'path_to_goal = ',board.path

for i in range(5):
    temp = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# In[ ]:

print "cost_of_path = ",board.cost



# In[ ]:

print "nodes_expanded = ",len(explored)

print "fringe_size = ",fringe.qsize()

print "max_fringe_size = ",max_fringe_size

print "running_time = ",elapsed

print "max_ram_usage = ",max_ram_usage/1000
# In[ ]:
print(temp)
