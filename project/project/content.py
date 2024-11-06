"""File containing all the contents for my website."""

class Content():
    """Content class."""

    def __init__(self) -> None:
        pass

    def generate_index_content(self):
        return """
        ---
        title: "Home"
        ---

        # Welcome to My Website

        ## About Me
        I am a passionate developer with interests in various fields of computer science. 
        [Read more](about.qmd)

        ## Computer Science
        I have worked on numerous projects involving algorithms, data structures, and software engineering principles.
        [Read more](computer-science.qmd)

        ## My Hungarian Thoughts
        I often share my thoughts and experiences related to Hungarian culture and language.
        [Read more](hungarian-thoughts.qmd)
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