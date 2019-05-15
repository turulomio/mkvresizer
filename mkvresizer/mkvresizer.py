import os
import datetime
import shutil
import pkg_resources
import argparse
from enzyme import MKV
import gettext
import sys
from mkvresizer.version import __version__, __versiondate__
from mkvresizer.libmanagers import ObjectManager_With_IdName
from signal import signal, SIGINT

try:
    t=gettext.translation('mkvresizer', pkg_resources.resource_filename("mkvresizer","locale"))
    _=t.gettext
except:
    _=str



def signal_handler(signal, frame):
        print(_("You pressed 'Ctrl+C', exiting..."))
        sys.exit(1)


class EMode:
    Movie120m=1
    TvShow60m=2

class Mode:
    def __init__(self, id, name):
        self.id=id
        self.name=name

class ModeManager(ObjectManager_With_IdName):
    def __init__(self):
        ObjectManager_With_IdName.__init__(self)
        self.append(Mode(EMode.Movie120m, "120 minutes movie"))
        self.append(Mode(EMode.TvShow60m, "60 minutes tv show"))
        
    def print(self):
        print(_("Predefined modes available:"))
        for o in self.arr:
            print("  + {}: {}".format(o.id, o.name))

class MkvParts:
    def __init__(self, id, name):
        self.id=id
        self.name=name#name with extension

class Mkv:
    def __init__(self, filename):
        self.filename=filename
        with open(self.filename, 'rb') as f:
            self.enzyme = MKV(f).to_dict()
        print(self.enzyme['info'])
        
    def convert(self, emode):
        pass
        
    def split(self, directoryoriginal):
        for video in self.enzyme['video_tracks']:
            command="mkvextract '{0}' tracks {1}:{2}/{1}.{3}".format(self.filename, video['number']-1,  directoryoriginal, self.__codec2extension(video['codec_id']))
            print (video)
            print(command)
            os.system(command)
        for video in self.enzyme['audio_tracks']:
            command="mkvextract '{0}' tracks {1}:{2}/{1}.{3}".format(self.filename, video['number']-1,  directoryoriginal, self.__codec2extension(video['codec_id']))
            print (video)
            print(command)
            os.system(command)
        for video in self.enzyme['subtitle_tracks']:
            command="mkvextract '{0}' tracks {1}:{2}/{1}.{3}".format(self.filename, video['number']-1,  directoryoriginal, self.__codec2extension(video['codec_id']))
            print (video)
            print(command)
            os.system(command)
        
    def join(self, emode):
        output="{}.MkvResizer_mode_{}.mkv".format(self.filename[:-4], emode)
        pass

    def __codec2extension(self, type):
        if type=='S_TEXT/UTF8':
            return "srt"
        elif type=='A_AAC':
            return "aac"
        elif type=='V_MPEG4/ISO/AVC':
            return "h264"
        else:
            return "avi"
        

### MAIN SCRIPT ###
def main(parameters=None):
    signal(SIGINT, signal_handler)
    parser=argparse.ArgumentParser(prog='mkvresizer', description=_('Resizes mkv to predefined modes'), epilog=_("Developed by Mariano Muñoz 2019-{}".format(__versiondate__.year)), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('--mode', help=_('Insert films from current numbered directory'), action="store", default=1,  type=int)
    parser.add_argument('--modes', help=_('Lists all available predefined modes'), action="store_true", default=False)
    parser.add_argument('file', help=_("File to convert"), action="store")

    global args
    args=parser.parse_args(parameters)


    if args.modes==True:
        modes=ModeManager()
        modes.print()
        sys.exit(0)

    directory="./mkvresizer_{}".format(str(datetime.datetime.now()).replace("-", "").replace(":", "").replace(" ", "")[0:14])
    directoryoriginal=directory+_("/original")
    directoryconverted=directory+_("/converted")
    os.mkdir(directory)
    os.mkdir(directoryoriginal)
    os.mkdir(directoryconverted)
    
    mkv=Mkv(args.file)
    mkv.split(directoryoriginal)
    mkv.join(args.modes)
    



   # shutil.rmtree(directory)
