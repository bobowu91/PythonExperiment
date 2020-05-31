# PythonExperiment
Learning Python with Git version control

git clone <git repo url>
git add <filename.py> | add . (for all updates)
git commit -m "type some info here"
git push

On Atom:

In atom we can run python scripts in different python versions by creating a new
profile in script run by hitting shift + command +i. Simply locate the version of
the python you want to use by running 'echo $PATH' and copy the the directory to
the command field. When we want to run the python file in Atom, hit shift + command + k
and select the profile.

when quitting Python, there are two ways.
1. hit command + q
2. click the top left red button

the first option shun down the program completely and restart the program will
automatically take us to the previous project states. A project state is a meta
data used to keep track some information about our folder, like our run options.

the second option close the current working window only. when we restart the program,
a new window will be created and all previous state are not recovered. 

On Python:

when we need to install python packages for different python versions or check
the installed version of a package or get info of a particular package under
certain python version, we can use pip followed by its version. For example,
pip3.6 or pip3.8. Currently I have 4 versions of Python{2.7, 3.6, 3.7, 3.8}
