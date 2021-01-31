from . import utils
import colorsys
import gizeh
import hashlib
from PIL import Image
import random
from typing import Tuple


class Color:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        self.red: int = red
        self.green: int = green
        self.blue: int = blue

    def hsv(self) -> Tuple[float]:
        return colorsys.rgb_to_hsv(*self.rgb())

    def rgb(self) -> Tuple[float]:
        return tuple(
            (channel / 255 for channel in (self.red, self.green, self.blue))
        )

    def rgb255(self) -> Tuple[float]:
        return (self.red, self.green, self.blue)

    def rotate_hue(self, degrees: int) -> 'Color':
        hue, saturation, value = self.hsv()
        hue = (((hue * 360) + degrees) % 360) / 360
        return Color.from_hsv(hue, saturation, value)

    @classmethod
    def from_hsv(cls, hue: float, saturation: float, value: float) -> 'Color':
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        return cls.from_rgb(*rgb)

    @classmethod
    def from_rgb(cls, red: float, green: float, blue: float) -> 'Color':
        rgb_255 = [int(channel * 255) for channel in (red, green, blue)]
        return cls(*rgb_255)


class Crabatar:
    patterns = [utils.draw_angled_lines, utils.draw_horizontal_lines,
                utils.draw_vertical_lines, utils.draw_overlapping_circles,
                utils.draw_recessed_circles, utils.draw_recessed_triangles,
                utils.draw_spinning_triangles]
    crab_img = Image.open('crab.png')

    def __init__(self, username: str):
        self.username: str = username
        self.hash: str = hashlib.sha256(self.username.encode())
        self.random = random.Random()
        self.reseed()

    def __repr__ (self):
        return f'<Crabatar {self.username!r}>'

    def reseed(self):
        self.random.seed(self.hash.digest()[-20:])

    def write_to_png(self, filename: str, size=512, inverted=False):
        self.reseed()

        res = 10000000
        hue = self.random.randrange(res) / res
        saturation = self.random.randrange(0.4 * res, 0.6 * res) / res
        palette = Palette(Color.from_hsv(hue, saturation, 1))
        pattern_func = self.random.choice(Crabatar.patterns)
        pattern = pattern_func(size, palette)
        pattern = Image.fromarray(pattern.get_npimage())
        if inverted:
            pattern.paste(Crabatar.crab_img, (0, 0), Crabatar.crab_img)
            pattern.save(filename, 'PNG')
        else:
            white_background = gizeh.Surface(width=size, height=size, bg_color=(1, 1, 1))
            white_background = Image.fromarray(white_background.get_npimage())
            white_background.paste(pattern, (0, 0), Crabatar.crab_img)
            white_background.save(filename, 'PNG')

class Palette:
    def __init__(self, root: 'Color'):
        self.root: 'Color' = root

    def complimentary(self):
        return [
            self.root.rgb(),
            self.root.rotate_hue(180).rgb()
        ]

    def regular(self, count: int):
        colors = list()
        for i in range(count):
            colors.append(self.root.rotate_hue((360 // count) * i).rgb())
        return colors

    def analogous(self, count: int, split_degrees: int):
        colors = list()
        for i in range(count):
            colors.append(self.root.rotate_hue(
                (split_degrees // count) * i - (split_degrees // 2)
            ).rgb())
        return colors

    def split_complimentary(self, split_degrees: int = 30):
        return [
            self.root.rgb(),
            self.root.rotate_hue(180 - split_degrees // 2).rgb(),
            self.root.rotate_hue(180 + split_degrees // 2).rgb()
        ]

    def tetradic(self, split_degrees: int = 60):
        return [
            self.root.rgb(),
            self.root.rotate_hue(split_degrees).rgb(),
            self.root.rotate_hue(180).rgb(),
            self.root.rotate_hue(split_degrees + 180).rgb()
        ]

    def triad(self):
        return self.regular(3)

    @classmethod
    def from_hash(cls, hash: hashlib._hashlib.HASH, saturation: float = 0.5,
                  value: float = 1):
        hue = hash.digest()[0] % 256 / 255
        root_color = Color.from_hsv(hue, saturation, value)
        return cls(root=root_color)
