# A love for food

version @1.0.0

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
	pip3 install -r requirements.txt
	python manage.py collectstatic
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver
```

## Database Settings

This app used SQLite for the database, so database settings are not required.

## Static Files

Static files are in /static/ directory.

## Templates Files

Templates files are in /template/ directory.

## Python Files

Python files are in /front/ directory.

## Uploaded images

Uploaded images are stored in /media/images/ directory.

## Structure of Project

```bash
< PROJECT ROOT >
	│   .gitattributes
	│   .gitignore
	│   db.sqlite3             # sqlite file
	│   manage.py
	│   Procfile
	│   Procfile.windows
	│   README.md
	│   requirements.txt        # python libraries for this app.
	│
	├───front
	│   │   admin.py
	│   │   apps.py
	│   │   models.py            # define Recipe table
	│   │   tests.py
	│   │   urls.py              # define URLs and combine URLs and view files
	│   │   __init__.py
	│   │
	│   ├───migrations
	│   │
	│   ├───views
	│   │   │   add_recipe.py     # add recipe function
	│   │   │   custome.py        # delete and edit recipe function
	│   │   │   detail.py         # show details of one recipe
	│   │   │   index.py          # show all recipes
	│   │   │   my_recipe.py      # show all recipes that the user added.
	│   │   │   search.py
	│   │   │
	│   │   ├───auth
	│   │   │   │   login.py      # user login
	│   │   │   │   signup.py     # user sign up
	│   │   │   │
	│   │   │   └───__pycache__
	│   │   │
	│   │   └───__pycache__
	│   │
	│   └───__pycache__
	│
	├───media
	│   └───images
	│
	├───recipes
	│   │   asgi.py
	│   │   settings.py                    # main setting file of this app.
	│   │   urls.py
	│   │   wsgi.py
	│   │   __init__.py
	│   │
	│   └───__pycache__
	│
	├───static
	│   └───assets
	│       ├───css
	│       │       app.css                  # the main styles in this file.
	│       │       bootstrap.min.css
	│       │       bootstrap.min.css.map
	│       │       icons.css
	│       │       pace.min.css
	│       │
	│       ├───flags
	│       │
	│       ├───fonts
	│       │
	│       ├───images
	│       │
	│       ├───js
	│       │       add_recipe.js                # add and edit function
	│       │       app.js                       # scrolling and delete function
	│       │       auth.js                      # sign up and sign in function
	│       │       bootstrap.bundle.min.js
	│       │       bootstrap.bundle.min.js.map
	│       │       jquery.min.js
	│       │       pace.min.js
	│       │       tata.js
	│       │       tinymce.min.js
	│       │
	│       └───plugins
	│           ├───Drag-And-Drop                # plugin to drag and drop file
	│           │
	│           └───input-tags                   # plugin to input multiple words
	│
	└───templates
	        add-new.html  # template file to add and edit recipes.
	        detail.html   # template file to show details of recipes.
	        index.html    # template file to show cards of recipes.
	        layout.html   # main layout file to extend.
	        signin.html   # sign-in page template file.
	        signup.html   # sign-up page template file.
```

## Demo
[DEMO](http://143.198.187.223/)