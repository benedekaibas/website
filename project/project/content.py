"""File containing all the contents for my website."""

class Content():
    """Content class."""

    def __init__(self) -> None:
        pass

    def generate_index_content(self):
        return """
        # Welcome to My Quarto Website

        This is a basic website template using Quarto and Python.

        ## Section 1
        Content for section 1.

        ## Section 2
        Content for section 2.
        """

    def generate_about_content(self):
        return """
        # About Me

        This is the About Me section.
        """

    def generate_computer_science_content(self):
        return """
        # Computer Science

        This is the Computer Science section.
        """

    def generate_hungarian_thoughts_content(self):
        return """
        # My Hungarian Thoughts

        This is the My Hungarian Thoughts section.
        """
    
if __name__ == "__main__":
    content = Content()
    
    with open("index.qmd", "w") as file:
        file.write(content.generate_index_content())
    
    with open("about.qmd", "w") as file:
        file.write(content.generate_about_content())
    
    with open("computer-science.qmd", "w") as file:
        file.write(content.generate_computer_science_content())
    
    with open("hungarian-thoughts.qmd", "w") as file:
        file.write(content.generate_hungarian_thoughts_content())