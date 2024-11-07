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
---
title: "Benedek Kaibas"
about:
  id: hero-heading
  template: solana
  image: profile.jpg
  links:
    - icon: twitter
      text: twitter
      href: https://twitter.com
    - icon: github
      text: Github
      href: https://github.com
---

### This content appears above the formatted about page content.

:::{#hero-heading}

Finley Malloc is the Chief Data Scientist at Wengo Analytics. When not innovating on data platforms, Finley enjoys spending time unicycling and playing with her pet iguana.

## Education

University of California, San Diego | San Diego, CA
PhD in Mathematics | Sept 2011 - June 2015

Macalester College | St. Paul MA
B.A in Economics | Sept 2007 - June 2011

## Experience

Wengo Analytics | Head Data Scientist | April 2018 - present

GeoScynce | Chief Analyst | Sept 2012 - April 2018

:::

### This content appears below the formatted about page content.
        """

    def generate_computer_science_content(self):
        return """
---
title: "Computer Science"
---

# Computer Science

This is the Computer Science section.
        """

    def generate_hungarian_thoughts_content(self):
        return """
---
title: "My Hungarian Thoughts"
---

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