# FunctionsGPT: Powering Extensibility in OpenAI

## Overview

FunctionsGPT is a dynamic Python script tailored to extend the capabilities of OpenAI. It empowers developers to create modular extensions, which can be invoked as distinct functions. By adhering to a standardized structure and interface, these extensions ensure seamless integration and execution, enhancing OpenAI's versatility without compromising its core functionalities.

## Why FunctionsGPT?

- Plug-and-Play Functionality: With the aim to keep the main application stable, the extensions are designed to be easily plugged in and played without any disruption.
- Standardized Structure: By adhering to the ExtensionInterface, developers can ensure uniformity and predictability in their extensions.
- Simplicity at its Core: From utilizing an extension to creating a new one, the processes are simplified, ensuring even newcomers to the platform can get started quickly.
- Open Ecosystem: Being open-source, FunctionsGPT thrives on community contributions. Developers can add, modify, or improve extensions, fostering a continuously evolving ecosystem.

## Core Features

- Directory Structure: Ensures every extension is organized in a standardized manner, enhancing clarity and maintainability.
- Key Elements of an Extension: From providing a crisp description to ensuring the right resources are available, FunctionsGPT ensures all extensions are comprehensive.
- Extension Interface: Maintaining uniformity across extensions, the interface mandates essential methods ensuring consistency in extensions' behavior.
- Ease of Usage: Just a few steps to utilize any extension – Import, Initialize, Execute, and optionally Shutdown.

## How To Build An Extensions

### Table of Contents
- [Introduction](#introduction)
- [Directory Structure](#directory-structure)
- [Extension Interface](#extension-interface)
- [Using an Extension](#using-an-extension)
- [Adding a New Extension](#adding-a-new-extension)

---

### Introduction
Extensions provide a modular way to add functionality to the core system. They are designed to be plug-and-play, ensuring that adding new features or updating existing ones does not disrupt the main application.

---

### Directory Structure
Each extension resides in its own directory within the `extensions` folder. The typical directory structure of an extension is as follows:

<pre>
extensions/
|-- name_of_extension/
    |-- model_manager.py
    |-- resources/
        |-- prompts.json
</pre>


- `model_manager.py`: The main Python script containing the extension's logic.
- `resources/`: A directory containing any resource files used by the extension, such as `prompts.json`.

---

### Key Elements of an Extension
Each extension should have the following key elements:

- **Description**: A brief overview of what the extension does.
- **Function Specification**: A detailed specification of the extension's functionality, including its name, a description, parameters, and any other relevant details.
- **Methods**: Functions or methods that implement the extension's logic, including initialization, execution, and shutdown procedures.
- **Resources**: Any additional files or data the extension might need, stored in the `resources/` directory.

---

### Extension Interface
Every extension must conform to the `ExtensionInterface`. This interface maintains a uniform structure across extensions. It mandates the implementation of:

- `description()`: Offers a sufficient description of the extension.
- `function_specification()`: Provides a detailed specification of the extension's function.
- `initialize()`: Sets up necessary configurations for the extension.
- `execute()`: Triggers the primary functionality of the extension.
- `shutdown()`: Manages any cleanup tasks post usage.

---

### Using an Extension
To employ an extension:

1. Import the pertinent extension class.
2. Instantiate the extension.
3. Invoke the `initialize()` method for setup.
4. Use `execute()` to initiate the extension's main function.
5. If necessary, use `shutdown()` for cleanup.

**Example**:

```python
from extensions.name_of_extension.model_manager import TheClass

# Initialize the extension
manager = TheClass()
manager.initialize()

# Use the extension
results = manager.execute("Some query")

# Shutdown (if necessary)
manager.shutdown()
```

---

### Adding a New Extension

To add a new extension:

1. Create a new directory under `extensions/`.
2. Implement the extension's functionality in a Python script, ensuring it adheres to the `ExtensionInterface`.
3. If the extension requires any resource files, place them in a `resources/` directory within the extension's directory.
4. Update any relevant configuration or main application scripts to utilize the new extension.
