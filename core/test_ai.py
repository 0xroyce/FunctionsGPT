import sys
import openai
import json
from config import Config
from core.extension_loader import ExtensionManager
import logging

logging.basicConfig(level=logging.INFO)

# Initialize configuration
CFG = Config()
openai.api_key = CFG.openai_api_key

class AITester:
    def __init__(self):
        self.extension_manager = ExtensionManager()
        self.extension_manager.load_extensions()

        # Automatically initialize and update the available_functions based on loaded extensions
        self.available_functions = {}
        for ext_name, ext_details in self.extension_manager.extensions.items():
            ext_instance = ext_details["instance"]
            function_spec = ext_instance.function_specification()
            function_name = function_spec["name"]
            self.available_functions[function_name] = getattr(ext_instance, 'execute')
            # Initialize the extension (if it has an initialize method)
            if hasattr(ext_instance, "initialize"):
                ext_instance.initialize()

    def call_openai(self, messages, functions):
        return openai.ChatCompletion.create(
            model=CFG.smart_llm_model,
            temperature=0.1,
            messages=messages,
            functions=functions,
            function_call="auto",
        )

    def run_ai(self, input):
        messages = [{
            'role': 'system', 'content': 'Your name is Virtuoso Edge',
            'role': 'system', 'content': 'Respond using markdown',
            'role': 'user', 'content': input
        }]

        # Create a list of function specifications based on the loaded extensions
        functions = [ext_details["instance"].function_specification() for ext_name, ext_details in
                     self.extension_manager.extensions.items()]

        last_function_name = None

        while True:
            response = self.call_openai(messages, functions)
            response_message = response["choices"][0]["message"]

            if response_message["content"]:
                print(response_message["content"])

            # If OpenAI called a function
            if response_message.get("function_call"):
                function_name = response_message["function_call"]["name"]
                function_args = json.loads(response_message["function_call"]["arguments"])

                # Check if the function is in our list of available functions
                if function_name in self.available_functions:
                    function_to_call = self.available_functions[function_name]
                    function_response = function_to_call(**function_args)

                    logging.info(f"Function {function_name} executed successfully!")

                    messages.append({
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    })

                # If the function called is the same as the last one, or no new function is called, break
                if function_name == last_function_name:
                    break

                last_function_name = function_name
            else:
                # No more function calls detected, break out of the loop
                break

        return messages[-1]["content"] if messages else ""


if __name__ == "__main__":
    tester = AITester()
    tester.run_ai("How are you?")
