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

## Deployment steps:
1. Install AWS Elastic Beanstalk CLI: `pip install awsebcli`
2. Initialize Elastic Beanstalk Application: `eb init -p python-3.9.13 pricing-manager --region us-west-2`
3. Create an Environment and Deploy: `eb create pricing-manager-env eb deploy`
4. Set Up Static Files (if using S3) within settings.py: 

'''
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# For S3
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
'''