"""File containing all the contents for my website."""

class Content():
    """Content class."""

    def __init__(self) -> None:
        pass


    def generate_about_content(self):
        return """
---
title: "Benedek Kaibas"
about:
  id: hero-heading
  template: solana
  image: profile.jpg
  links:
    - icon: linkedin
      text: LinkedIn
      href: https://www.linkedin.com/in/kaibas-benedek-222644a5/
    - icon: github
      text: Github
      href: https://github.com/benedekaibas
---

:::{#hero-heading}

I am a student-athlete at Allegheny College studying computer science and competing in tennis. I am also a research assistant.

## Education

Allegheny College, Meadville | Meadville, PA
BA in Computer Science | Sept 2022 - June 2026

Allegheny College, Meadville | Meadville, PA
BA in Economics | Sept 2022 - June 2026

## Experience

Allegheny College | Computer Science Research Assistant | September 2024 - present

Allegheny College | Technical Leader | January 2024 - present

:::

### Thanks for visiting my page 🙏
        """

    def generate_computer_science_content(self):
        return """
---
title: "Computer Science"
---

This is the Computer Science section.
        """

    def generate_hungarian_thoughts_content(self):
        return """
---
title: "My Hungarian Thoughts"
---

This is the My Hungarian Thoughts section.
        """


if __name__ == "__main__":
    content = Content()
    
    with open("about.qmd", "w") as file:
        file.write(content.generate_about_content())
    
    with open("computer-science.qmd", "w") as file:
        file.write(content.generate_computer_science_content())
    
    with open("hungarian-thoughts.qmd", "w") as file:
        file.write(content.generate_hungarian_thoughts_content())
