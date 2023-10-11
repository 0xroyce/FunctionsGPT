import os
from extensions.extension_interface import ExtensionInterface


class Hello_world(ExtensionInterface):

    @staticmethod
    def description():
        """
        Returns a description of the HelloWorld extension.
        """
        return """The Hello_world function simply returns a greeting from Virtuoso Edge."""

    @staticmethod
    def function_specification():
        """Returns the function specification for this extension."""
        return {
            "name": "Hello_world_execute",
            "description": f"""{Hello_world.description()}""",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            }
        }

    def __init__(self):
        pass

    def initialize(self):
        """Initialize the HelloWorld extension."""
        pass

    def execute(self):
        """Return a greeting from Virtuoso Edge."""
        return "Hello World from Virtuoso Edge"

    def shutdown(self):
        """Shutdown method for the Hello_world extension."""
        pass


if __name__ == "__main__":
    manager = Hello_world()
    manager.initialize()  # Initialize the extension

    try:
        result = manager.execute()
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
