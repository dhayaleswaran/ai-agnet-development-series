from blueprint.data_adapter import DataAdapter


class TextExtractor(DataAdapter):
    def extract(self, path):
        is_file = super().file_exists(path)
        if not is_file:
            print(f"File {path} does not exist.")
            return None

        with open(path, "r", encoding="utf-8") as data_source_item:
            return data_source_item.read()
