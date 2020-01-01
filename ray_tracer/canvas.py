from color import Color

class Canvas:
    def __init__(self, width=0, height=0):
        if width <= 0:
            raise ValueError("Width must be greater than 0")
        if height <= 0:
            raise ValueError("Height must be greater than 0")

        self.width = width
        self.height = height

        # A canvas will be a list, with height lists, each with width Color
        # objects to represent the color at a particular pixel.  So, later
        # when accessing the lists, the y coordinate will represent the first
        # dimension and the x coordinate the second dimension
        self.canvas = [[Color(red=0, blue=0, green=0) for _ in range(width)]
                       for _ in range(height)]

    def _validate_coordinates(self, x=0, y=0):
        if x < 0 or x >= self.width:
            raise ValueError("X coordinate is out of bounds")

        if y < 0 or y >= self.height:
            raise ValueError("Y coordinate is out of bounds")

    def get_pixel(self, x=0, y=0):
        self._validate_coordinates(x=x, y=y)

        return self.canvas[y][x]

    def set_pixel(self, x=0, y=0, color=Color()):
        self._validate_coordinates(x=x, y=y)

        # When inserting, we are going to create a new color object as storing
        # the reference provided would be bad if the caller modifies the
        # referenced color object
        self.canvas[y][x] = Color(red=color.red,
                                  blue=color.blue,
                                  green=color.green)

    def to_ppm(self):
        header = "P3\n{} {}\n255".format(self.width, self.height)

        # Walk through each row and convert the colors to a line of text of
        # 3-tuples with spaces between values and a newline at the end of each
        # row.  Limit line length, not including newline, to 70 characters
        pixel_text = []
        for y in range(self.height):
            y_text = []
            for x in range(self.width):
                y_text.append("{}".format(self.canvas[y][x]))
            y_text = " ".join(y_text)

            # If the line is 70 or fewer characters in length, then just append
            # the line to the lines we have created.  Otherwise...break the
            # lines...
            if len(y_text) <= 70:
                pixel_text.append(y_text)
            else:
                # Note we assume well-formed lines.  A line of all spaces
                # would break this.

                # While there are more than 70 characters left in the line,
                # starting at character 71, walk backwards until we get to a
                # space.  Slice the string so that the front part (from
                # beginning to the last character before the space) is added
                # to the list of lines we already have and the back part (from
                # the first character after the space until the end is re-
                # assigned to the line we are working on.
                while len(y_text) > 70:
                    index = 70
                    while y_text[index] != ' ':
                        index -= 1
                    pixel_text.append(y_text[:index])
                    y_text = y_text[index + 1:]

                # Append anything left over to the list of lines we are
                # accumulating.
                pixel_text.append(y_text)

        # Combine the header plus each of the accumulated lines joined by a
        # newline to be the resulting PPM data.
        return "{}\n{}\n".format(header, "\n".join(pixel_text))