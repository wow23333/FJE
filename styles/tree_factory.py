from .abstract_factory import StyleFactory
from component.concrete_container import ConcreteContainer
from component.concrete_leaf import ConcreteLeaf


class TreeStyleFactory(StyleFactory):
    def create_container(self, name, level):
        return ConcreteContainer(name, level, style='tree')

    def create_leaf(self, name, level):
        return ConcreteLeaf(name, level, style='tree')
