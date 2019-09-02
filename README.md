## openplotter-myapp
This is a template with comments to help create apps for OpenPlotter. It should be written for python3.

### Installing

#### For production

Install [openplotter-settings](https://github.com/openplotter/openplotter-settings) and just install this app from *OpenPlotter Apps* tab.

> Your app should be aproved and added to openplotter-settings by OpenPlotter team.

#### For development

> Put here all the info needed to edit and propose changes to your app.

Install OpenPlotter dependencies:

`sudo apt install openplotter-settings python3-wxgtk4.0`

> Any OpenPlotter app needs at least openplotter-settings and python3-wxgtk4.0

Install other dependencies:

`sudo apt install foo bar`

`sudo pip install foo bar`

Clone the repository:

`git clone https://github.com/openplotter/openplotter-myapp`

Make your changes and test them:

`sudo python3 setup.py install`

Pull request your changes to github and we will check and add them to the next version of the [Debian package](https://launchpad.net/~openplotter/+archive/ubuntu/openplotter/).

> Once approved we will add your app to the OpenPlotter PPA repository. Please provide any important info necessary to create the Debian package.

### Documentation

https://openplotter.readthedocs.io

> Please add a chapter to OpenPlotter documentation with info to use your app: https://github.com/openplotter/docs

### Support

http://forum.openmarine.net/forumdisplay.php?fid=1

> Feel free to use openmarine.net forum to give support for your app.
> Thanks for contributing!!!
