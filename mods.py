# OS module to change directory
import os, sys, math, collections, random
import random

os.mkdir("tempdir")
os.chdir("tempdir")

os.getcwd() # shows the directory

os.listdir # sub directories


# sys module: functions and variables used to manipulate python's runtime env.
sys.path
sys.version


math.pi
math.e

player = collections.namedtuple("player", ["name", "age", "team"])
p1 = player("Lambard", 40, "Chelsea")

d1 = collections.OrderedDict()
d1["First"] = 23
d1["Second"] = 30
d1["Third"] = 50
d1["Fourth"] = 99

q = collections.deque([20, 26, 49, 94])
q.appendleft(15)
q.append(66)
q.pop()
q.popleft()

random.randint(1, 100)