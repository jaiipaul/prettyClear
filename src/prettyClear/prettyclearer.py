import os
import random
import prettyClear.shapes as shapes


class PrettyClearer:
    def __init__(self):
        self.shape_registry = shapes.ShapeRegistry()

    def _clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _pick_random_shape(self):
        n_shapes = len(self.shape_registry.registry)
        random_pick = random.randint(0, n_shapes-1)
        return self.shape_registry.get_registered_shapes()[random_pick]

    def run(self):
        self._clear_console()
        self._pick_random_shape().draw()
