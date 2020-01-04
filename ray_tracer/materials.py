import math

from color import Color
from lights import PointLight
from point import Point
from util import Utilities
from vector import Vector


class Material:
    def __init__(self,
                 color=None,
                 ambient=0.1,
                 diffuse=0.9,
                 specular=0.9,
                 shininess=200.0):
        self._color = Color(red=color.red, green=color.green, blue=color.blue) \
            if color else Color(red=1, green=1, blue=1)
        self._ambient = float(ambient)
        self._diffuse = float(diffuse)
        self._specular = float(specular)
        self._shininess = float(shininess)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = Color(red=value.red, green=value.green, blue=value.blue)

    @property
    def ambient(self):
        return self._ambient

    @ambient.setter
    def ambient(self, value):
        if value >= 0.0:
            self._ambient = value

    @property
    def diffuse(self):
        return self._diffuse

    @diffuse.setter
    def diffuse(self, value):
        if value >= 0.0:
            self._diffuse = value

    @property
    def specular(self):
        return self._specular

    @specular.setter
    def specular(self, value):
        if value >= 0.0:
            self._specular = value

    @property
    def shininess(self):
        return self._shininess

    @shininess.setter
    def shininess(self, value):
        if value >= 0.0:
            self._shininess = value

    def __eq__(self, other):
        return \
            self._color == other._color and \
            Utilities.equal(self._ambient, other._ambient) and \
            Utilities.equal(self._diffuse, other._diffuse) and \
            Utilities.equal(self._specular, other._specular) and \
            Utilities.equal(self._shininess, other._shininess)

    def lighting(self, light, position, eye, normal):
        # Combine the material's color with the intensity/color of the light
        effective_color = self._color * light.intensity

        # Determine the direction to the light source
        light_vector = (light.position - position).normalize()

        # Compute the ambient contribution to the final color, which is not
        # affected by the angle of the light
        ambient = effective_color * self._ambient

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
            diffuse = effective_color * self._diffuse * light_dot_normal

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
                factor = math.pow(reflect_dot_eye, self._shininess)
                specular = light.intensity * self._specular * factor

        return ambient + diffuse + specular
