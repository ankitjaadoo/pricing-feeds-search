# pricing-feeds-search

## Instructions to run the app
- to run the application, git clone the repo.
- run the command `pip install -r requirements.txt`
- change directory to pricing_feeds_app
- run the command `python manage.py runserver`

## Endpoints to be tested:

- `/pricing/upload/` - use the file 'myFile0.csv' provided in the repo to upload.
- `/pricing/search/` - you can search for any of the products from here.
- `/pricing/edit/<int>/` - you can edit the product details from here.