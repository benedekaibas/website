"""File containing all the contents for my website."""

class Content():
    """Content class."""

    def __init__(self) -> None:
        pass

    def generate_index_content(self):
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

Allegheny College, Meadville | Meadville, PA |
BA in Computer Science | Sept 2022 - June 2026

Allegheny College, Meadville | Meadville, PA |
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

<div class="article-container">
  <a href="article1.qmd" class="article-card">
    <h3>Article 1</h3>
    <p>Summary of article 1...</p>
  </a>
  <a href="article2.qmd" class="article-card">
    <h3>Article 2</h3>
    <p>Summary of article 2...</p>
  </a>
  <a href="article3.qmd" class="article-card">
    <h3>Article 3</h3>
    <p>Summary of article 3...</p>
  </a>
</div>

<style>
.article-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.article-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  width: 30%;
  text-decoration: none;
  color: inherit;
  transition: transform 0.3s;
}

.article-card:hover {
  transform: scale(1.05);
}
</style>
        """

    def generate_hungarian_thoughts_content(self):
        return """
---
title: "My Hungarian Thoughts"
---

<div class="article-container">
  <a href="hungarian-article1.qmd" class="article-card">
    <h3>Article 1</h3>
    <p>Summary of article 1...</p>
  </a>
  <a href="hungarian-article2.qmd" class="article-card">
    <h3>Article 2</h3>
    <p>Summary of article 2...</p>
  </a>
  <a href="hungarian-article3.qmd" class="article-card">
    <h3>Article 3</h3>
    <p>Summary of article 3...</p>
  </a>
</div>

<style>
.article-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.article-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  width: 30%;
  text-decoration: none;
  color: inherit;
  transition: transform 0.3s;
}

.article-card:hover {
  transform: scale(1.05);
}
</style>
        """

    def contact_information(self):
        return """
---
title: "Contact Information"
links:
  - icon: phone
    text: Phone Number
    href: tel:+36202298148
  - icon: email
    text: My Email
    href: mailto:kaibas01@allegheny.edu
---

# Contact Information

You can reach me via phone or email.
        """

    def generate_article_content(self, title, content_file):
        with open(content_file, 'r') as file:
            content = file.read()
        return f"""
---
title: "{title}"
---

# {title}

{content}
        """

if __name__ == "__main__":
    content = Content()
    
    with open("index.qmd", "w") as file:
        file.write(content.generate_index_content())
    
    with open("computer-science.qmd", "w") as file:
        file.write(content.generate_computer_science_content())
    
    with open("hungarian-thoughts.qmd", "w") as file:
        file.write(content.generate_hungarian_thoughts_content())
    
    with open("contact.qmd", "w") as file:
        file.write(content.contact_information())
    
    # Generate individual article files
    articles = [
        ("article1.qmd", "Article 1", "articles/content.txt"),
        ("article2.qmd", "Article 2", "articles/content.txt"),
        ("article3.qmd", "Article 3", "articles/content.txt"),
        ("hungarian-article1.qmd", "Hungarian Article 1", "articles/content.txt"),
        ("hungarian-article2.qmd", "Hungarian Article 2", "articles/content.txt"),
        ("hungarian-article3.qmd", "Hungarian Article 3", "articles/content.txt")
    ]
    
    for filename, title, content_file in articles:
        with open(filename, "w") as file:
            file.write(content.generate_article_content(title, content_file))