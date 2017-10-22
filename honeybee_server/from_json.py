"""Set up and run a radiance analysis from a json file."""
import os
import json

from . import flask_app
import honeybee
from honeybee.radiance.recipe.solaraccess.gridbased import SolarAccessGridBased
from honeybee.radiance.recipe.pointintime.gridbased import GridBased
from honeybee.futil import bat_to_sh

app_dir = flask_app.config['BASEDIR']
project_dir = os.path.dirname(app_dir)
bin_dir = os.path.join(project_dir, 'radiance')
honeybee.config.radbinPath = os.path.join(bin_dir, 'bin')
honeybee.config.radlibPath = os.path.join(bin_dir, 'lib')


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

    # import pdb; pdb.set_trace()
    # start to run the subprocess
    if os.name == 'nt':
        success = rec.run(bat)
    else:
        success = rec.run(sh)

    # run post-processing code
    if success:
        return True, rec.results()
    else:
        return False, ()
