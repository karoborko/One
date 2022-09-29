import wspolrzednekartezjanskie as wk
import wspolrzednebiegunowe as wb
import motywy as m
import matplotlib.pyplot as pl
import random as rd

n = 1500
# PART 1 CARTESIAN COORDINATES
points_2D = wk.cartesiancoordinates(n, 2)

pl.figure(figsize = (7,7))
print("""The density distribution for Cartesian coordinates is uniform. Each point has exactly the same probability of 
occurrence in a given place. This is evidenced by diagram 1, 
which for many random points contained in a single circle takes the form of a circle in which the points are distributed 
evenly, i.e. there are no places where points appear less frequently or more frequently. The frequency of their occurrence 
is the same throughout the circle.\n\n""")
for i in range(n):
    if points_2D[i][0] ** 2 + points_2D[i][1] ** 2 <= 1:
        pl.plot(points_2D[i][0], points_2D[i][1], 'r.')
    else:
        pl.plot(points_2D[i][0], points_2D[i][1], 'c.')

# PART 2. POLAR COORDINATES
n_polar_points = wb.polarcoordinates(n)
n_cartesian_points = wb.from_polar_to_cartesian(n_polar_points)
pl.figure(figsize = (7, 7))
print("""The distribution of density for the polar coordinates is not uniform - it means that there are different 
probabilities of the occurrence of points in a given place. This is evidenced by diagram 2, which for many random 
points in a single circle has the form of radiation - in the middle there are more dense areas, while on the outside 
the frequency of the points is small. This is due to the fact that as the length of the beam increases, the length 
of the circle to be filled and which is covered by this beam also increases. Hence the points appear less and less there.\n\n""")
for i in range(n):
    pl.plot(n_cartesian_points[i][0], n_cartesian_points[i][1], 'k.')

# PART 3. MOTIFS
Motifs = []
for k in range(1000): # generates 1000 motifs
    motif = "" # empty motif at the beggining of each iteration k loop 
    for i in range(8):
        p = rd.uniform(0.0, 1.0) # draws the probability (float) in reange 0-1
        motif += m.distribuanta(p, i) # adds dodaje nitrogen base on i-th place in the motif
    Motifs.append(motif) # attaches motif to motif list 
print("Found motifs:")
print(Motifs)