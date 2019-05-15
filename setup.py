from setuptools import setup, Command
import datetime
import gettext
import os
import platform
import site

gettext.install('mkvresizer', 'mkvresizer/locale')

class Doxygen(Command):
    description = "Create/update doxygen documentation in doc/html"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Creating Doxygen Documentation")
        os.system("""sed -i -e "41d" doc/Doxyfile""")#Delete line 41
        os.system("""sed -i -e "41iPROJECT_NUMBER         = {}" doc/Doxyfile""".format(__version__))#Insert line 41
        os.system("rm -Rf build")
        os.chdir("doc")
        os.system("doxygen Doxyfile")
        os.system("rsync -avzP -e 'ssh -l turulomio' html/ frs.sourceforge.net:/home/users/t/tu/turulomio/userweb/htdocs/doxygen/mkvresizer/ --delete-after")
        os.chdir("..")

class Procedure(Command):
    description = "Create/update doxygen documentation in doc/html"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(_("New Release:"))
        print(_("  * Change version and date in version.py"))
        print(_("  * Edit Changelog in README"))
        print("  * python setup.py doc")
        print("  * mcedit locale/es.po")
        print("  * python setup.py doc")
        print("  * python setup.py install")
        print("  * python setup.py doxygen")
        print("  * git commit -a -m 'mkvresizer-{}'".format(__version__))
        print("  * git push")
        print(_("  * Make a new tag in github"))
        print("  * python setup.py sdist upload -r pypi")
        print(_("  * Create a new gentoo ebuild with the new version"))
        print(_("  * Upload to portage repository")) 

class Uninstall(Command):
    description = "Uninstall installed files with install"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if platform.system()=="Linux":
            os.system("rm -Rf {}/mkvresizer*".format(site.getsitepackages()[0]))
            os.system("rm /usr/bin/mkvresizer")
            os.system("rm /usr/share/man/man1/mkvresizer.1")
            os.system("rm /usr/share/man/es/man1/mkvresizer.1")
        else:
            print(_("Uninstall command only works in Linux"))

class Doc(Command):
    description = "Update man pages and translations"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        #es
        os.system("xgettext -L Python --no-wrap --no-location --from-code='UTF-8' -o locale/mkvresizer.pot *.py mkvresizer/*.py")
        os.system("msgmerge -N --no-wrap -U locale/es.po locale/mkvresizer.pot")
        os.system("msgmerge -N --no-wrap -U locale/fr.po locale/mkvresizer.pot")
        os.system("msgfmt -cv -o mkvresizer/locale/es/LC_MESSAGES/mkvresizer.mo locale/es.po")
        os.system("msgfmt -cv -o mkvresizer/locale/fr/LC_MESSAGES/mkvresizer.mo locale/fr.po")

        for language in ["en", "es", "fr"]:
            self.mangenerator(language)

    def mangenerator(self, language):
        """
            Create man pages for parameter language
        """
        from mangenerator import Man
        if language=="en":
            lang1=gettext.install('mkvresizer', 'badlocale')
            man=Man("man/man1/mkvresizer")
        else:
            lang1=gettext.translation('mkvresizer', 'mkvresizer/locale', languages=[language])
            lang1.install()
            man=Man("man/{}/man1/mkvresizer".format(language))
        print("  - DESCRIPTION in {} is {}".format(language, _("DESCRIPTION")))

        man.setMetadata("mkvresizer",  1,   datetime.date.today(), "Mariano Muñoz", _("Change files and directories owner and permissions recursively."))
        man.setSynopsis("""usage: mkvresizer [-h] [--version] [--insert | --generate] [--user USER]
                   [--port PORT] [--host HOST] [--db DB] [--output OUTPUT]
                   [--format {PDF,ODT}]""")
        man.header(_("DESCRIPTION"), 1)
        man.paragraph(_("This app has the following mandatory parameters:"), 1)
        man.paragraph("--insert", 2, True)
        man.paragraph(_("Inserts a directory with movies with the index of the last directory numeric name."), 3)
        man.paragraph("--generate", 2, True)
        man.paragraph(_("Generates the movie collection document"), 3)

        man.paragraph(_("Postgresql database connection parameters:"), 1)
        man.paragraph("--user", 2, True)
        man.paragraph(_("User of the database. By default 'postgres'." ), 3)
        man.paragraph("--port", 2, True)
        man.paragraph(_("Database port. By default '5432'"), 3)
        man.paragraph("--host", 2, True)
        man.paragraph(_("Database server. By default '127.0.0.1'."), 3)
        man.paragraph("--db", 2, True)
        man.paragraph(_("Database name. By default 'mkvresizer'."), 3)
        man.paragraph("--output", 2, True)
        man.paragraph(_("Path where the movie book it's going to be generated. You can use this parameter as many times as you want."), 3)
        man.paragraph("--format", 2, True)
        man.paragraph(_("You can choose PDF or ODT arguments. PDF is used by default."), 3)

        man.header(_("EXAMPLES"), 1)
        man.paragraph(_("Insert movies with index 23"), 2, True)
        man.paragraph("mkvresizer --insert /path/to/my/movies/23", 3)
        man.paragraph(_("This command insert in database all movies (up to 6) in 23 directory. Each film must have it's cover with the same filename."), 3)
        man.paragraph(_("Generate a book with all movies in the database"), 2, True)
        man.paragraph("mkvresizer --generate --output /home/user/mymoviecollection.pdf", 3)
        man.paragraph(_("This command generates a movie book in the output path."), 3)
        man.save()



class Compile(Command):
    description = "Fetch remote modules"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import datetime
        print ("Copying libmanagers.py anc connection_pg from Xulpymoney project")
        os.chdir("mkvresizer")
        os.remove("libmanagers.py")
        os.system("wget https://raw.githubusercontent.com/turulomio/xulpymoney/master/xulpymoney/libmanagers.py  --no-clobber")
        os.system("sed -i -e '3i ## THIS FILE HAS BEEN DOWNLOADED AT {} FROM https://github.com/Turulomio/xulpymoney/xulpymoney/libmanagers.py.' libmanagers.py".format(datetime.datetime.now()))

    ########################################################################


## Version of modele captured from version to avoid problems with package dependencies
__version__= None
with open('mkvresizer/version.py', encoding='utf-8') as f:
    for line in f.readlines():
        if line.find("__version__ =")!=-1:
            __version__=line.split("'")[1]


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

if platform.system()=="Linux":
    data_files=[('/usr/share/man/man1/', ['man/man1/mkvresizer.1']), 
                ('/usr/share/man/es/man1/', ['man/es/man1/mkvresizer.1'])
               ]
else:
    data_files=[]

setup(name='mkvresizer',
    version=__version__,
    description='Generate your own personal movie collection book',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: System Administrators',
                 'Topic :: System :: Systems Administration',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Programming Language :: Python :: 3',
                ],
    keywords='movie collection book',
    url='https://github.com/Turulomio/mkvresizer',
    author='Turulomio',
    author_email='turulomio@yahoo.es',
    license='GPL-3',
    packages=['mkvresizer'],
    entry_points = {'console_scripts': ['mkvresizer=mkvresizer.mkvresizer:main',
                                       ],
                   },
    install_requires=['colorama','setuptools', 'enzyme'],
    data_files=data_files,
    cmdclass={ 'doxygen': Doxygen,
               'doc': Doc,
               'uninstall': Uninstall,
               'procedure': Procedure,
               'compile': Compile,
             },
    zip_safe=False,
    include_package_data=True
    )

_=gettext.gettext#To avoid warnings
