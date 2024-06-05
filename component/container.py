from component.component import Component


class Container(Component):
    def __init__(self, name, level, style):
        super().__init__(name, level, style)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, prefix, is_last):
        pass
