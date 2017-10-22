"""Set up and run a radiance analysis from a json file."""
import os
import json

from honeybee.radiance.recipe.solaraccess.gridbased import SolarAccessGridBased
from honeybee.radiance.recipe.pointintime.gridbased import GridBased
from honeybee.futil import bat_to_sh


def run_from_json(recipe, folder, name):
    """Create a python recipe from json object and run the analysis."""
    if recipe["id"] == 0:
        rec = SolarAccessGridBased.fromJson(recipe)
    elif recipe["id"] == 1:
        rec = GridBased.fromJson(recipe)
    else:
        raise ValueError(
            "Invalid id input {}. "
            "Currently only the id of [0] SolarAccess and [1] pointintime are supported!"
            .format(recipe['id'])
        )

    # generate bat file
    bat = rec.write(folder, name)
    # Convert bat to sh
    sh = bat_to_sh(bat)

    # start to run the subprocess
    if os.name == 'nt':
        success = rec.run(bat)
    else:
        success = rec.run(sh)

    # run post-processing code
    if success:
        return True
    else:
        return False


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    import honeybee
    honeybee.config.radbinPath = '/usr/local/radiance/bin'
    honeybee.config.radlibPath = '/usr/local/radiance/lib'
    fp = r"resources/dyn_analysis_recipe.json"
    full_path = os.path.join(os.path.dirname(__file__), fp)
    with open(full_path, 'rb') as inf:
        recipe = json.load(inf)
    # os.chdir(os.path.dirname(__file__))
    success = run_from_json(recipe, 'test', 'hackathon_dynamo')
    print(success)
