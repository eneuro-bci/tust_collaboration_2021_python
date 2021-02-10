class Color:
    """
    This is put RGB in arrays
    """
    change_color = 0

    color_list = []  # 存储渐变色
    color_list2 = []  # 存储渐变色相反色

    # 从红到黄
    for g in range(0, 256):
        color_list.append((255, g, 0))
        color_list2.append((0, 255 - g, 255))

    # 从黄到绿
    for r in range(255, -1, -1):
        color_list.append((r, 255, 0))
        color_list2.append((255 - r, 0, 255))

    # 从绿到青
    for b in range(0, 256):
        color_list.append((0, 255, b))
        color_list2.append((255, 0, 255 - b))

    # 从青到蓝
    for g in range(255, -1, -1):
        color_list.append((0, g, 255))
        color_list2.append((255, 255 - g, 0))

    # 从蓝到紫
    for r in range(0, 256):
        color_list.append((r, 0, 255))
        color_list2.append((255 - r, 255, 0))

    # 从紫到红
    for g in range(255, -1, -1):
        color_list.append((255, 0, g))
        color_list2.append((0, 255, 255 - g))
