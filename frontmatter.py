import frontmatter

with open('example.md', 'r', encoding='utf-8') as f:
    post = frontmatter.load(f)

# Access metadata
print(post.metadata['title'])  # "Getting Started with AI"
print(post.metadata['tags'])   # ["ai", "machine-learning", "tutorial"]

# Access content
print(post.content)  # The markdown content without frontmatter
