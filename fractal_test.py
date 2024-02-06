import main as mn
import unittest as ut
import numpy as np
import matplotlib.pyplot as plt

epsilon = 1e-7


class TestSegmentsAreMadeOfPoints(ut.TestCase):
    def test_segments_are_made_of_points(self):
        with self.assertRaises(TypeError):
            mn.Segment([0, 0], [1, 1])


class TestGenerateSegment(ut.TestCase):
    def test_generate_segment_wo_scale(self):
        point1 = mn.Point(-1, -1)
        point2 = mn.Point(1, 1)
        segment = mn.generate_segment(mn.Point(0, 0), [1, 1])
        self.assertEqual(segment.p1, point1)
        self.assertEqual(segment.p2, point2)

    def test_generate_segment_with_scale(self):
        point1 = mn.Point(-0.5, -0.5)
        point2 = mn.Point(0.5, 0.5)
        scale = 0.5
        segment = mn.generate_segment(mn.Point(0, 0), [1, 1], scale)
        self.assertEqual(segment.p1, point1)
        self.assertEqual(segment.p2, point2)


class TestGenerateMainDrawSegments(ut.TestCase):
    def test_generate_main_draw_wo_scale_wo_rot_segments(self):
        base = [0, 0]
        angles = list(map(lambda x: x * np.pi, [0, 0.5]))

        point1 = mn.Point(-0.5, 0)
        point2 = mn.Point(0.5, 0)
        point3 = mn.Point(0, -0.25)
        point4 = mn.Point(0, 0.25)
        s1 = mn.Segment(point1, point2)
        s2 = mn.Segment(point3, point4)

        target_segments = [s1, s2]

        draw = mn.generate_main_draw(base, angles)

        for segm in range(len(draw.segments)):
            for extreme in range(2):
                for coord in range(2):
                    elem1 = draw.segments[segm].get_coordinates()[extreme][coord]
                    elem2 = target_segments[segm].get_coordinates()[extreme][coord]
                    self.assertLess(np.abs(elem1 - elem2), epsilon)

    def test_generate_main_draw_wo_scale_wo_rot_basis(self):
        base = [0, 0]
        angles = list(map(lambda x: x * np.pi, [0, 0.5]))

        point1 = mn.Point(-0.5, 0)
        point2 = mn.Point(0.5, 0)
        point3 = mn.Point(0, -0.25)
        point4 = mn.Point(0, 0.25)

        target_basis = [point1, point2, point3, point4]

        draw = mn.generate_main_draw(base, angles)

        for base in range(len(draw.basis)):
            for extreme in range(2):
                elem1 = draw.basis[base]
                elem2 = target_basis[base]
                self.assertLess(np.abs(elem1.x - elem2.x), epsilon)
                self.assertLess(np.abs(elem1.y - elem2.y), epsilon)
