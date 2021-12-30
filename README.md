# Face Attendance/Identity Project (Server-side)

The following repository is the server-side application of the Face Attendance/Identity Project. This project handles the data management process such as the update, delete, and creation process of face identity. On the other hand, this will also return all lists of existing faces in the database and along with is encoded points and details such as name and id.

Furthermore, the server-side can manage image data that is stored in the AWS S3 bucket. For every update request to a specific face identity, will update its image data in S3. The same functionality will happen for the deletion process of face identity.

Below is a system diagram that is more or less described how the system works and how the architecture is being structured:

![FaceIdentityProject drawio](https://user-images.githubusercontent.com/61646199/147730210-25c12ff7-9ad2-4240-a2a5-a7c9c2424a30.png)

## How to use the API?

You are required to create a **.env** file that will store your Django secret key and **having an AWS account is a prerequisite** as you create your S3 bucket, access key, and its secret key. Below is the sample of content that should be put inside the **.env** file: 

```
DJANGO_SECRET=Replace_it_with_your_django_secret_key
AWS_SECRET_KEY=Replace_it_with_your_aws_secret_key
AWS_ACCESS_KEY=Replace_it_with_your_aws_access_key
AWS_REGION=Replace_it_with_your_aws_region
AWS_BUCKET_NAME=Replace_it_with_your_aws_s3_bucket_name
```

### Install packages:

Before running the program, you are required to install its dependencies. However, since the virtual environment is utilised for this project to python version consistency please run the following command in your terminal window, the current location of the terminal is located in the current directory.  The command below will activate the virtual environment for this project.

```
source venv/bin/activate
```

After activating the virtual environment, run the following commands to install all dependencies specified in the requirements.txt file.

```
pip install -r requirements.txt
```

### Running the Django server:

Finally to run your Django server, type the following command to run the server locally in port 8000.

```
python manage.py runserver
```



