# pylint: disable=invalid-name, no-self-use, too-few-public-methods
"""Fixes for GFDL ESM2M"""

from ..fix import Fix
from ..CMIP5.GFDL_ESM2G import allvars as base_allvars


class allvars(base_allvars):
    """Fixes for all variables"""


<<<<<<< HEAD:esmvalcore/cmor/_fixes/CMIP5/GFDL_ESM2M.py
class sftof(Fix):
    """Fixes for sftof"""
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
    """Fixes for sftof."""
>>>>>>> origin/development:esmvalcore/cmor/_fixes/cmip5/gfdl_esm2m.py

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


class co2(Fix):
    """Fixes for co2"""

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
        cube *= 1e6
        cube.metadata = metadata
        return cube


class Tos(Fix):
    """Fixes for tos."""

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
