import json
import random

# Function to generate random text for blog posts
def generate_text(post_number):
    title = f"Blog Post #{post_number}"
    content = f"This is the detailed content of blog post #{post_number}. It includes interesting insights and well-thought-out ideas."
    excerpt = f"This is the content of blog post #{post_number}."
    return title, content, excerpt

# Generate 100 blog posts
blog_posts = []
for i in range(1, 101):
    title, content, excerpt = generate_text(i)
    blog_post = {
        "id": i,
        "title": title,
        "content": content,
        "excerpt": excerpt
    }
    blog_posts.append(blog_post)

# Save the blog posts to a JSON file
output_file = "blog_posts.json"
with open(output_file, "w") as file:
    json.dump(blog_posts, file, indent=4)

print(f"Generated {len(blog_posts)} blog posts and saved to {output_file}")
