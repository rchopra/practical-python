# tableformat.py


class TableFormatter:
    def headings(self, headers):
        """Emit the table headings."""
        raise NotImplementedError()

    def row(self, rowdata):
        """Emit a single row of table data."""
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """Emit a table in plan-text format."""

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """Output portfolio data in CSV format."""

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """Output portfolio data in HTML format."""

    def headings(self, headers):
        print("<tr>", end="")
        for h in headers:
            print(f"<th>{h}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for d in rowdata:
            print(f"<td>{d}</td>", end="")
        print("</tr>")


class FormatError(Exception):
    pass


def create_formatter(name):
    """Create an appropriate formatter given an output format name."""
    if name == "txt":
        return TextTableFormatter()
    if name == "csv":
        return CSVTableFormatter()
    if name == "html":
        return HTMLTableFormatter()
    raise FormatError(f"Unknown table format {name}")


def print_table(objects, columns, formatter):
    """Make a nicely formatted table from a list of objects and attribute names."""
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)
