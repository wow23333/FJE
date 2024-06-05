from icons.default_icon_factory import DefaultIconFactory
from icons.poker_icon_factory import PokerIconFactory
from explorer.explorer_builder import ExplorerBuilder
from styles.rectangle_factory import RectangleStyleFactory
from styles.tree_factory import TreeStyleFactory


def main():
    json_file = './assets/example.json'
    # json_file = './assets/complex.json'
    # json_file = './assets/middle.json'
    # json_file = './assets/simple.json'
    icon_config = 'Icon_families/icon_config.json'

    builder = ExplorerBuilder()

    print("Tree Style with Default Icons:")
    explorer = builder.set_style_factory(TreeStyleFactory()).set_icon_factory(DefaultIconFactory()).build()
    explorer.show(json_file)
    print()

    print("Rectangle Style with Default Icons:")
    explorer = builder.set_style_factory(RectangleStyleFactory()).set_icon_factory(DefaultIconFactory()).build()
    explorer.show(json_file)
    print()

    print("Tree Style with Poker Icons:")
    explorer = builder.set_style_factory(TreeStyleFactory()).set_icon_factory(PokerIconFactory(icon_config)).build()
    explorer.show(json_file)
    print()

    print("Rectangle Style with Poker Icons:")
    explorer = builder.set_style_factory(RectangleStyleFactory()).set_icon_factory(
        PokerIconFactory(icon_config)).build()
    explorer.show(json_file)
    print()


if __name__ == "__main__":
    main()
