import random as r

def planetNameGenerator(seed):
    r.seed(seed)
    catalogue = ["Kepler ", "CoRoT-", "HD ", "HAT-P-", "K2-", "2MASS ", "EPIC ", "GJ ", "HATS-", "KOI-", "MASCARA-",
                 "OGLE-", "TrES-", "WASP-"]

    planet_name = r.choice(catalogue)+str(r.randint(1,2500))
    return planet_name