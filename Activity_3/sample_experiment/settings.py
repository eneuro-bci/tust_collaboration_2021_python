"""
Activity 3
--------------------------
sample_experiment/settings

This file contains the implementation of Settings class.

--
Collaboration between Tianjin University of Science and Technology (TUST) and the Brain-Computer Interface (BCI)
department of the Tianjin International Joint Academy of Biomedicine (TJAB).

Tianjin, China, February 2021.
"""


class Settings:
    """
    This is a static class that contains which attributes represent default values and configurable settings for the
    experiment.
    """

    # Note: the attributes are treated as constants and therefore, they use all caps identifiers

    # General
    PYTHON_DEPENDENCIES = ('pygame', 'randomword')    # List all the additional packages required to run this experiment
    TARGET_FPS = 60

    # Size and Position
    WINDOW_TITLE = "Activity 3"
    WINDOW_SIZE = (1280, 720)

    TEXT_SIZE_STATUS = 18
    TEXT_SIZE_WORD = 30
    CHANGE_WORD = 30

    TEXT_FONT_STATUS = "arial"
    TEXT_FONT_WORD = "arial"

    word_x = 600
    word_y = 360
    CHANGE_POSITION = (word_x, word_y)

    TEXT_ELAPSED_TIME_POSITION = (25, 0)
    TEXT_FPS_POSITION = (WINDOW_SIZE[0] - 100, 0)
    TEXT_WORD_POSITION = (word_x, word_y)


    # Time
    TIME_WORD_REFRESH = 1.0   # In seconds
