from easydev import TempFile

from bioconvert import bioconvert_data
from bioconvert.core import decorators
from bioconvert.core.decorators import requires


def test_require_binaries():
    def f():
        pass

    g = requires(external_binary="mv")(f)
    assert g.is_disabled is False
    # test cache now
    g = requires(external_binary="mv")(f)
    assert g.is_disabled is False
    g = requires(external_binaries=["ls", ])(f)
    assert g.is_disabled is False
    g = requires(external_binaries=["ls", "mv", ])(f)
    assert g.is_disabled is False

    g = requires(external_binary="tagada1")(f)
    assert g.is_disabled
    # test cache now
    g = requires(external_binary="tagada1")(f)
    assert g.is_disabled
    g = requires(external_binaries=["rm", "tagada2"])(f)
    assert g.is_disabled


def test_require_libraries():
    def f():
        pass

    g = requires(python_library="wheel")(f)
    assert g.is_disabled is False
    # test cache now
    g = requires(python_library="wheel")(f)
    assert g.is_disabled is False
    g = requires(python_libraries=["pip", ])(f)
    assert g.is_disabled is False
    g = requires(python_libraries=["pip", "wheel", ])(f)
    assert g.is_disabled is False

    g = requires(python_library="tagada3")(f)
    assert g.is_disabled
    # test cache now
    g = requires(python_library="tagada3")(f)
    assert g.is_disabled
    g = requires(python_libraries=["urllib3", "tagada4"])(f)
    assert g.is_disabled


def test_require_both():
    def f():
        pass

    g = requires(python_library="wheel", external_binary="top")(f)
    assert g.is_disabled is False

    g = requires(python_library="tagada5", external_binary="top")(f)
    assert g.is_disabled

    g = requires(python_library="wheel", external_binary="tagada6")(f)
    assert g.is_disabled

    g = requires(python_library="tagada7", external_binary="tagada8")(f)
    assert g.is_disabled


def test_get_compression_format():
    assert decorators.get_compression_format(bioconvert_data('SRR390728_2.fastq.7z')) == "7Z"
    assert decorators.get_compression_format(bioconvert_data('SRR390728_2.fastq.tar.xz')) == "XZ"
    assert decorators.get_compression_format(bioconvert_data('SRR390728_2.fastq.zip')) == "ZIP"
    assert decorators.get_compression_format(bioconvert_data('SRR390728_2.fastq.gz')) == "GZ"
    assert decorators.get_compression_format(bioconvert_data('SRR390728_2.fastq')) == "UNKNOWN"
    with TempFile(suffix=".7z") as tempfile:
        assert decorators.get_compression_format(tempfile.name) == "UNKNOWN"
    with TempFile(suffix=".gz") as tempfile:
        with open(tempfile.name, 'w') as out:
            out.write("eee")
        assert decorators.get_compression_format(tempfile.name) == "UNKNOWN"
