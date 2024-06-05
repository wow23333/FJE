import argparse
from icons.default_icon_factory import DefaultIconFactory
from icons.poker_icon_factory import PokerIconFactory
from explorer.explorer import FunnyJsonExplorer
from styles.rectangle_factory import RectangleStyleFactory
from styles.tree_factory import TreeStyleFactory


def get_style_factory(style):
    if style == 'tree':
        return TreeStyleFactory()
    elif style == 'rectangle':
        return RectangleStyleFactory()
    else:
        raise ValueError(f"Unknown style: {style}")


def get_icon_factory(icon_family, icon_config):
    if icon_family == 'default':
        return DefaultIconFactory()
    elif icon_family == 'poker':
        return PokerIconFactory(icon_config)
    else:
        raise ValueError(f"Unknown icon family: {icon_family}")


def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer (FJE)')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'],
                        help='Style of the visualization')
    parser.add_argument('-i', '--icon', required=True, choices=['default', 'poker'],
                        help='Icon family for the visualization')

    args = parser.parse_args()

    style_factory = get_style_factory(args.style)
    icon_config = 'Icon_families/icon_config.json'
    icon_factory = get_icon_factory(args.icon, icon_config)

    explorer = FunnyJsonExplorer(style_factory, icon_factory)
    explorer.show(args.file)


if __name__ == "__main__":
    main()
