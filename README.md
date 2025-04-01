<p align="center">
  <img src="https://github.com/mihirkumarmistry/securevault/blob/dev/src/assets/images/logo-dark.svg" width="400" height="200">
</p>

# Securevault
**Securevault** is a secure file sharing application. It contains multiple security mechanisms, including **RBAC** (Role-Based Access Control), **AES** (Advanced Encryption Standard) for data encryption, **MFA** (Multi-Factor Authentication), and **TLS** (Transport Layer Security) for secure transmission.

# Steps to run the applications
## Prerequisites
Before setting up the project, you have the following installed:
1. Install latest version of **node** v22.13.1 or higher. [Download Node](https://nodejs.org/en/download)
2. Install Angular CLI using command. ```npm install -g @angular/cli```
3. Run backend project by following the steps mention in readme file. [BackendAPI](https://github.com/athul-narayanan/securevaultapi)

## Steps to run angular application
1. Clone [Repository](https://github.com/mihirkumarmistry/securevault.git) locally.
2. Go to project file and install dependencies using this command ```npm install --force```
3. Once all the depandancy install successfully run this command to run appllication ```npm run start```

## User Roles
This application manage three main role:
1. User: This role contains basic level of access (eg: File upload ans sharing)
2. Admin: This role has authority to create user and manage user.
3. Manager: This role is a super role in the application will all access including manage admins and users.
