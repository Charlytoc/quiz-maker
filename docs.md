<style>
    body {
        color: #d8c4c4;
    }
    .blue {
        color: #1e8a9b;
        font-weight: bold;
    }
    .title {
        background: #000;
        display: block;
        text-align: center;
        padding: 5px
    }
    .rose {
        color: #f6005a;
        font-weight: bold;
    }
    .white {
        color: #fff;
        font-weight: bold;
    }
    .center {
        text-align: center;
        display: block;
    }
</style>

# <span class="blue title">Building a Django API</span>

## <span class="white center">Setting the environment</span>

## <span class="rose">**Install Python**</span>
The first thing to keep in mind is that Django works with Python, for that reason it is necessary to have Python in the computer.
> Remember to mark the option <span class="rose">add to path</span>
***
## <span class="rose">**Create a new directory for the project**</span>
To create a new directory, go to the command line and paste the command:
```
mkdir <directory-name>
```
Where **directory-name** is how you want to name the folder where the project is in.
***
## <span class="rose">**Init a virtual environment**</span>
To initialize a new virtual environment in Python, go to the directory previusly created and open the CLI (Command Line Interface) and run the command:
```
py -m venv venv  
```
A new directory called venv will be created in the directory.
***
## <span class="rose">**Get inside the venv**</span>
To get inside the venv you need to run another command, this command will ensure you're installing all modules inside the environment
```
venv\Scripts\activate
```
Run it in Powershell
## <span class="rose">**Install Django**</span>
To install Django it is as simple as run a command in the current directory
```
pip install django 
```
Once installed, you can check if all is correct running 
```
django-admin --version
```
It will shows you the django-admin version.

## <span class="white center">Initializing empty project</span>
Now that we have completed the setting of the environment, we need to start our project with Django.

## <span class="rose">**Init project**</span>
In django, we have a command to start a new project, it is so simple, you just need to be in the current directory and run:
```
django-admin startproject <project-name> .
```
Change **project-name** with the desired project-name.
The point is to tell django to install the required files in the current directory.

## <span class="rose">**Init app**</span>
Now that we have a project, we need to add modules to that project, in django, that modules are called app, for example, an app can manage the authentication of the users, another app to manage a part of the project, and in that way we can have all our project in different modules. To start a new app, run:
```
python manage.py startapp <app-name>
```
This will create a new app in the current directory, but it is more easy to read if we have our app inside the project, for that reason, just move the **app** inside the **project** folder
```
mv app-name/ project/
```
Now, we need to change the name in **project/app/apps.AuthConfig.name** from **app** to **project.app** depending of the name of the project and app, in this example:
```
class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.authenticate'
```

## <span class="rose">**Register app**</span>
To register the app in the project, we need to add it in settings.py.INSTALLED_APPS, for our example:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.authenticate'
]
```
## <span class="rose">**Time to test if everything is correct**</span>
Run the command to up the project:
```
python manage.py runserver
```
Go to the browser in the localhost:8000m and you'll see a sample app running. But in the terminar there is an error that tells <span class="rose">You have 18 unapplied migration(s).</span>, maybe the number could be different. 

That error is caused because we need <span class="rose"> to run the migrations</span>. Run the command:

```
python manage.py migrate
```
## <span class="white center">Adding the first view</span>
In Python, we work under the arquitecture **MVT (Model, View, Template)**, where the Model is the instance in the DB (Database), the view is the function that run in a certain route, and the template is the HTML template that is shown in that route.
Keeping that in mind, the first thing we need to add in Python, is a view, just to testing, and starting to work.
I'll add a view just to say "Hello, world" to the visitor of the route.

## <span class="rose">Define the view</span>
In the app, there're a lot of files that comes with it, open views.py and add the following code:
```
from django.http import HttpResponse

def say_hello_world(request):
    return HttpResponse("Hello, world")
```
Now run the server and go to the port 8000. Notice that nothing is happening, that is because we need to register our views first.

## <span class="rose">Register the view</span>
To register the view we need to go to project/urls.py and open the file. Add the following code: 
```
from .authenticate.views import say_hello_world
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', say_hello_world, name="Hello")
]
```
We are importing the view, and adding a new path in the urlpatterns. The path receives three arguments: the route we want to assing to the view, the view itself, and a name that is an indetifier to the the view.

Now go to <span class="rose">localhost:8000/hello/</span> and see the magic.

## <span class="rose">Refactoring to be pro</span>

## <span class="white center">Saving the project in a Github repository</span>
## <span class="rose">Init the git repository</span>
```
git init
```
## <span class="rose">Add the remote</span>
```
git remote add <remote-name> <remote-url>
```
**remote-name** use to be named <span class="rose">**origin**</span> and the **remote-url** is the url of the Github repository.
If everything is correct when you run the command
```
git remote -v
```
You will see your Github repository url for fetch and push.
## <span class="rose">Ignore the modules</span>
Add a file .gitignore to ignore the modules and make our repository more easy to share.
```
touch .gitignore
```
A .gitignore file will be added to the directory, enter in the file with
```
code .gitignore
```
And at the following line:
```
#.gitignore

venv/
```
## <span class="rose">Add the changes to be stage</span>
Add all the files of our application with
```
git add .
```
## <span class="rose">Commit the changes</span>
Commit the changes that you'll be adding  to the remote repository and leave a message
```
git commit -m "a message with the changes you made"
```
## <span class="rose">Finally, upload the changes</span>
The moment of truth, upload the changes to Github
```
git push origin <branch>
```
where **branch** is the name of the current branch or the branch you want to upload the changes, in this case, the branch is <span class="rose">main<span>