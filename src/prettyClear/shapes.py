import os
import random


class Shape:
    def __init__(self, name: str, pattern: str = ''):
        self._name = name
        self._pattern = pattern

    @property
    def name(self) -> str:
        return self._name

    @property
    def pattern(self) -> str:
        return self._pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self._pattern = pattern

    def draw(self):
        pattern_lines = self.pattern.split('\n')
        line_length = len(pattern_lines[0])+1
        term_length = os.get_terminal_size().columns
        n_pattern = random.randint(1, int(term_length/line_length))
        colors = {f'\033[{random.randint(40, 47)}m'
                  for _ in range(n_pattern)}

        for p_line in pattern_lines:
            term_line = ' '
            for color in colors:
                cur_line = p_line.replace("x", color+" \033[0m")
                term_line += cur_line+' '
            print(term_line)


class ShapeRegistry:
    def __init__(self):
        self._registry: dict[str, Shape] = {}

    @property
    def registry(self) -> dict[str, Shape]:
        return self._registry

    def initialize(self, shape_pattern_dict: dict[str, str]):
        for name, pattern in shape_pattern_dict.items():
            self.register(Shape(name, pattern))

    def register(self, shape: Shape) -> Shape | None:
        if (shape.name, shape) in self._registry.items():
            print(f'Shape {shape.name} already registred...')
            return None
        self._registry[shape.name] = shape
        return shape

    def get_registered_shapes(self) -> list[Shape]:
        return list(self._registry.values())

    def get(self, shape_name: str) -> Shape | None:
        if shape_name not in self._registry:
            print(f'No shape found with name {shape_name}')
        return self._registry[shape_name]
