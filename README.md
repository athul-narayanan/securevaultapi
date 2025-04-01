<p align="center">
  <img src="https://github.com/mihirkumarmistry/securevault/blob/dev/src/assets/images/logo-dark.svg" width="400" height="200">
</p>

# SecurevaultAPI
**Securevault** is a secure file sharing application. It contains multiple security mechanisms, including **RBAC** (Role-Based Access Control), **AES** (Advanced Encryption Standard) for data encryption, **MFA** (Multi-Factor Authentication), and **TLS** (Transport Layer Security) for secure transmission.

# Steps to run the applications
## Prerequisites
Before setting up the project, you have the following installed:
1. Install Docker Desktop [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Install Pgadmin 4  [Download Pgadmin 4](https://www.pgadmin.org/download/)

## Steps to run angular application
1. Clone [Repository](https://github.com/athul-narayanan/securevaultapi.git) locally.
2. Generate TLS Certificate following the below steps
   1. Generate certificate directory by running  ```mkdir certs```
   2. Generate Encrypted private key by running  ```openssl genrsa -aes256 -out django_local.key 2048```
   3. Create certificate signing request by running ```openssl req -new -key django_local.key -out django_local.csr```
   4. Enter the details according to the questionnaire
   5. Generate self signed certificate by running ```openssl x509 -req -days 365 -in django_local.csr -signkey django_local.key -out django_local.crt```
3. Add values for below properties in docker-compose.yml
   1. POSTGRES_DB - # represents name of the database (eg: securevaultdatabse)
   2. POSTGRES_PASSWORD - # 
   3. Create certificate signing request by running ```openssl req -new -key django_local.key -out django_local.csr```
   4. Enter the details according to the questionnaire
   5. Generate self signed certificate by running ```openssl x509 -req -days 365 -in django_local.csr -signkey django_local.key -out django_local.crt```

## User Roles
This application manage three main role:
1. User: This role contains basic level of access (eg: File upload ans sharing)
2. Admin: This role has authority to create user and manage user.
3. Manager: This role is a super role in the application will all access including manage admins and users.
