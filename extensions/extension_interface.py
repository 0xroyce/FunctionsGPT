from abc import ABC, abstractmethod

class ExtensionInterface(ABC):

    @abstractmethod
    def initialize(self):
        """Initialize the extension."""
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute the extension's main functionality."""
        pass

    @abstractmethod
    def shutdown(self):
        """Perform any cleanup or shutdown operations."""
        pass
