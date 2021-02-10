"""
Activity 3
-----------------------------
sample_experiment/main_window

This file contains implementation of the Window class. The Window always reference to the class responsible
for everything that is on-screen.

--
Collaboration between Tianjin University of Science and Technology (TUST) and the Brain-Computer Interface (BCI)
department of the Tianjin International Joint Academy of Biomedicine (TJAB).

Tianjin, China, February 2021.
"""

# Local imports
import random
import time                         # The first group is always for Python's built-in packages

import pygame                       # Second group is for external packages (numpy, pygame, etc)
import randomword

from .settings import Settings      # Third group is user-written code imports


class MainWindow:
    """
    This class handles the update and rendering of all the elements on the screen. The experiment program
    for the activity 3 is executed through an instance of this class. The class calls helper functions from
    other modules for processing.
    """

    def __init__(self):
        """
        Define class attributes
        """

        # General attributes
        self.screen = None
        self.is_initialized = False
        self.is_running = False
        self.event_one_second = None  # Pygame's event object, will be triggered every 1 sec

        # Timing
        self.start_time = 0
        self.elapsed_time = 0
        self.timestamp = 0
        self.time_word_refresh = Settings.TIME_WORD_REFRESH  # Time in seconds on which the word should refresh

        # FPS
        self.target_fps = 0
        self.clock = None
        self.fps = 0
        self.fps_count = 0

        # Colors
        self.color_text_status = None  # Tuple used to represent the RGB Color used the status text
        self.color_text_word = None  # Tuple used to represent the RGB Color of the Word
        self.color_background = None  # Tuple for the RGB values of the background color

        # Font objects
        self.font_elapsed_time = None
        self.font_fps = None
        self.font_word = None
        self.font_change = None

        # Texts (the string displayed on the screen) using the Font objects, values below are dummy
        self.text_elapsed_time = "Elapsed Time"
        self.text_fps = "FPS"
        self.text_word = "WORD"

        # Positions (for the on-screen texts)
        self.position_elapsed_time = None
        self.position_fps = None
        self.position_word = None
        self.position_change = None
        self.word_x = None
        self.word_y = None

    def initialize(self):
        """
        This method should be called before 'run'
        Note how initialization is made using the values stored in the Settings class
        :return:
        """

        # Start Pygame and screen
        pygame.init()
        self.screen = pygame.display.set_mode(Settings.WINDOW_SIZE)
        pygame.display.set_caption(Settings.WINDOW_TITLE)

        # Set font objects
        self.font_elapsed_time = pygame.font.SysFont(Settings.TEXT_FONT_STATUS, Settings.TEXT_SIZE_STATUS)
        self.font_fps = pygame.font.SysFont(Settings.TEXT_FONT_STATUS, Settings.TEXT_SIZE_STATUS)
        self.font_word = pygame.font.SysFont(Settings.TEXT_FONT_WORD, Settings.TEXT_SIZE_WORD)
        self.font_change = pygame.font.SysFont("arial", Settings.CHANGE_WORD)

        # Set a fixed Pygame event that is triggered every second (for the text status updates)
        self.clock = pygame.time.Clock()
        self.event_one_second = pygame.USEREVENT + 1
        pygame.time.set_timer(self.event_one_second, 1000)
        self.target_fps = Settings.TARGET_FPS

        # Set default colors
        self.color_text_status = (255, 255, 255)
        self.color_text_word = (255, 255, 255)
        self.color_background = (0, 0, 0)

        # Set positions
        self.position_elapsed_time = Settings.TEXT_ELAPSED_TIME_POSITION
        self.position_fps = Settings.TEXT_FPS_POSITION
        self.position_word = Settings.TEXT_WORD_POSITION
        self.word_x = Settings.word_x
        self.word_y = Settings.word_y
        self.position_change = (Settings.word_x, Settings.word_y)

        # Set user-defined flags and time references
        self.is_initialized = True
        self.is_running = False
        self.start_time = time.perf_counter()   # Used to compute the elapsed time
        self.elapsed_time = 0
        self.timestamp = 0

    def run(self):
        """
        This run executes the main loop. The main loop calls other methods from this class as well as
        helper functions from the helper_functions module.
        :return:
        """

        if not self.is_initialized:
            self.initialize()

        self.is_running = True
        self.timestamp = time.perf_counter()

        while self.is_running:
            """
            This is the main loop. Code in this section is run every frame.
            """

            # Set frame background
            self.screen.fill(self.color_background)

            # Check for input and user-defined events
            self._check_for_events()

            # Check for completion of the time required to update the word
            if time.perf_counter() - self.timestamp >= self.time_word_refresh:
                self._perform_word_refresh_event()

            # At the end of each frame, update all textures and re-draw the screen
            self._update_on_screen_text(self.font_elapsed_time, self.text_elapsed_time, self.color_text_status,
                                        self.position_elapsed_time)

            self._update_on_screen_text(self.font_fps, self.text_fps, self.color_text_status,
                                        self.position_fps)

            self._update_on_screen_text(self.font_change, self.text_word, self.color_text_word,
                                        self.position_change)

            self.clock.tick(self.target_fps)
            pygame.display.flip()
            self.fps_count += 1

    def _check_for_events(self):
        """
        Use this method to perform all operations related to input events. Note that this method is private
        :return:
        """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.is_running = False

            if event.type == self.event_one_second:

                # Update the elapsed time and FPS count
                self.elapsed_time = time.perf_counter() - self.start_time
                elapsed_time_str = "{:.1f}".format(self.elapsed_time)
                self.text_elapsed_time = f'Elapsed time: {elapsed_time_str} secs.'

                self.fps = self.fps_count
                self.text_fps = f'FPS: {self.fps}'
                self.fps_count = 0

            if event.type == pygame.KEYDOWN:
                print(event.key)
                # Move up
                if event.key == 1073741920:
                    if Settings.word_y <= 0:
                        Settings.word_y = Settings.word_y
                    elif Settings.word_y > 0:
                        Settings.word_y - 10
                # Move down
                elif event.key == 1073741914:
                    if Settings.word_y >= Settings.WINDOW_SIZE[1]:
                        Settings.word_y = Settings.WINDOW_SIZE[1]
                    elif Settings.word_y < Settings.WINDOW_SIZE[1]:
                        Settings.word_y = Settings.word_y + 10
                # Move left
                elif event.key == 1073741916:
                    if Settings.word_x <= 0:
                        Settings.word_x = Settings.word_x
                    elif Settings.word_x > 0:
                        Settings.word_x = Settings.word_x - 10
                # Move right
                elif event.key == 1073741918:
                    if Settings.word_x < Settings.WINDOW_SIZE[0]:
                        Settings.word_x = Settings.word_x + 10
                    elif Settings.word_x >= Settings.WINDOW_SIZE[0]:
                        Settings.word_x = Settings.word_x
                # Back to the center
                elif event.key == 1073741917:
                    Settings.word_y = Settings.WINDOW_SIZE[1] / 2
                    Settings.word_x = Settings.WINDOW_SIZE[0] / 2
                # Random in one place
                elif event.key == 1073741922:
                    Settings.word_y = random.randint(50, 600)
                    Settings.word_x = random.randint(50, 600)
                # 第二个需求：使用上下方向键调整字的大小
                elif event.key == 1073741906:
                    # 将字体放大
                    Settings.CHANGE_WORD = Settings.CHANGE_WORD + 10
                elif event.key == 1073741905:
                    # 将字体缩小
                    Settings.CHANGE_WORD = Settings.CHANGE_WORD - 10
                self.font_change = pygame.font.SysFont("arial", Settings.CHANGE_WORD)

    def _perform_word_refresh_event(self):
        """
        This method is designed to conduct all operations that must be carried out every time that the
        word's refresh time is completed. Getting a new word and other actions will be performed here.
        :return:
        """

        # Get a new word
        self.text_word = randomword.get_random_word()

        # Update the reference timestamp
        self.timestamp = time.perf_counter()

    def _update_on_screen_text(self, font_object, text, color, position):
        """
        This method will create/update a new text texture using the information from the inputs
        :return:
        """

        texture = font_object.render(text, True, color)
        self.screen.blit(texture, position)
