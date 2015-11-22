# TesterSite

TesterSite is a simple Python/Django web application , that i've experienced REST APIs and many many other features.

  - Introduction to Django
  - make CRUD (Create,Read,Update,Delete) ability for REST(Representational State Transfers) 
  - go deeper and deeper in Python 
  - make all possible 


### Version
1.0.0

### Tech

TesterSite uses a number of open source projects to work properly:

* [Django] - full python framework
* [Ace Editor] - awesome web-based text editor
* [Marked] - a super fast port of Markdown to JavaScript
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [keymaster.js] - awesome keyboard handler lib by [@thomasfuchs]
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

You need pip installed globally:

```sh
$ pip install virtualenv virtualenvwrapper
```

```sh
$ mkvirtualenv TesterSite-venv
$ git clone [git-repo-url] TesterSite
$ pip install -r requirements.txt
$ cd TesterSite
$ ./manage.py makemigrations 
$ ./manage.py migrate
$ ./manage.py runserver
```

### Plugins

TesterSite is currently extended with the following plugins

* Dropbox
* Github
* Google Drive
* OneDrive

Readmes, how to use them in your own application can be found here:

* [plugins/dropbox/README.md] [PlDb]
* [plugins/github/README.md] [PlGh]
* [plugins/googledrive/README.md] [PlGd]
* [plugins/onedrive/README.md] [PlOd]


### Todos

 - Add thumbnails into models
 - Add account and authorization processors
 - Add some more useful packeges
 - Add REST-API for creation  & commiunication with mobile applications
- Add Heruko and deploy on 
- Add tests & code comment and some more deeper Python/Django coding


### Development

Want to contribute? Great!


License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does it's job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Django]: https://www.djangoproject.com/
   [git-repo-url]: <https://github.com/LordK1/TesterSite.git>
   [starter-template]: <https://github.com/LordK1/Starter.git>
   [@thomasfuchs]: <http://twitter.com/thomasfuchs>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [marked]: <https://github.com/chjj/marked>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [keymaster.js]: <https://github.com/madrobby/keymaster>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>
   
   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]:  <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
