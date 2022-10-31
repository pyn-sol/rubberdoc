"""
## Subpackage Two, Module One  

This Module has an explanatory docstring at the top, and then jumps right 
into the details.
"""

class TestObject:
    """
    A short description detailing the functions of TestObject.
    """
    def __init__(self):
        pass 

    def function_one(self, input: str) -> str:
        """Does a thing with the stuff.

        This function does stuff with the input.

        Args:
            input (str): any string is fine...
        Returns:
            str: Returns the `input` unaltered
        """
        print(input)
        return input
