# facial-attendance-system

## Description
This project implements a **serverless face recognition attendance system** using AWS.

When an image is uploaded to an Amazon S3 bucket, an AWS Lambda function is automatically triggered to process the image, perform face recognition, and mark employee attendance without any manual intervention.

---

## Frontend (Client Side)

### Purpose
The frontend provides a simple interface for employees to upload their face images in order to mark attendance.

### Description
- Employees upload their face image from a mobile phone or desktop
- The image is directly uploaded to an Amazon S3 bucket
- No face processing happens on the frontend, ensuring security and simplicity

### Technologies Used
- HTML
- CSS
- JavaScript (or React – optional)
- Amazon S3 (for image upload)

### Frontend Upload Path
Images are uploaded to the following S3 path:



### Frontend Flow
1. Employee selects a face image
2. Image is uploaded to the S3 `uploads/` folder
3. Backend processing starts automatically via S3 trigger

---

## Backend (Serverless Architecture)

### Description
The backend is fully serverless and handles face recognition and attendance marking using AWS services.

### AWS Services Used
- **Amazon S3** – Image storage and trigger source
- **AWS Lambda** – Backend processing logic
- **Amazon Rekognition** – Face detection and recognition
- **Amazon CloudWatch** – Logs and monitoring
- **AWS IAM** – Access control and security

---

## Project Flow
1. Employee uploads image to S3 (`uploads/` folder)
2. S3 triggers the Lambda function
3. Lambda extracts employee ID from the image filename
4. Amazon Rekognition processes the image
5. Attendance is marked
6. Execution details are logged in CloudWatch

---

## Repository Structure

