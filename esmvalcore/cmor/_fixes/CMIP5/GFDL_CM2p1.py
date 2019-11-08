<<<<<<< HEAD:esmvalcore/cmor/_fixes/CMIP5/GFDL_CM2p1.py
# pylint: disable=invalid-name, no-self-use, too-few-public-methods
=======
>>>>>>> origin/development:esmvalcore/cmor/_fixes/cmip5/gfdl_cm2p1.py
"""Fixes for GFDL CM2p1 model."""
from copy import deepcopy

from ..fix import Fix
from ..CMIP5.GFDL_ESM2G import allvars as base_allvars


class allvars(base_allvars):
    """Fixes for all variables."""


<<<<<<< HEAD:esmvalcore/cmor/_fixes/CMIP5/GFDL_CM2p1.py
class sftof(Fix):
=======
class Areacello(Fix):
    """Fixes for areacello"""

    def fix_metadata(self, cubes):
        """
        Fix metadata.

        Fixes wrong units.

        Parameters
        ----------
        cube: iris.cube.Cube

        Returns
        -------
        iris.cube.Cube

        """
        cube = self.get_cube_from_list(cubes)
        cube.units = 'm2'
        return cubes


class Sftof(Fix):
>>>>>>> origin/development:esmvalcore/cmor/_fixes/cmip5/gfdl_cm2p1.py
    """Fixes for sftof."""

    def fix_data(self, cube):
        """
        Fix data.

        Fixes discrepancy between declared units and real units

        Parameters
        ----------
        cube: iris.cube.Cube

        Returns
        -------
        iris.cube.Cube

        """
        metadata = cube.metadata
        cube *= 100
        cube.metadata = metadata
        return cube


class Tos(Fix):
    """Fixes for tos"""

    def fix_data(self, cube):
        """
        Fix data.

        Fixes discrepancy between declared units and real units

        Parameters
        ----------
        cube: iris.cube.Cube

        Returns
        -------
        iris.cube.Cube

        """
        metadata = deepcopy(cube.metadata)
        cube += 273.15
        cube.metadata = metadata
        return cube

    def fix_metadata(self, cubes):
        """
        Fix metadata.

        Fixes wrong standard_name.

        Parameters
        ----------
        cube: iris.cube.Cube

        Returns
        -------
        iris.cube.Cube

        """
        cube = self.get_cube_from_list(cubes)
        cube.standard_name = 'sea_surface_temperature'
        return cubes
