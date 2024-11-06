"""File containing all the contents for my website."""

class Content():
    """Content class."""

    def __init__(self) -> None:
        pass

    def generate_content(self):
        return """
        # Welcome to My Quarto Website

        This is a basic website template using Quarto and Python.

        ## Section 1
        Content for section 1.

        ## Section 2
        Content for section 2.
        """
    
if __name__ == "__main__":
    content = Content().generate_content()
    with open("index.qmd", "w") as file:
        file.write(content)
