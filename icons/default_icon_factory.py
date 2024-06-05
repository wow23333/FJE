from .icon_factory import IconFactory


class DefaultIconFactory(IconFactory):
    def get_icon(self, is_leaf):
        return ''
