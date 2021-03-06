import yaml


default_manifest = yaml.safe_load("""
---
# version is for the format of this file, not its contents.
version: 0

context:
    class: insights.core.context.HostContext
    args:
        timeout: 10 # timeout in seconds for commands. Doesn't apply to files.

# disable everything by default
# defaults to false if not specified.
default_component_enabled: false

# commands and files to ignore
blacklist:
    files: []
    commands: []
    patterns: []
    keywords: []

# packages and modules to load
packages:
    - insights.specs.default

# Can be a list of dictionaries with name/enabled fields or a list of strings
# where the string is the name and enabled is assumed to be true. Matching is
# by prefix, and later entries override previous ones. Persistence for a
# component is disabled by default.
persist:
    - name: insights.specs.Specs
      enabled: true

# configuration of loaded components. names are prefixes, so any component with
# a fully qualified name that starts with a key will get the associated
# configuration applied. Can specify timeout, which will apply to command
# datasources. Can specify metadata, which must be a dictionary and will be
# merged with the components' default metadata.
configs:
    - name: insights.specs.Specs
      enabled: true

    - name: insights.specs.default.DefaultSpecs
      enabled: true

    - name: insights.parsers.hostname
      enabled: true

    - name: insights.parsers.facter
      enabled: true

    - name: insights.parsers.systemid
      enabled: true

    - name: insights.combiners.hostname
      enabled: true

# needed because some specs aren't given names before they're used in DefaultSpecs
    - name: insights.core.spec_factory
      enabled: true
""")


def get_manifest(machine_id):
    return default_manifest
