# pylint: disable=invalid-name, no-self-use, too-few-public-methods
"""Fixes for HadGEM2_ES."""
import numpy as np

from ..fix import Fix


class allvars(Fix):
    """Fixes common to all vars."""

    def fix_metadata(self, cubes):
        """
        Fixes latitude.

        Parameters
        ----------
        cube: iris.cube.CubeList

        Returns
        -------
        iris.cube.CubeList

        """
        for cube in cubes:
            lats = cube.coords('latitude')
            if lats:
                lat = cube.coord('latitude')
                lat.points = np.clip(lat.points, -90., 90.)
                lat.bounds = np.clip(lat.bounds, -90., 90.)

        return cubes


class o2(Fix):
    """Fixes for o2."""

    def fix_metadata(self, cubes):
        """
<<<<<<< HEAD:esmvalcore/cmor/_fixes/CMIP5/HadGEM2_ES.py
        Apply fixes to the files prior to creating the cube.

        Should be used only to fix errors that prevent loading or can
        not be fixed in the cube (i.e. those related with missing_value
        and _FillValue or missing standard_name).
        Parameters
        ----------
        filepath: basestring
            file to fix.
        output_dir: basestring
            path to the folder to store the fix files, if required.
=======
        Fix standard and long name.

        Parameters
        ----------
        cube: iris.cube.CubeList

>>>>>>> origin/development:esmvalcore/cmor/_fixes/cmip5/hadgem2_es.py
        Returns
        -------
        iris.cube.CubeList

        """
        std = 'mole_concentration_of_dissolved_molecular_oxygen_in_sea_water'
        long_name = 'Dissolved Oxygen Concentration'

        cubes[0].long_name = long_name
        cubes[0].standard_name = std
        return cubes
