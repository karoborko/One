import numpy as np

                     # 1   2    3    4    5    6    7    8
Profile = np.array([[0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7],  # A (adenine)
                    [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2],  # C (cytosine)
                    [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1],  # G (guanine)
                    [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0]]) # T (thymine)
# Profile matrix   determines the probability of a given base in the i-th position in the motif

def distribuanta(p, i):
    """dystrybuanta - funkcja zbierajaca prawdopodobienstwa i zwracajaca zasade azotowa, ktorej
    prawdopodobienstwo p odpowiada prawdopodienstwu wystapienia danej zasady na i-tym miejscu w motywie"""
    assert p >= 0, "the probability can never be less than 0"
    assert p <= 1, "the probability can never be greater than 1"
    assert i >= 0, "the columns in the Profile matrix are indexed from 0"
    assert i <= 7, "the columns in the Profile matrix are indexed up to 7"
    t = lambda x, y : x + y
    t1 = t(0.0, Profile[0][i])
    t2 = t(t1, Profile[1][i])
    t3 = t(t2, Profile[2][i])
    t4 = t(t3, Profile[3][i])
    assert t4 > 0.99999999999 and t4 < 1.00000000001, "the sum of the probabilities equal 1"
    # due to adding 0.1 (float) t4 is never equal 1, but rather e.g. 0.99999... or 1.0000001...


    if p >= 0 and p <= t1:
        return "A" # probabilities from 0 to t1 correspond to the occurrence of A
    elif p > t1 and p <= t2:
        return "C" # probabilities from t1 to t2 correspond to the occurrence of C
    elif p > t2 and p <= t3:
        return "G" # probabilities from t2 to t3 correspond the occurrence of G
    elif p > t3 and p <= t4:
        return "T" # probabilities from t3 to t4 = 1 correspond the occurrence of T

if __name__ == '__main__':
    print("Tests of the function: ")
    test_motif = ""
    for i in range(8):
        test_motif += distribuanta(0.7, i)
    assert test_motif == "GCCGGCTA", "Error of distribuanta function"

    test_motif2 = ""
    for i in range(8):
        test_motif2 += distribuanta(0.99999999999, i)
    assert test_motif2 == "TGTTTTTG", "Error of distribuanta function"


    test_motif3 = ""
    for i in range(8):
        test_motif3 += distribuanta(0.0, i)
    assert test_motif3 == "AAAAAAAA", "Error of distribuanta function"