#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix

        red = graphics.Color(255, 0, 0)
        green = graphics.Color(0, 255, 0)
        blue = graphics.Color(0, 0, 255)
        white = graphics.Color(255, 255, 255)

        OFFSET = 2
        for x in range(0, canvas.width, 5):
            graphics.DrawLine(canvas, x + OFFSET, 0, x + OFFSET, canvas.height, blue)
        try:
            while True:
                time.sleep(100)
        except KeyboardInterrupt:
            pass


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
