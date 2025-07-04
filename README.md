# 📚 Mantap Bookstore

**Mantap Bookstore** is a cloud-deployed Django web application that simulates a modern online bookstore. The platform supports essential e-commerce features such as user authentication, book listings, ordering, payments, and role-based access control for customers, sellers, and admins.

---

## 🌟 Key Features

- 🛍️ **Book Catalog & Slider Promotions**  
  Users can browse books and view promotional sliders on the homepage.

- 👥 **User Roles & Authentication**  
  - Customers: View and purchase books  
  - Sellers: Upload books, manage orders  
  - Admin: Manage users, books, payments

- 🛒 **Order & Payment System**  
  Includes order creation, payment tracking, and order status updates.

- 📦 **File Uploads & Media Management**  
  Supports book cover image uploads and promotional media.

---

## ☁️ AWS Integration Overview

Mantap Bookstore is fully hosted on **Amazon Web Services (AWS)** using Infrastructure as Code (IaC) with CloudFormation templates.

### 🔧 Infrastructure Components

- **Amazon EC2**  
  Hosts the Django web app in private subnets behind a bastion host.

- **Amazon RDS (MySQL)**  
  Stores application data securely with encryption and private access.

- **Amazon S3 + CloudFront**  
  Hosts and distributes static and media files globally with high availability.

- **Application Load Balancer (ALB)**  
  Routes traffic to EC2 instances and supports auto scaling.

- **Auto Scaling Group**  
  Ensures high availability and scales instances based on demand.

- **IAM Roles & Instance Profiles**  
  Secure access between services (e.g., EC2 to S3, EC2 to RDS).

- **CloudWatch & CloudTrail**  
  Monitors application metrics and logs API events for auditing.

---

## 🔐 Security Highlights

- **Encrypted RDS & S3 Buckets**  
  Protects sensitive data at rest.

- **Strict Security Groups**  
  Controls traffic between public and private resources.

- **CloudTrail Logging**  
  Tracks all API activity and changes in AWS.

- **IAM Least Privilege**  
  Follows best practices for secure service interactions.

> 🔒 **Note:** HTTPS and AWS WAF are not enabled due to sandbox environment limitations.

---

## 🖼️ Screenshot Suggestions for Report

- Dashboard view of CloudTrail logs  
- EC2 instance attached to Auto Scaling Group  
- CloudWatch metrics for EC2 or RDS  
- Screenshot of your Django homepage  
- S3 bucket and CloudFront configuration  
- RDS DB connection confirmation

---

## 📌 Summary

Mantap Bookstore demonstrates a secure and scalable deployment of a web application using Django and AWS services. It showcases key cloud architecture principles, including isolation, automation, scalability, and monitoring—all integrated using Infrastructure as Code.

