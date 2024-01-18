<!-- DO NOT REMOVE - contributor_list:data:start:["MuhammadSaadSiddique", "YousraMashkoor", "OneebKhan", "Jaweria-B"]:end -->
## Setup your Backend Environment

navigate to backend folder and run the following commands
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Setting DB Credentials

> touch .env
```
export DB_USER=yous-user-name

export DB_PASSWORD=your-pwd

export DB_HOST=localhost

export DB_NAME=quranicsci-db
```

## Run the backend server

> python manage.py runserver

## Setup the frontend

Before installing the dependencies and starting the server make sure you are using ```nvm```. This enables you to use different node versions without having to uninstall and reinstall node. The reason for using nvm is to avoid conflict in package versions and reduce changes made to package-lock.json. 

For help in installing nvm on your specific device reference the following [article](https://www.freecodecamp.org/news/node-version-manager-nvm-install-guide/)

After installing nvm run the following commands

```
nvm install 20.10.0
nvm use 20.10.0
```

Navigate to frontend folder and run the following commands to install the dependencies
```
npm install
```

## Run the frontend server

> npm run start

## Before making a pull request

- ### Create a build (frontend only)
	Make sure before you make a pull request to build the project using the following command
	```
	npm run build
	```
	If the build fails, fix the code causing the build to fail and then make the pull request.


# [Join Discord server for discussion](https://discord.gg/kWJjnFW3eK)

<!-- prettier-ignore-start -->
<!-- DO NOT REMOVE - contributor_list:start -->
### 👥 Contributors


- **[@MuhammadSaadSiddique](https://github.com/MuhammadSaadSiddique)** 

- **[@YousraMashkoor](https://github.com/YousraMashkoor)** 

- **[@OneebKhan](https://github.com/oneebkhan)** 

- **[@Jaweria-B](https://github.com/Jaweria-B)** 

<!-- DO NOT REMOVE - contributor_list:end -->
<!-- prettier-ignore-end -->
