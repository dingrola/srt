import os

source = '/Users/rolandding/Desktop'
dest = '/Users/rolandding/Downloads'
debug = False

class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path

def get_filepaths(directory, filter):

    filesList = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            if filename.endswith(filter):
                filepath = os.path.join(root, filename)

                filesList.append(File(filename, filepath))  # Add it to the list.

    return filesList  # Self-explanatory.

print
print('********** Start transfering SRT to right directories **********')
print
srtList = get_filepaths(source, '.srt')
videosList = get_filepaths(dest, '.mkv')
videosList.extend(get_filepaths(dest, '.mp4'))
failedList = []

if debug:
    print('SrtList : ')
    for srtFile in srtList:
        print(srtFile.name)
    print
    print('VideoList : ')
    for video in videosList:
        print(video.name)
    print

for srtFile in srtList:
    success = False
    srtNameSplit = str.split(srtFile.name, ' - ')
    if srtNameSplit.__len__() > 1:
        srtName = srtNameSplit[0].strip()
        srtName = srtName.replace(' ', '.')
        srtNo = srtNameSplit[1].strip()
        srtNo = srtNo.replace('x', 'E')

        if debug: 
            print('SrtName : ' + srtName)
            print('SrtNo : ' + srtNo)

        for video in videosList:
            if str.startswith(video.name.lower(), srtName.lower()[:10]):
                if str.find(video.name.lower(), srtNo.lower()) >= 0:
                    destpath, extension = os.path.splitext(video.path)
                    if debug:
                        print('srtFile.path = ' + srtFile.path)
                        print('destpath = ' + destpath)
                    os.rename(srtFile.path, destpath + '.srt')
                    print(srtFile.name)
                    print(video.name)
                    print
                    success = True

    if not success:
        failedList.append(srtFile.name)     

if len(failedList) > 0:
    print('----------- ' + str(len(failedList)) + ' has failed ---------')      
    for failedSrt in failedList:
        print(failedSrt)   
    print

print('*************** End of transfers ***************')



