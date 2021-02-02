"""
Activity 3
-----------------
launch_experiment

This file contains the entry-point script for the execution of the sample experiment. The experiment
will run according to the settings and behaviour defined on the sample_experiment package.

--
Collaboration between Tianjin University of Science and Technology (TUST) and the Brain-Computer Interface (BCI)
department of the Tianjin International Joint Academy of Biomedicine (TJAB).

Tianjin, China, February 2021.
"""

# Local imports
from sample_experiment import MainWindow

# Execute the experiment

if __name__ == '__main__':

    experiment = MainWindow()
    experiment.initialize()
    experiment.run()

    print("Program completed")
