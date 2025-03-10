# migr-AI-tion

migr-AI-tion aims to educate users on how "truth" is created using data, and to provide new possibilities for self-representation for migrants, whose stories are not heard in the mainstream media

![alt text](figma/blogpostPhoto/Screenshot%202021-02-11%20at%2012.43.15.png)

Social inequalities are being reinforced and propagated by the economic operations of the tech industry, specifically in the ways that data is scraped and trained for AI technologies. The blind trust that is placed in software to provide "objective" judgements creates problematic divisions between those who can shape knowledge, and those who are tracked, silenced, and exploited to develop technologies for First World users. This problem, data colonialism, recalls a European colonial tradition, wherein a scientific, 'objectivist' rationale was provided for the colonization of 'other' groups. To address data colonialism, we decided to implement a data literacy project, to educate users on how "truth" is created using data, and to provide new possibilities for self-representation for migrants, whose stories are not heard in the mainstream media. For this project, we decided to focus on how experiences of migrants could be incorporated into a computer vision dataset. 

---

## Table of Contents

- [Features](#features)
- [Installation Backend](#installation-backend)
- [Features Backend](#features-backend)
- [Installation Frontend](#installation-frontend)
- [Features Frontend](#features-frontend)
- [Author Info](#author-info)

---

## Features

Computer vision is a wide field, but one of the classic, first achievements of computer vision was the classification of objects present in images. This particular task is also known for its bias, a subgroup of classification algorithms can detect faces, but are significantly less efficient with people of color. While some of these biases have been addressed, there remain fundamental problems with computer vision. Firstly, it often continues to show a bias in favor of the Global North.  Secondly, people often misconceive how effective AI actually is at detecting and recognizing. We needed to bring more public understanding to the magical, "black box" AI. To do this, we implemented 3 features:

1. **Image upload** - The image upload features allows users to upload an image and to tag and create a caption for that image. Once the data has been submitted, users are able to compare their tags with ImageNet AI tags.

2. **Image view -** The image view feature allows users to search for images via 'tags' of their interest. Viewers are able to view all images related to a certain tag on a sliding carousel, and all tags assigned to a particular image. ImageNet AI tags are again available for making comparisons. 

3. **Data visualisation -** On the home page, users are able to see the network relations of tags and the frequency by which a certain tag has been submitted. This gives the user a general idea of what aspects of the migration experience are considered important by migrants themselves.


---

## Installation Backend

### Pull files from GitHub
Create a new folder "migr-AI-tion" for this project on your computer.
Than open the GitBash with the right click on the folder sign and use following commands to pull the files from GitHub. *Also pull before you start working on files, which you work on together with others. So you use the latest version of the files.*

```bash
git clone
```
```bash
git status
```
```bash
git checkout main
```
```
git pull
```
### Push changes to GitHub
First create a new branch, so you don't push to the main branch. Than switch to the branch and commit your changes.
```bash
git branch <branchname>
```
```bash
git checkout <branchname>
```
```bash
git status
```
```bash
git add .
```
```bash
git commit -m "<message/changes>"
```
```bash
git push
```
```bash
git status
```

### Setting up infrastructure for Mac

#### 1: Setting up virtual environment 
You require an up-to-date Python 3 version (for the Image Classification version 3.4 through 3.8 are compatible) as well as `pip`. Do this only the **first** time. 
```bash
user@Users-MacBook-Pro migr-AI-tion % python3 -m venv venv
user@Users-MacBook-Pro migr-AI-tion % source venv/bin/activate
```


#### 2: Installing requirements
Please note the 'venv' addition to your terminal to ensure that you successfully set-up the virtual environment. This step needs to be repeated, if new requirements were added while working on the back-end. 
```bash
(venv) user@Users-MacBook-Pro migr-AI-tion % cd backend
(venv) user@Users-MacBook-Pro backend % pip install -r requirements.txt
```

#### 3: Starting FastAPI app
The uvicorn command starts the ASGI app which is located in the src folder. 
```bash
(venv) user@Users-MacBook-Pro backend % cd src
(venv) user@Users-MacBook-Pro src % uvicorn main:app --reload
```
If you encounter the following error, you have to create a new folder in the backend called /images. 
```bash
RuntimeError: Directory 'images' does not exist
```
For that you have to quit the app by pressing `CTRL+C` and create the directory 'images'. 
```bash
(venv) user@Users-MacBook-Pro src % mkdir images
(venv) user@Users-MacBook-Pro src % uvicorn main:app --reload
```

#### 4: Interacting with the app 
If successfully installed, you should see the following output in the terminal: 
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 
```
And depending with your local set-up you can interact with the API on the above seen IP. For example appending /docs to this local URL will allow you to test your created endpoints. For further information, see the documentation of [FastAPI](https://fastapi.tiangolo.com/). 

### Setting up infrastructure for Windows

#### 1: Setting up virtual environment 
You require an up-to-date Python 3 version as well as `pip`. Python 3.4 through 3.8 are compatible with the image classification algorithm. Do this only the **first** time you install the app.
```bash
C:\Users\migr-AI-tion>python -m venv venv
C:\Users\migr-AI-tion>venv\Scripts\Activate.ps1
```

#### 2: Installing requirements
Please note the 'venv' addition to your terminal to ensure that you successfully set-up the virtual environment. This might have to be repeated if new dependencies were added to the back-end. 
```bash
(venv) C:\Users\migr-AI-tion>cd backend
(venv) C:\Users\migr-AI-tion\backend>pip install -r requirements.txt
```

#### 3: Starting FastAPI app
The uvicorn command starts the ASGI app which is located in the src folder. 
```bash
(venv) C:\Users\migr-AI-tion\backend>cd src
(venv) C:\Users\migr-AI-tion\backend\src>uvicorn main:app --reload
```
If you encounter the following error, you have to create a new folder in the backend called /images. 
```bash
RuntimeError: Directory 'images' does not exist
```
For that you have to quit the app by pressing `CTRL+C` and create the directory 'images'. 
```bash
(venv) C:\Users\migr-AI-tion\backend\src>mkdir images
(venv) C:\Users\migr-AI-tion\backend\src>uvicorn main:app --reload
```

#### 4: Interacting with the app 
If successfully installed, you should see the following output in the terminal: 
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 
```
And depending with your local set-up you can interact with the API on the above seen IP. For example appending /docs will allow you to test your created endpoints. For further information, see the documentation of [FastAPI](https://fastapi.tiangolo.com/).



---

## Features Backend

#### 1. Endpoints
Two endpoints in total, one for images and one for tags:

1. **"images endpoint" includes a 'post-method' and a 'get-method'** -The 'post-method' reads the image and validates if the image consists of an acceptable file ("jpg", "jpeg", "png", "JPEG", "PNG"), is not truncated and whether the PIL library recognizes it as an image and, if validated, saves the image, its caption as well as its newly created unique id in the data table "images". This method also validates if the inserted tags already exist in the table "tags" and, if they are new, adds them to this data table, whilst querying the tag-ids already present and adding new ids for tags not yet present. Also, the unique ids of the image and the tag(s) are saved in "images_tags", linking tags to images. Furthermore, the image is passed to the MobileNetV2 architecture pre-trained with ImageNet weights and 1000 possible tags. The results are stored in the ai_tags table. Which cannnot be queried by itself, as it will be queried only in relation to the get-image endpoint to which it is related. 
The 'get-method' retrieves a list of all images in the database "images". As the tables ai_tags and tags are related through Foreign Keys, tags and ai_tags are also returned for every image. Currently no pagination is implemented, as there the inteded current use as a documentary project with few users does not require this. However, this feature might be added later.  

2. **"tags endpoint" includes two 'get-methods'** - The 'get-method' retrieves a list of all tags in the database "tags". While the tag/network endpoint returns two lists, one with nodes of the network graph for the homepage (all the tags and counts of their occurence). The edge array returns connections between tags and their values. 

#### 2. Data bases
Four tables in total, currently using SQLite but will/might change to PostgreSQL.

1. **"images"** - including 'id' and 'caption'
2. **"tags"** - including 'id' and 'tag'
3. **"images_tags"** - including 'tag_id' and 'image_id'
4. **"ai_tags"** - including 'id', 'image_id', 'tag' and 'confidence'

![alt text](/figma/blogpostPhoto/entity_relationship_diagram.png)


#### 3. AWS Deployment
(no details here yet, still has to be done and updated later)

---

## Installation Frontend

After the backend is set and running a frontend set-up is needed to be able to load the app in the local host. [Create React App](https://github.com/facebook/create-react-app).

### 1: Installing required dependencies

Please open a new terminal in the project directory without closing the previous terminal for backend set-up.

#### For Mac
```bash
user@Users-MacBook-Pro migr-AI-tion % cd frontend
user@Users-MacBook-Pro frontend % npm install
```

#### For Windows
```bash
C:\Users\migr-AI-tion> cd frontend
C:\Users\migr-AI-tion\frontend> npm install
```

### 2: Available Scripts

Once all the dependencies are installed in the project directory, you can run:

#### For Mac
```bash
user@Users-MacBook-Pro frontend % npm start
```

#### For Windows
```bash
C:\Users\migr-AI-tion\frontend> npm start
```

##### `npm start`
Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.


---


## Features Frontend
The MVP consists of 4 main features. Which are:
#### 1: Data Visualisation
Once the page is loaded, a data visualisation in the form of a network graph should be visible. The user should be able to interact with the graph and on hover it will show words representing tags of images available in the database. Whenever a user upload a new post (consisting of an image, a caption and tags) into the database, it will automatically be implemented to the net. So with a new tag input there will be a new branch on the net to be seen.

#### 2: Upload Function
User should be able to upload an image with format .png or .jpg, input tags and also caption and then upload them as a post into the backend system. The image can then be found in the Gallery page when user searches for a certain tag.

#### 3: Searchbar Function
User should be able to type any query into the search bar and when the 'enter' key or the magnifying glass icon is pressed, a result of images related to the query should appear. The string will be matched partially in the tags database. 

#### 4: Carousel Display
The result images will be presented in form of a sliding carousel. In the carousel, the information about the image uploaded will then be visible. The carousel consists of arrows to slide, a card box to contain the image information, and dots  as the indicator of page. The information provided in the carousel will be the image itself, the tags and caption inputed by the user, the tags results detected by the AI, and the confidence level of how high is the match level of the tags output by AI.

---

## Author Info
For futher information you can contact: 

Jie Liang Lin /// Web /// 

Btari Galuh Chandraditya /// Web /// @btarigaluh

Thanh Tung Ha Thuc (Tony Ha) /// Data /// 

Michèle Fischer /// Data /// 

Margit Hain /// Data /// @CodeGitte

Paul Bochtler /// AI /// @datapumpernickel

Sofia Fontenla /// UX ///

Nuno Moreira /// UX /// 
