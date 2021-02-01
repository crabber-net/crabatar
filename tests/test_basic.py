from .context import *
import os


class TestModels:
    def test_color(self):
        red = Color.from_rgb(1, 0, 0)
        green = Color.from_rgb(0, 1, 0)
        blue = Color.from_rgb(0, 0, 1)

        # Test __repr__
        assert red.__repr__() == '<Color (1.00, 0.00, 0.00)>'

        # Test __eq__
        assert Color.from_rgb(0, 0, 0) == Color.from_rgb(0, 0, 0)
        assert Color.from_rgb(0, 0, 0) != 'A string.'

        # Test float -> integer conversion
        assert Color(255, 0, 0) == red
        assert Color(0, 255, 0) == green
        assert Color(0, 0, 255) == blue

        # Test converting RGB -> HSV -> RGB
        assert red.rgb() == Color.from_hsv(*red.hsv()).rgb()

        # Test rotating hues
        assert red.rotate_hue(120) == green
        assert red.rotate_hue(240) == blue
        assert red.rotate_hue(360) == red

    def test_crabatar(self):
        jake = Crabatar('jake')

        # Test __repr__
        assert jake.__repr__() == '<Crabatar \'jake\'>'

        # Test generate_pattern
        pattern = jake.generate_pattern(512)
        assert pattern.width == pattern.height == 512

        # Test write_avatar
        filename = 'jake.png'
        for inverted in (True, False):
            if os.path.exists(filename):
                # Ensure no conflicting files
                os.remove(filename)
            jake.write_avatar(filename, inverted=inverted)
            assert os.path.exists(filename)
            os.remove(filename)

    def test_palette(self):
        red_palette = Palette(Color(255, 0, 0))

        # Test classmethod
        hash = Crabatar('jake').hash
        assert Palette.from_hash(hash)

        # Test palette generation methods
        assert red_palette.analogous(3, 60)
        assert red_palette.complimentary() == [(1.0, 0.0, 0.0),
                                               (0.0, 1.0, 1.0)]
        assert red_palette.regular(3) == [(1.0, 0.0, 0.0),
                                          (0.0, 1.0, 0.0),
                                          (0.0, 0.0, 1.0)]
        assert red_palette.split_complimentary()
        assert red_palette.tetradic() == [(1.0, 0.0, 0.0),
                                          (1.0, 1.0, 0.0),
                                          (0.0, 1.0, 1.0),
                                          (0.0, 0.0, 1.0)]
        assert red_palette.triad() == red_palette.regular(3)

    def test_generic_utils(self):
        length = 10
        correct_sequence = list(range(length)) + list(reversed(range(length)))
        assert [jsin(i, length) for i in range(length * 2)] == correct_sequence

    def test_drawing_utils(self):
        palette = Palette(Color(0, 255, 255))

        for draw_func in (draw_overlapping_circles, draw_recessed_circles,
                          draw_recessed_triangles, draw_angled_lines,
                          draw_horizontal_lines, draw_vertical_lines,
                          draw_wavy_lines):
            result = draw_func(size=512, palette=palette)
            assert isinstance(result, gizeh.Surface)
