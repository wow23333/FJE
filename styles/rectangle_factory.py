from .abstract_factory import StyleFactory
from component.concrete_container import ConcreteContainer
from component.concrete_leaf import ConcreteLeaf


class RectangleStyleFactory(StyleFactory):
    def create_container(self, name, level):
        return ConcreteContainer(name, level, style='rectangle')

    def create_leaf(self, name, level):
        return ConcreteLeaf(name, level, style='rectangle')
