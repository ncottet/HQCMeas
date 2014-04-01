# -*- coding: utf-8 -*-
#==============================================================================
# module : base_editor.py
# author : Matthieu Dartiailh
# license : MIT license
#==============================================================================
from atom.api import Callable, Unicode, Instance, Bool, Event
from enaml.core.declarative import Declarative, d_
from enaml.widgets.api import Page

from hqc_meas.tasks.api import BaseTask


class BaseEditor(Page):
    """ Base class for all editors.

    """
    # Id of the builder which created this editor.
    id = Unicode()

    # Currently selected task in the tree.
    selected_task = Instance(BaseTask)

    # Should the tree be visible when this editor is selected.
    tree_visible = d_(Bool(True))

    # Should the tree be enabled when this editor is selected.
    tree_enabled = d_(Bool(True))

    # Event receiving the new measure being edited when it changes. This event
    # can be handled to clear any cached infos hold by the editor.
    new_measure = d_(Event())


class Editor(Declarative):
    """ Extension for the 'editors' extension point of a MeasurePlugin.

    """
    # Editor description.
    description = d_(Unicode())

    # Factory function returning an instance of the editor. This callable
    # should take as single arguiment a reference to the workbench.
    factory = d_(Callable())

    # Test function determining if the editor is fit to be used for the
    # selected task. This function should take as arguments the workbench and
    # the selected task and return a boolean.
    test = d_(Callable())