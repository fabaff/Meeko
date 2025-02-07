#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Meeko
#

__version__ = "0.5.0"

try:
    import openbabel
except ImportError:
    _has_openbabel = False
else:
    _has_openbabel = True

try:
    import prody
except ImportError:
    _has_prody = False
else:
    _has_prody = True

from .preparation import MoleculePreparation
from .molsetup import RDKitMoleculeSetup
from .utils import rdkitutils
from .utils import pdbutils
from .utils import geomutils
from .utils import utils
from .atomtyper import AtomTyper
from .receptor_pdbqt import PDBQTReceptor
from .molecule_pdbqt import PDBQTMolecule
from .rdkit_mol_create import RDKitMolCreate
from .reactive import reactive_typer
from .reactive import get_reactive_config
from .writer import PDBQTWriterLegacy
from . import analysis

__all__ = ['MoleculePreparation', 'RDKitMoleculeSetup',
        'pdbutils', 'geomutils', 'rdkitutils', 'utils',
        'AtomTyper', 'PDBQTMolecule', 'PDBQTReceptor', 'analysis',
        'RDKitMolCreate',
        'PDBQTWriterLegacy',
        'reactive_typer',
        'get_reactive_config',
        'gridbox',
]

if _has_openbabel:
    from .molsetup import OBMoleculeSetup
    from .utils import obutils
    __all__.append("OBMoleculeSetup")
    __all__.append("obutils")

if _has_prody:
    from .covalentbuilder import CovalentBuilder
    __all__.append("CovalentBuilder")
