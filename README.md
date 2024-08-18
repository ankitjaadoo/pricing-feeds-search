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

- STATIC_URL = '/static/'
- STATIC_ROOT = os.path.join(BASE_DIR, 'static')

- For S3
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

### Important Design Decisions
Before diving into the code, let's discuss some key design decisions for this application:

1. Database Design:

- Schema: Define tables for Store, Product, and PriceHistory. Consider using composite keys or foreign keys to link tables.
- Indexing: Ensure proper indexing on fields like Store ID, SKU, Product Name, and Date for optimized search queries.
- Database Choice: Use a relational database like PostgreSQL to handle complex queries and large datasets efficiently.

2. Scalability:

- Database Sharding/Partitioning: If the database grows large, consider sharding or partitioning by country or store ID.
- Load Balancing: Use load balancers to distribute incoming traffic across multiple server instances.

3. Data Validation:

- Validate the uploaded CSV files for correct formatting and data integrity before persisting them in the database.

4. Concurrency Handling:

- Implement locks or use optimistic concurrency control to handle multiple users editing the same records simultaneously.

5. Security:

- Secure endpoints with authentication and authorization.
- Implement data encryption for sensitive information.
- Use HTTPS to secure data in transit.

6. Deployment:

- Consider containerizing the application using Docker for easier deployment and scaling.
- Use CI/CD pipelines for automated testing and deployment.

7. Logging and Monitoring:

- Integrate logging for tracking errors, and user activity, and monitoring performance.
- Use tools like Prometheus and Grafana for real-time monitoring and alerting.