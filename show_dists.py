from importlib.metadata import distribution, distributions, packages_distributions
from pprint import pprint

dists = []
for dist in distributions():
    pprint(dist.name)
    if dist.name == "foo":
        dists.append(dist)

for dist in dists:
    pprint(dist.files)


pprint(packages_distributions())
