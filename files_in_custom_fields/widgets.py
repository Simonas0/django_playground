from django import forms


class MultiWidget(forms.MultiWidget):
    def decompress(self, value):
        return value or (None,)

    def value_from_datadict(self, data, files, name):
        return tuple(
            widget.value_from_datadict(data, files, name + "_%s" % i)
            for i, widget in enumerate(self.widgets)
        )
