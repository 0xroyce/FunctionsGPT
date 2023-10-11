import os
import importlib

def scan_extensions_directory():
    """Find the extensions directory and return a list of all extensions."""
    # Start with the current directory of the script
    directory = os.path.dirname(os.path.abspath(__file__))

    # Loop to keep going up the directory tree
    while True:
        # Check if the 'extensions' directory exists in the current directory
        if 'extensions' in os.listdir(directory):
            extensions_dir = os.path.join(directory, 'extensions')
            return [item for item in os.listdir(extensions_dir)
                    if os.path.isdir(os.path.join(extensions_dir, item))
                    and not item.startswith("__")]

        # Move up one directory level
        parent_directory = os.path.dirname(directory)

        # If we're already at the system root, break out of the loop
        if directory == parent_directory:
            break

        directory = parent_directory

    raise FileNotFoundError("Could not find 'extensions' directory.")

class ExtensionManager:
    """Manager class to handle the dynamic loading and accessing of extensions."""

    def __init__(self):
        self.extensions = {}

    def load_extensions(self):
        """Load all extensions from the extensions directory."""
        extension_dirs = scan_extensions_directory()
        for ext in extension_dirs:
            try:
                # Dynamically import the extension's model_manager module
                module = importlib.import_module(f"extensions.{ext}.model_manager")

                # Get the main class from the module, instantiate it, and store its details
                extension_class = getattr(module, ext.capitalize())
                extension_instance = extension_class()

                # Check if the extension has the function_specification method
                if hasattr(extension_instance, "function_specification"):
                    description = extension_instance.description()
                    self.extensions[ext] = {"instance": extension_instance, "description": description}
            except (ImportError, AttributeError) as e:
                print(f"Failed to load extension {ext}. Error: {e}")

    def get_extension(self, name):
        """Get the instance of a specific extension."""
        return self.extensions.get(name, {}).get("instance")

    def get_all_descriptions(self):
        """Get descriptions of all loaded extensions."""
        return {name: ext["description"] for name, ext in self.extensions.items()}


if __name__ == "__main__":
    manager = ExtensionManager()
    manager.load_extensions()
    descriptions = manager.get_all_descriptions()

    for ext_name, desc in descriptions.items():
        print(f"Extension: {ext_name}")
        print(f"Description: {desc}")
        print('-' * 50)