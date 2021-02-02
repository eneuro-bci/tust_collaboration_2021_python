"""
Activity 3
--------------------------
sample_experiment/__init__

This file contains the sample_experiment package initialization file. It organizes and exposes the relevant function and
class imports.

--
Collaboration between Tianjin University of Science and Technology (TUST) and the Brain-Computer Interface (BCI)
department of the Tianjin International Joint Academy of Biomedicine (TJAB).

Tianjin, China, February 2021.
"""

# Note: An __init__ file is used to perform a wide range of checks and actions but at the very list, it organizes the
# exposed imports from the package

from .settings import Settings
from .main_window import MainWindow

__all__ = (
    'Settings',
    'MainWindow',
)

# Note: This is usually when we check for package dependencies but will be added at a later point
