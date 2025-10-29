PROJECT OBJECTIVES

Set Up a New Django Project:
--> Initialize and configure a new Django project tailored for a blogging platform.
--> Establish the initial models and prepare the base templates.

Implement User Authentication:
--> Develop a comprehensive user authentication system, including registration, login, logout, and profile management.

Create Blog Post Management Features:
--> Enable CRUD (Create, Read, Update, Delete) operations for blog posts.
--> Allow authenticated users to manage their content dynamically.

Add Comment Functionality:
--> Implement a comment system to enhance interactivity, allowing users to leave and manage comments on blog posts.

Implement Advanced Features:
--> Add tagging and search functionalities to improve content organization and discoverability.

📝 Feature Documentation: Tagging and Search System
🏷️ Tagging System
Purpose: Tags allow users to categorize blog posts with keywords, making it easier to organize and discover related content.

How It Works (Developer Overview):
The Post model uses django-taggit with a tags = TaggableManager() field.
The PostForm includes a tags field using TagField, allowing users to input comma-separated tags.
Tags are saved automatically when a post is created or updated.
Tags are displayed on the post detail page using post.tags.all.
Each tag links to a filtered view (PostsByTagView) that shows all posts with that tag.

User Instructions:
When creating or editing a post, enter relevant tags in the “Tags” field.
Separate multiple tags with commas (e.g., django, webdev, tutorial).
Tags will appear below the post content once published.
Click on any tag to view other posts with the same tag.

🔍 Search System
Purpose: The search feature allows users to find posts by keywords in the title, content, or tags.
How It Works (Developer Overview):
A search bar is available in the post list or base template.
The SearchPostsView handles GET requests with a query parameter (?q=keyword).
Posts are filtered using Django’s Q objects to match the query against title, content, and tags.
Results are displayed in search_results.html.

User Instructions:
Type a keyword or phrase into the search bar (e.g., authentication, blog, comments).
Press Enter or click the search button.
Posts matching the keyword will be listed on the results page.
You can combine search with tag filtering for more precise results.

🛠 Developer Notes
Add 'taggit' to INSTALLED_APPS in settings.py.
Run python manage.py migrate after installing django-taggit.
Tag filtering URLs follow the pattern /tags/<tag_name>/.
Search queries are handled via /search/?q=keyword.

Views used:
PostsByTagView (CBV): filters posts by tag.
SearchPostsView (CBV): filters posts by keyword.