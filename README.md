# OpenAPI 3 + Connexion + AioHTTP tutorial

The purpose of this tutorial is to facilitate learning about the
[OpenAPI 3](https://github.com/OAI/OpenAPI-Specification/) spec +
[Connexion](https://connexion.readthedocs.io/en/latest/) +
[AioHTTP](https://aiohttp.readthedocs.io/en/latest/)
stack. And designing APIs according to the
[Google API Design Guide](https://cloud.google.com/apis/design/).
Also use of proper linting and Python formatting is encouraged through a pre-commit hook.
With some knowledge of how to use a shell (Mac/Linus/Unix - I prefer
[Bash](https://www.gnu.org/software/bash/)) + [Git](https://git-scm.com/) +
[Python 3](https://docs.python.org/3/), you should be able to have
this tutorial working for you pretty quickly. The interesting part of this tutorial is that there
are [Pytests](https://docs.pytest.org/en/latest/) for each step. This also works to demo
test driven development. Each part of the tutorial has a different pytest file and a
corresponding [Makefile](https://www.gnu.org/software/make/manual/html_node/Introduction.html)
entry to make running it simple. Answers for each step in the tutorial are included in different
Git branches named for the step.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisite Software

Install [Docker for Mac](https://docs.docker.com/docker-for-mac/install/) by following their
instructions.

Install [Homebrew](https://brew.sh/) which is a package manager for Mac that helps you install
other things.

This project uses Python 3.7.3. I recommend using [Pyenv](https://github.com/pyenv/pyenv) to
manage Python version needed for different projects. You can install it via Homebrew:

```bash
brew install pyenv
```

You'll need to follow that up by telling Pyenv to install Python 3.7.3 like:

```bash
pyenv install 3.7.3
```

### Setup

First fork this project to your own `github.com` account. Then clone the project locally.

Once the project is cloned to your computer, dependencies must be setup. Python dependencies should
always be managed in a virtualenv.
[Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) is the recommended
tool to help with this. To get a version of Virtualenvwrapper that works with Pyenv run:

*Note*: If using `zsh` (or other) shell replace `.bashrc` with `.zshrc` (or the appropriate
equivalent).

```bash
brew install pyenv-virtualenvwrapper
echo export PYENV_VIRTUALENVWRAPPER_PREFER_PYVENV="true" >> ~/.bashrc && source ~/.bashrc
pyenv virtualenvwrapper
```

Change into the directory to where you cloned this project (if you haven't already):
```bash
cd tutorial-openapi-aiohttp
```

Now create & setup your virtualenv like:

```bash
make venv
workon tutorial-openapi-aiohttp
```

### Running the AioHTTP server

If you can get the AioHTTP server running, then you know your environment is setup correctly for
the rest of the tutorials.

This project requires some environment variables to work properly.
The easiest way to manage these is by creating using [direnv](https://direnv.net/). Then you can
simply add them to a `.envrc` file in the root of your repo.

Install direnv with the command:

```bash
brew install direnv
```

You then need to create a `.envrc` file in the root of the project with the following lines:

```bash
export PYTHONPATH=`pwd`
# If you use virtualenvwrapper, the following line is also helpful
source $WORKON_HOME/tutorial-openapi-aiohttp/bin/activate
```

After the `.envrc` file is created with the correct values, allow direnv to setup the env:

```bash
cd `pwd`
direnv allow
```

After the env variables are set, start up your docker services with:

```bash
make docker
```

After the docker containers start up, you can run the app like:

```bash
make run
```

*Note* This will run your server in the foreground and monopolize the shell until you `CTRL+C`.

Then you can test the API by using `curl` in a new shell:

```bash
curl -v "http://127.0.0.1:9000/"
```

If you go to the URL in your browser, it will redirect you back to the Github project + README.

While the app is running, you can also view the local Swagger UI docs by opening your browser
to [localhost/ui](http://127.0.0.1:9000/ui/).

Once you are finished exploring, you can safely `CTRL+C` to shut down the web server.

### Running the tests

There are pytests which validate that you've correctly completed each step in this tutorial.
You can run the tests by executing:

```bash
make tests
```

The first time your run this all the tests will fail. This is expected. You'll be doing the
work in this tutorial to get the tests working.

### Before committing code

Finally, we want to setup githooks to encourage quality usage of Python. You can do this with:

```bash
make githooks
```

## Passing the tests

Each of the tests will require a few steps to get it working. First, you should modify `index.yaml`
inside the `spec` folder. Each test will require adding new yaml under the `paths` directive.
In addition, for test #2 you should add a new item under the `components:schemas` for the Kudo
object which will be reused in tests #3 & #4.

### Test 1 - Hello World

To get test 1 passing you'll need to do a few items:
* Update index.yaml. You can look at the included `/` path as an example.
    1. Add a `/hello-world` route to the index.yaml
    2. Add a GET method to the route with a summary and description.
    3. Add a combination of `x-openapi-router-controller` (*optional*) and `operationId` (*required*)
        attributes pointing to your function. Don't worry too much about the Google API Design
        Guide on this one.  It's just a 'Hello World'.
    4. Add a 200 response and description.
* Create your new handler file & function. You can look at `handlers/root.py` and
    [AIOHTTP docs](https://aiohttp.readthedocs.io/en/latest/web_quickstart.html#handler) to
    figure this part out. You *MUST* return a JSON object with a single key of `"Hello"` and it's
    corresponding value set to `"World"`.
* After these changes, you can test your code. If you wish, you may use `make run` and hit your
    endpoint to see the results, or you can use the Makefile via `make test_1`.
