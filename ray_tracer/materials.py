import math

from color import Color
from util import Utilities


class Material:
    def __init__(self,
                 color=None,
                 ambient=0.1,
                 diffuse=0.9,
                 specular=0.9,
                 shininess=200.0):
        self.color = color
        self.ambient = float(ambient)
        self.diffuse = float(diffuse)
        self.specular = float(specular)
        self.shininess = float(shininess)
        self.pattern = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = Color(red=value.red, green=value.green, blue=value.blue) \
            if value else Color(red=1, green=1, blue=1)

    @property
    def ambient(self):
        return self._ambient

    @ambient.setter
    def ambient(self, value):
        self._ambient = value if value >= 0.0 else 0.0

    @property
    def diffuse(self):
        return self._diffuse

    @diffuse.setter
    def diffuse(self, value):
        self._diffuse = value if value >= 0.0 else 0.0

    @property
    def specular(self):
        return self._specular

    @specular.setter
    def specular(self, value):
        self._specular = value if value >= 0.0 else 0.0

    @property
    def shininess(self):
        return self._shininess

    @shininess.setter
    def shininess(self, value):
        self._shininess = value if value >= 0.0 else 0.0

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        self._pattern = value

    def __eq__(self, other):
        return \
            self.color == other.color and \
            Utilities.equal(self.ambient, other.ambient) and \
            Utilities.equal(self.diffuse, other.diffuse) and \
            Utilities.equal(self.specular, other.specular) and \
            Utilities.equal(self.shininess, other.shininess)

    def __ne__(self, other):
        return not self == other

    def lighting(self, shape, light, position, eye, normal, in_shadow):
        # If the material has a pattern, then figure out the color of the
        # pattern at the position.  Otherwise, use the material's default
        # color
        if self.pattern is not None:
            color = self.pattern.shape_color_at(shape=shape, position=position)
        else:
            color = self.color

        # Combine the material's color with the intensity/color of the light
        effective_color = color * light.intensity

        # Determine the direction to the light source
        light_vector = (light.position - position).normalize()

        # Compute the ambient contribution to the final color, which is not
        # affected by the angle of the light
        ambient = effective_color * self.ambient

        # Take the dot product of the light vector and the normal vector.  This
        # is the cosine of the angle between the two vectors.  A number less
        # than zero indicates that the light source is behind the surface.  In
        # that case, the diffuse and specular components contribute nothing to
        # the final color.
        light_dot_normal = light_vector.dot_product(normal)
        if light_dot_normal < 0:
            diffuse = specular = Color(red=0, green=0, blue=0)
        else:
            # Compute the diffuse contribution to the final color
            diffuse = effective_color * self.diffuse * light_dot_normal

            # Take the dot product of the reflection vector (computed from the
            # light vector and the normal vector) and the eye vector.  This is
            # the cosine of the angle between the two vectors.  A number less
            # than zero indicates that the light reflects away from the eye.  In
            # that case the specular component contributes nothing to the final
            # color.
            reflect_vector = (-light_vector).reflect(normal)
            reflect_dot_eye = reflect_vector.dot_product(eye)
            if reflect_dot_eye < 0:
                specular = Color(red=0, green=0, blue=0)
            else:
                # Contribute the specular contribution to the final color
                factor = math.pow(reflect_dot_eye, self.shininess)
                specular = light.intensity * self.specular * factor

        return ambient if in_shadow else ambient + diffuse + specular
