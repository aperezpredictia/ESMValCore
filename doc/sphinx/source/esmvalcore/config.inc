.. _config:

*******************
Configuration files
*******************

Overview
========

There are several configuration files in ESMValTool:

* ``config-user.yml``: sets a number of user-specific options like desired
  graphical output format, root paths to data etc. 
* ``config-developer.yml``: sets a number of standardized file-naming and paths to data
  formatting;
* ``config-references.yml``: stores information on diagnostic authors and scientific
  journals references;
* ``config-logging.yml``: stores information on logging (duh!).

User configuration file
=======================

The ``config-user.yml`` is one of the two files the user needs to provide to the
``esmvaltool`` executable at run time, the second being ``recipe.yml`` (named accordingly
as per the specific diagnostic/recipe used).

The ``config-user.yml`` configuration file contains all the global level
information needed by ESMValTool. ``config-user.yml`` can be reused as many times the
user needs to before changing any of the options stored in it. This file is essentially
the gateway between the user and the machine-specific instructions to ``esmvaltool``.
The following shows the default settings from the ``config-user.yml`` file with explanations
in a commented line above each option:

.. code-block:: yaml

  # Diagnostics create plots? [true]/false
  # turning it off will turn off graphical output from diagnostic
  write_plots: true

  # Diagnositcs write NetCDF files? [true]/false
  # turning it off will turn off netCDF output from diagnostic
  write_netcdf: true

  # Set the console log level debug, [info], warning, error
  # for much more information printed to screen set log_level: debug
  log_level: info
  # verbosity is deprecated and will be removed in the future
  # verbosity: 1

  # Exit on warning? true/[false]
  exit_on_warning: false

  # Plot file format? [ps]/pdf/png/eps/epsi
  output_file_type: pdf

  # Destination directory where all output will be written
  # including log files and performance stats
  output_dir: ./esmvaltool_output

  # Auxiliary data directory (used for some additional datasets)
  # this is where e.g. files can be downloaded to by a download
  # script embedded in the diagnostic
  auxiliary_data_dir: ./auxiliary_data

  # Use netCDF compression true/[false]
  compress_netcdf: false

  # Save intermediary cubes in the preprocessor true/[false]
  # set to true will save the output cube from each preprocessing step
  # these files are numbered according to the preprocessing order
  save_intermediary_cubes: false

  # Remove the preproc dir if all fine
  # this option true will remove ALL preprocessor files
  # CAUTION when using: if you need those files, set it to false
  remove_preproc_dir: true

  # Run at most this many tasks in parallel null/[1]/2/3/4/..
  # Set to null to use the number of available CPUs.
  # Make sure your system has enough memory for the specified number of tasks.
  max_parallel_tasks: 1

  # Path to custom config-developer file, to customise project configurations.
  # See config-developer.yml for an example. Set to None to use the default
  config_developer_file: null

  # Get profiling information for diagnostics
  # Only available for Python diagnostics
  profile_diagnostic: false

  # Rootpaths to the data from different projects (lists are also possible)
  rootpath:
    CMIP5: [~/cmip5_inputpath1, ~/cmip5_inputpath2]
    OBS: ~/obs_inputpath
    default: ~/default_inputpath

  # Directory structure for input data: [default]/BADC/DKRZ/ETHZ/etc
  # See config-developer.yml for definitions.
  drs:
    CMIP5: default

Most of these settings are fairly self-explanatory, ie:

.. code-block:: yaml

  # Diagnostics create plots? [true]/false
  write_plots: true
  # Diagnositcs write NetCDF files? [true]/false
  write_netcdf: true

The ``write_plots`` setting is used to inform ESMValTool about your preference
for saving figures. Similarly, the ``write_netcdf`` setting is a boolean which
turns on or off the writing of netCDF files.

.. code-block:: yaml

  # Auxiliary data directory (used for some additional datasets)
  auxiliary_data_dir: ~/auxiliary_data

The ``auxiliary_data_dir`` setting is the path to place any required
additional auxiliary data files. This method was necessary because certain
Python toolkits such as cartopy will attempt to download data files at run
time, typically geographic data files such as coastlines or land surface maps.
This can fail if the machine does not have access to the wider internet. This
location allows us to tell cartopy (and other similar tools) where to find the
files if they can not be downloaded at runtime. To reiterate, this setting is
not for model or observational datasets, rather it is for data files used in
plotting such as coastline descriptions and so on.

.. note::

   **Pro Tip: working with multiple config-user files.**

   You choose your config.yml file at run time, so you could have several
   available with different purposes. One for formalised run, one for debugging, etc.

.. note::

   **Note on data finding sections of the config-user file.**

   A detailed explanation of the data finding-related sections of the ``config-user.yml``
   (``rootpath`` and ``drs``) is presented in config-user-rootpath_ and config-user-drs_
   in the Data Finder section; these sections relate directly to the data finding capabilities
   of ESMValTool and are very important to be understood by the user.

.. _config-developer:

Developer configuration file
============================

This configuration file describes the file system structure for several
key projects (CMIP5, CMIP6) on several key machines (BADC, CP4CDS, DKRZ, ETHZ,
SMHI, BSC) - CMIP data is stored as part of the Earth System Grid Federation (ESGF)
and the standards for file naming and paths to files are set out by CMOR and DRS.
For a detailed description of these standards and how the impact on the use in ESMValTool
we refer the user to CMOR-DRS_ section where we relate these standards to the data retrieval
mechanism built-in ESMValTool.

The data directory structure of the CMIP5/6 projects is set up differently
at each site. The following code snippet is an example of several paths
descriptions for the CMIP5 at various sites:

.. code-block:: yaml

  CMIP5:
    input_dir:
      default: '/'
      BADC: '[institute]/[dataset]/[exp]/[frequency]/[modeling_realm]/[mip]/[ensemble]/latest/[short_name]'
      CP4CDS: '[institute]/[dataset]/[exp]/[frequency]/[modeling_realm]/[mip]/[ensemble]/[short_name]/latest/'
      DKRZ: '[institute]/[dataset]/[exp]/[frequency]/[modeling_realm]/[mip]/[ensemble]/[latestversion]/[short_name]'
      ETHZ: '[exp]/[mip]/[short_name]/[dataset]/[ensemble]/'
      SMHI: '[dataset]/[ensemble]/[exp]/[frequency]'
      BSC: '[project]/[exp]/[dataset.lower]'

As an example, the CMIP5 file path on BADC would be:

.. code-block:: yaml

        [institute]/[dataset ]/[exp]/[frequency]/[modeling_realm]/[mip]/[ensemble]/latest/[short_name]

When loading these files, ESMValTool replaces the placeholders ``[item]`` with actual
values supplied for by the information form ``config-user.yml`` and ``recipe.yml``.
The resulting real path would look something like this:

.. code-block:: bash

    MOHC/HadGEM2-CC/rcp85/mon/ocean/Omon/r1i1p1/latest/tos

Again, for a more in-depth description this process, as part of the data retrieval mechanism,
please see CMOR-DRS_.

.. _config-ref:

References configuration file
=============================

The ``config-references.yml`` file is the full list of ESMValTool authors,
references and projects. Each author, project and reference in the documentation
section of a recipe needs to be in this file in the relevant section.

For instance, the recipe ``recipe_ocean_example.yml`` file contains the following
documentation section:

.. code-block:: yaml

  documentation
    authors:
      - demo_le

    maintainer:
      - demo_le

    references:
      - demora2018gmd

    projects:
      - ukesm


All four items here are named people, references and projects listed in the
``config-references.yml`` file.

Logging configuration file
==========================

.. warning::
    Section to be added