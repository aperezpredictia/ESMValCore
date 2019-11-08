<<<<<<< HEAD:esmvalcore/cmor/_fixes/CMIP5/CESM1_BGC.py
# pylint: disable=invalid-name, no-self-use, too-few-public-methods
=======
>>>>>>> origin/development:esmvalcore/cmor/_fixes/cmip5/cesm1_bgc.py
"""Fixes for CESM1-BGC model."""

from dask import array as da

from ..fix import Fix


class co2(Fix):
    """Fixes for co2 variable."""

    def fix_data(self, cube):
        """Fix data.

        Fixes discrepancy between declared units and real units

        Parameters
        ----------
        cube: iris.cube.Cube

        Returns
        -------
        iris.cube.Cube

        """
        metadata = cube.metadata
        cube *= 28.966 / 44.0
        cube.metadata = metadata
        return cube


class Gpp(Fix):
    """Fixes for gpp variable."""

    def fix_data(self, cube):
        """Fix data.

        Fix missing values.

        Parameters
        ----------
        cube: iris.cube.Cube

        Returns
        -------
        iris.cube.Cube

        """
        data = da.ma.masked_equal(cube.core_data(), 1.0e33)
        return cube.copy(data)


class Nbp(Gpp):
    """Fixes for nbp variable."""
