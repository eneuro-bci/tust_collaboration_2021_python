"""
Activity 3
-----------------------------
sample_experiment/color

This file contains a class that computes all the colors that the background and the word can have.

--
Collaboration between Tianjin University of Science and Technology (TUST) and the Brain-Computer Interface (BCI)
department of the Tianjin International Joint Academy of Biomedicine (TJAB).

Tianjin, China, February 2021.
"""


class Color:
    """
    This is put RGB in arrays
    """

    def __init__(self):

        self.change_color = 0
        self.main_color_list = []  # 存储渐变色
        self.number_colors = 0
        self.opposite_color_list = []  # 存储渐变色相反色
        self.size_opposite_list = 0

    def compute_colors(self):

        # 从红到黄
        for g in range(0, 256):
            self.main_color_list.append((255, g, 0))
            self.opposite_color_list.append((0, 255 - g, 255))

        # 从黄到绿
        for r in range(255, -1, -1):
            self.main_color_list.append((r, 255, 0))
            self.opposite_color_list.append((255 - r, 0, 255))

        # 从绿到青
        for b in range(0, 256):
            self.main_color_list.append((0, 255, b))
            self.opposite_color_list.append((255, 0, 255 - b))

        # 从青到蓝
        for g in range(255, -1, -1):
            self.main_color_list.append((0, g, 255))
            self.opposite_color_list.append((255, 255 - g, 0))

        # 从蓝到紫
        for r in range(0, 256):
            self.main_color_list.append((r, 0, 255))
            self.opposite_color_list.append((255 - r, 255, 0))

        # 从紫到红
        for g in range(255, -1, -1):
            self.main_color_list.append((255, 0, g))
            self.opposite_color_list.append((0, 255, 255 - g))

        self.number_colors = len(self.main_color_list)
