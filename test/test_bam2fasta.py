from bioconvert.bam2fasta import BAM2Fasta
from bioconvert import bioconvert_data
from easydev import TempFile, md5

def test_conv():
    infile = bioconvert_data("test_measles.sorted.bam")
    with TempFile(suffix=".fa") as tempfile:
        convert = BAM2Fasta(infile, tempfile.name)
        convert(method="bamtools")

        # Check that the output is correct with a checksum
        # Note that we cannot test the md5 on a gzip file but only 
        # on the original data. This check sum was computed
        # fro the unzipped version of biokit/data/converters/measles.bed
        assert md5(tempfile.name) == "ea5511c3c8913626be152609887c8c4d"

        convert = BAM2Fasta(infile, tempfile.name)
        convert(method="samtools")
        assert md5(tempfile.name) == "cc9afcef458f3402fbdef1a091e05c39"

        # md5 are different but differences is just due to a split of the fastq on several lines
