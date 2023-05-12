"""
``cubi-isa-templates``: Create ISA-tab TSV files from templates with `Cookiecutter`_.

This repository contains ISA-Tab templates originally in the ``dubi-tk`` package. They can be
imported to be used in other projects with minimal external depdendencies.

Available Templates
-------------------

The `Cookiecutter`_ directories are located in this module's directory.  Currently available
templates are:

- ``isatab-generic``
- ``isatab-germline``
- ``isatab-microarray``
- ``isatab-ms_meta_biocrates``
- ``isatab-single_cell_rnaseq``
- ``isatab-stem_cell_core``
- ``isatab-stem_cell_core_bulk``
- ``isatab-stem_cell_core_sc``
- ``isatab-bulk_rnaseq``
- ``isatab-tumor_normal_dna``
- ``isatab-tumor_normal_triplets``

Adding Templates
----------------

Adding templates consists of the following steps:

1. Add a new template directory below ``cubi_isa_templates``.
2. Register the directory by appending a ``IsaTabTemplate`` object to ``_TEMPLATES`` in
   ``cubi_isa_templates/__init__.py``.
3. Add it to the list above in the docstring.
4. Submit a pull request for the addition.

The easiest way to start out is to copy an existing cookiecutter template and registration.

More Information
----------------

For using these in ``cubi-tk``, see ``cubi-tk isa-tpl`` CLI documentation and
``cubi-tk isa-tab --help`` for more information.

.. _Cookiecutter: https://cookiecutter.readthedocs.io/
"""

import attr
import json
import os
import typing


#: Base directory to this file.
_BASE_DIR = os.path.dirname(__file__)


@attr.s(frozen=True, auto_attribs=True)
class IsaTabTemplate:
    """Information regarding an ISA-tab template."""

    #: Name of the ISA-tab template.
    name: str

    #: Path to template directory.
    path: str

    #: Configuration loaded from ``cookiecutter.json``.
    configuration: typing.Dict[str, typing.Any]

    #: Optional description string.
    description: typing.Optional[str] = None


def load_variables(template_name, extra=None):
    """Load variables given the template name."""
    extra = extra or {}
    config_path = os.path.join(_BASE_DIR, template_name, "cookiecutter.json")
    with open(config_path, "rt") as inputf:
        result = json.load(inputf)
    result.update(extra)
    return result


#: Known ISA-tab templates (internal, mapping generated below).
_TEMPLATES = (
    IsaTabTemplate(
        name="single_cell_rnaseq",
        path=os.path.join(_BASE_DIR, "isatab-single_cell_rnaseq"),
        description="single cell RNA sequencing ISA-tab template",
        configuration=load_variables("isatab-single_cell_rnaseq"),
    ),
    IsaTabTemplate(
        name="bulk_rnaseq",
        path=os.path.join(_BASE_DIR, "isatab-bulk_rnaseq"),
        description="bulk RNA sequencing ISA-tab template",
        configuration=load_variables("isatab-generic"),
    ),
    IsaTabTemplate(
        name="tumor_normal_dna",
        path=os.path.join(_BASE_DIR, "isatab-tumor_normal_dna"),
        description="Tumor-Normal DNA sequencing ISA-tab template",
        configuration=load_variables("isatab-tumor_normal_dna", {"is_triplet": False}),
    ),
    IsaTabTemplate(
        name="tumor_normal_triplets",
        path=os.path.join(_BASE_DIR, "isatab-tumor_normal_triplets"),
        description="Tumor-Normal DNA+RNA sequencing ISA-tab template",
        configuration=load_variables("isatab-tumor_normal_triplets", {"is_triplet": True}),
    ),
    IsaTabTemplate(
        name="germline",
        path=os.path.join(_BASE_DIR, "isatab-germline"),
        description="germline DNA sequencing ISA-tab template",
        configuration=load_variables("isatab-germline"),
    ),
    IsaTabTemplate(
        name="generic",
        path=os.path.join(_BASE_DIR, "isatab-generic"),
        description="generic RNA sequencing ISA-tab template",
        configuration=load_variables("isatab-generic"),
    ),
    IsaTabTemplate(
        name="microarray",
        path=os.path.join(_BASE_DIR, "isatab-microarray"),
        description="microarray ISA-tab template",
        configuration=load_variables("isatab-microarray"),
    ),
    IsaTabTemplate(
        name="ms_meta_biocrates",
        path=os.path.join(_BASE_DIR, "isatab-ms_meta_biocrates"),
        description="MS Metabolomics Biocrates kit ISA-tab template",
        configuration=load_variables("isatab-ms_meta_biocrates"),
    ),
    IsaTabTemplate(
        name="stem_cell_core_bulk",
        path=os.path.join(_BASE_DIR, "isatab-stem_cell_core_bulk"),
        description="Bulk RNA sequencing ISA-tab template from hiPSC for stem cell core projects",
        configuration=load_variables("isatab-stem_cell_core_bulk"),
    ),
    IsaTabTemplate(
        name="stem_cell_core_sc",
        path=os.path.join(_BASE_DIR, "isatab-stem_cell_core_sc"),
        description="Single cell RNA sequencing ISA-tab template from hiPSC for stem cell core "
        "projects",
        configuration=load_variables("isatab-stem_cell_core_sc"),
    ),
)

#: Known ISA-tab templates.
TEMPLATES = {tpl.name: tpl for tpl in _TEMPLATES}