import logging

from multiqc.base_module import BaseMultiqcModule, ModuleNoSamplesFound

from .qualcal import QualCalMixin

log = logging.getLogger(__name__)


class MultiqcModule(BaseMultiqcModule, QualCalMixin):
    """
    Supported tools:

    - `QualCal`

    #### QualCal

    [QualCal](https://support.sentieon.com/manual/usages/general/#qualcal-algorithm) is a tool for
    detecting systematic errors in read base quality scores of aligned high-throughput sequencing
    reads. It is closely related to [BaseRecalibrator](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_gatk_tools_walkers_bqsr_BaseRecalibrator.php).
    """

    def __init__(self):
        super(MultiqcModule, self).__init__(
            name="Sentieon",
            anchor="sentieon",
            target="Sentieon",
            href="https://www.sentieon.com/",
            info="Sentieon Genomics software is a set of software tools that perform analysis of genomic data obtained from DNA sequencing.",
            doi=["10.1101/115717"],
        )

        # Set up class objects to hold parsed data
        self.general_stats_headers = {}
        self.general_stats_data = {}

        # Call submodule functions
        n_reports_found = 0
        n_reports_found += self.parse_sentieon_qualcal()

        # Exit if we didn't find anything
        if n_reports_found == 0:
            raise ModuleNoSamplesFound

        # Add to the General Stats table (has to be called once per MultiQC module)
        self.general_stats_addcols(self.general_stats_data, self.general_stats_headers)

    def parse_report(self, lines, table_names):
        """Parse a Sentieon QualCal report

        Only SENTIEON_QCAL_TABLE entries are parsed.  Tables are returned as a dict of tables.
        Each table is a dict of arrays, where names correspond to column names, and arrays
        correspond to column values.

        Args:
            lines (file handle): an iterable over the lines of a Sentieon QualCal report report.
            table_names (dict): a dict with keys that are Sentieon QualCal report report table names
                (e.g. "#:SENTIEON_QCAL_TABLE:Quantized:Quality quantization map"), and values that are the
                keys in the returned dict.

        Returns:
            {
                table_1:
                    {
                        col_1: [ val_1, val_2, ... ]
                        col_2: [ val_1, val_2, ... ]
                        ...
                    }
                table_2:
                    ...
            }
        """

        report = dict()
        lines = (line for line in lines)
        for line in lines:
            line = line.rstrip()
            if line in table_names.keys():
                report[table_names[line]] = self.parse_sentieon_qualcal_report_table(lines)
        return report

    @staticmethod
    def parse_sentieon_qualcal_report_table(lines):
        headers = next(lines).rstrip().split()
        table = {h: [] for h in headers}
        for line in lines:
            line = line.rstrip()

            # testing to see if we have reached the end of a table in a Sentieon QualCal report
            if line == "":
                break

            for index, value in enumerate(line.split()):
                table[headers[index]].append(value)
        return table
