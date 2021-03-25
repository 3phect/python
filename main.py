# Akula electronics sim
# Hui Hui Studios - 3phect

# Libraries random and math
import random
from random import randint
from math import pi
from math import sin

# DC input
GroundPowerDC = randint(0, 1)
Battery1 = randint(0, 1)
Battery2 = randint(0, 1)
IFF = 0
PTS25M = 0

# AC input
GroundPowerAC = sin(random.uniform(0, 2 * pi))
GeneratorLeft = sin(random.uniform(0, 2 * pi))
GeneratorRight = sin(random.uniform(0, 2 * pi))

# DC lines

    # VU-6B Left
if GroundPowerDC or GeneratorLeft:
    DCLeftCommon = 1
    DCLeftReserve = 1

    # VU-6B Right
if GroundPowerDC or GeneratorRight:
    DCRightCommon = 1
    DCRightReserve = 1

if Battery1 or Battery2:
    POS500B = 1

# AC lines
if GroundPowerAC or GeneratorLeft:
    ACLeftReserve = 1
    ACLeftCommon = 1

if GroundPowerAC or GeneratorRight:
    ACRightReserve = 1
    ACRightCommon = 1
    BackUpADI = 1

# POS500B
if IFF == 1:
    PTS25M = 0

if PTS25M or IFF:
    BackUpADI = not BackUpADI

# Results
print("DC Left Reserve", DCLeftReserve)
print("DC Right Reserve", DCRightReserve)
print("DC Left Common", DCLeftCommon)
print("DC Right Common", DCRightCommon)
print("Backup ADI", BackUpADI)
print("AC Left Reserve", ACLeftReserve)
print("AC Right Reserve", ACRightReserve)
print("AC Left Common", ACLeftCommon)
print("AC RIght Common", ACRightCommon)