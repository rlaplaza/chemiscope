import os

from chemiscope.jupyter import ChemiscopeWidget, MapWidget, StructureWidget

from .file_path_iterator import FilePathIterator


class ChemiscopeScraper:
    """Custom scraper for Chemiscope visualizations"""

    def __repr__(self):
        return "ChemiscopeScraper"

    def __call__(self, _block, block_vars, gallery_conf):
        # Get a target directory with the source files
        examples_data_dir = gallery_conf.get("examples_dirs")
        target_dir = os.path.join(examples_data_dir, "data")
        os.makedirs(target_dir, exist_ok=True)

        # Create an iterator to generate the file name
        iterator = FilePathIterator(target_dir)

        # Retrieve the chemiscope widget from block variables
        widget = block_vars.get("example_globals", {}).get("___")

        if widget:
            dataset_file_path = iterator.next()
            widget.save(dataset_file_path)

            if type(widget) is ChemiscopeWidget:
                mode = "default"
            elif type(widget) is StructureWidget:
                mode = "structure"
            elif type(widget) is MapWidget:
                mode = "map"
            else:
                raise TypeError("Scraped widget is not a chemiscope widget")

            return f""".. chemiscope::
                :filename: {os.path.basename(dataset_file_path)}
                :mode: {mode}
            """
        else:
            return ""