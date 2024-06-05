from component.component import Component


class Leaf(Component):
    def __init__(self, name, level, style):
        super().__init__(name, level, style)

    def draw(self, prefix, is_last):
        pass
