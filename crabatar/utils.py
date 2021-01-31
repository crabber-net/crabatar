import gizeh
import math


def draw_solid(size, color):
    surface = gizeh.Surface(width=size, height=size)
    gizeh.rectangle(lx=size, ly=size, xy=(size // 2, size // 2),
                    fill=color.rgb()) \
            .draw(surface)
    return surface


def draw_overlapping_circles(size, palette, count=5):
    colors = palette.triad()
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
    colors = palette.analogous(4, 90)
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


def draw_recessed_triangles(size, palette, count=5):
    colors = palette.analogous(5, 90)
    surface = gizeh.Surface(width=size, height=size)
    radius = int(size * 1.4)
    for idx in range(count):
        color = colors[idx % len(colors)]
        color_triangle = gizeh.regular_polygon(
            r=radius - ((radius / count) * idx),
            n=3,
            angle=math.pi * 1.5,
            xy=(size // 2, size // 2),
            fill=color
        )
        color_triangle.draw(surface)
    return surface


def draw_spinning_triangles(size, palette, count=6):
    colors = palette.analogous(5, 90)
    surface = gizeh.Surface(width=size, height=size)
    gizeh.rectangle(lx=size, ly=size, xy=(size // 2, size // 2),
                    fill=colors[count % len(colors)]) \
            .draw(surface)
    for idx in range(count):
        color = colors[idx % len(colors)]
        color_triangle = gizeh.regular_polygon(
            r=size - ((size / count) * idx),
            n=3,
            angle=(math.pi / count / 3) * idx,
            xy=(size // 2, size // 2),
            fill=color
        )
        color_triangle.draw(surface)
    return surface


def draw_angled_lines(size, palette, count=5):
    colors = palette.analogous(count, 90)
    surface = gizeh.Surface(width=size, height=size)
    for idx in range(count):
        color = colors[idx % len(colors)]
        color_rect = gizeh.rectangle(
            lx=size * 2,
            ly=size / count + 1,
            xy=(size / 2, (size / count) * idx + (size / (count * 2))),
            fill=color
        ).rotate(45, center=(size // 2, size // 2))
        color_rect.draw(surface)
    return surface


def draw_horizontal_lines(size, palette, count=5):
    colors = palette.analogous(5, 60)
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



def draw_vertical_lines(size, palette, count=5):
    colors = palette.analogous(5, 60)
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
