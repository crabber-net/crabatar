import gizeh
import math


def draw_solid(size, palette):
    color = palette.root.rgb()
    surface = gizeh.Surface(width=size, height=size)
    gizeh.rectangle(lx=size, ly=size, xy=(size // 2, size // 2),
                    fill=color) \
            .draw(surface)
    return surface


def draw_overlapping_circles(size, palette, count=4):
    colors = palette.monochromatic(2)
    surface = gizeh.Surface(width=size, height=size)
    for v_idx in range(count):
        for idx in range(count):
            color = colors[(idx + v_idx) % len(colors)]
            x_pos = idx * (size // (count - 1))
            y_pos = v_idx * (size // (count - 1))
            color_circle = gizeh.circle(
                r=size // count,
                xy=(x_pos, y_pos),
                fill=color
            )
            color_circle.draw(surface)
    return surface


def draw_recessed_circles(size, palette, count=5):
    colors = palette.monochromatic(count)
    colors.reverse()
    surface = gizeh.Surface(width=size, height=size)
    for idx in range(count):
        color = colors[idx % len(colors)]
        color_circle = gizeh.circle(
            r=size - ((size / count) * idx),
            xy=(size // 2, size // 2),
            fill=color
        )
        color_circle.draw(surface)
    return surface


def draw_recessed_triangles(size, palette, count=4):
    colors = palette.monochromatic(count)
    colors.reverse()
    surface = gizeh.Surface(width=size, height=size)
    radius = int(size * 1.5)
    for idx in range(count):
        color = colors[idx % len(colors)]
        color_triangle = gizeh.regular_polygon(
            r=radius - ((radius / count) * idx),
            n=3,
            angle=math.pi * 1.5,
            xy=(size // 2, size // 2 + (math.pi * size) / 10),
            fill=color
        )
        color_triangle.draw(surface)
    return surface


def draw_angled_lines(size, palette, count=5):
    colors = palette.monochromatic(2)
    surface = gizeh.Surface(width=size, height=size)
    for idx in range(count + 2):
        idx = idx - 1
        color = colors[idx % len(colors)]
        color_rect = gizeh.rectangle(
            lx=size * 2,
            ly=size / (count - 1) + 2,
            xy=(size / 2, (size / (count - 1)) * idx),
            fill=color
        ).rotate(45, center=(size // 2, size // 2))
        color_rect.draw(surface)
    return surface


def draw_horizontal_lines(size, palette, count=7):
    colors = palette.monochromatic(2)
    surface = gizeh.Surface(width=size, height=size)
    for idx in range(count):
        color = colors[idx % len(colors)]
        color_rect = gizeh.rectangle(
            lx=size,
            ly=size / count + 1,
            xy=(size / 2, (size / count) * idx + (size / (count * 2))),
            fill=color
        )
        color_rect.draw(surface)
    return surface



def draw_vertical_lines(size, palette, count=7):
    colors = palette.monochromatic(2)
    surface = gizeh.Surface(width=size, height=size)
    for idx in range(count):
        color = colors[idx % len(colors)]
        color_rect = gizeh.rectangle(
            lx=size / count + 1,
            ly=size,
            xy=((size / count) * idx + (size / (count * 2)), size / 2),
            fill=color
        )
        color_rect.draw(surface)
    return surface


def draw_wavy_lines(size, palette, count=7, frequency=6):
    colors = palette.monochromatic(2)
    surface = gizeh.Surface(width=size, height=size)

    # Jacob's sin()
    jin = lambda i, n: (((i // n) * (n - 1)) - ((i % n) * (-1 + (i // n) * 2)))

    for idx in range(count + 1):
        color = colors[idx % len(colors)]
        points = [
            (
                # Px
                ((
                    ((p + p // (frequency + 2)) % 2) / 2 \
                    + idx + (p // (frequency + 2))
                ) - 1) * (size / (count - 1)) \
                + (-1 + (p // (frequency + 2)) * 2),
                # Py
                (jin(p, frequency + 2) - 1) * (size / (frequency - 1))
            )
            for p in range((frequency + 2) * 2)
        ]
        line = gizeh.polyline(points=points, fill=color)
        line.draw(surface)
    return surface
