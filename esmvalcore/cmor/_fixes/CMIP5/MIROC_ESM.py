<<<<<<< HEAD:esmvalcore/cmor/_fixes/CMIP5/MIROC_ESM.py
# pylint: disable=invalid-name, no-self-use, too-few-public-methods
"""Fixes for MIROC ESM model"""
import cf_units
=======
"""Fixes for MIROC ESM model."""

>>>>>>> origin/development:esmvalcore/cmor/_fixes/cmip5/miroc_esm.py
from iris.coords import DimCoord
from iris.exceptions import CoordinateNotFoundError

from ..fix import Fix


class tro3(Fix):
    """Fixes for tro3."""

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
        cube *= 1000
        cube.metadata = metadata
        return cube


class co2(Fix):
    """Fixes for co2"""

    def fix_metadata(self, cubes):
        """
        Fix metadata.

        Fixes error in cube units

        Parameters
        ----------
        cube: iris.cube.CubeList

        Returns
        -------
        iris.cube.Cube

        """
        self.get_cube_from_list(cubes).units = '1.0e-6'
        return cubes


<<<<<<< HEAD:esmvalcore/cmor/_fixes/CMIP5/MIROC_ESM.py
class gpp(Fix):
    """Fixes for gpp"""

    def fix_metadata(self, cubes):
        """
        Fix metadata.

        Fixes error in cube units

        Parameters
        ----------
        cube: iris.cube.CubeList

        Returns
        -------
        iris.cube.CubeList

        """
        # Fixing the metadata, automatic unit conversion should do the trick
        self.get_cube_from_list(cubes).units = cf_units.Unit('g m-2 day-1')
        return cubes


class allvars(Fix):
    """Common fixes to all vars"""
=======
class AllVars(Fix):
    """Common fixes to all vars."""
>>>>>>> origin/development:esmvalcore/cmor/_fixes/cmip5/miroc_esm.py

    def fix_metadata(self, cubes):
        """
        Fix metadata.

        Fixes error in air_pressure coordinate, sometimes called AR5PL35

        Parameters
        ----------
        cube: iris.cube.CubeList

        Returns
        -------
        iris.cube.CubeList

        """
        for cube in cubes:
            try:
                old = cube.coord('AR5PL35')
                dims = cube.coord_dims(old)
                cube.remove_coord(old)

                plev = DimCoord.from_coord(old)
                plev.var_name = plev
                plev.standard_name = 'air_pressure'
                plev.long_name = 'Pressure '
                cube.add_dim_coord(plev, dims)
            except CoordinateNotFoundError:
                pass

        return cubes
