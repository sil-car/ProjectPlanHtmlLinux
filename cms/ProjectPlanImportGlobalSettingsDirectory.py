'''
Supersedes ProjectPlanImport.py by using the provided global 'SettingsDirectory'.

@author: Nate Marti
'''
import os
from ProjectPlanImport import ProjectPlan # sub-imported by ProjectPlanHtmlLinux

       
def basePlans():
    """An iterator that yields a sequence of tuples consisting of base plan 
    name and path. A base plan is an XML file in 
    My Paratext 8 Projects\_StandardPlans
    """
    # strPlansDirectory = os.path.join(settingsDirectory(),"_StandardPlans")
    global SettingsDirectory
    strPlansDirectory = os.path.join(SettingsDirectory,"_StandardPlans")
    listFiles = os.listdir(strPlansDirectory)
    for strFile in listFiles:
        if strFile[-4:] == '.xml':
            strName = strFile[0:-4]
            strPath = os.path.join(strPlansDirectory, strFile)
            yield strName, strPath
            

def findBasePlan(strSearch):
    """ Searches for a base plan whose name contains strSearch, and returns
    the name of the plan and its path. If more than one plan matches
    strSearch, the first one found is returned.
    """
    for strName, strPath in basePlans():
        if strSearch in strName:
            return strName, strPath
    return '',''
        
def findProjectProgress(strProject):
    if not strProject:
        return '',''
    global SettingsDirectory
    strPath = os.path.join(
        # settingsDirectory(), strProject, 'ProjectProgress.xml'
        SettingsDirectory, strProject, 'ProjectProgress.xml'
        )
    if os.path.exists(strPath):
        strName = strProject + ' ProjectProgress.xml'
        return strName, strPath
    else:
        return '',''
        
def ProjectNames():
    """An iterator that returns a sequence of project names. A project is
    identified as a folder in settingsDirectory() that contains a file named 
    settings.xml
    """
    global SettingsDirectory
    # listFiles = os.listdir(settingsDirectory())
    listFiles = os.listdir(SettingsDirectory)
    for strFile in listFiles:
        # strPath = settingsDirectory() + strFile
        strPath = SettingsDirectory + strFile
        if os.path.isdir(strPath):
            # Found a folder. Does it contain a settings file?
            strSettingsPath = os.path.join(strPath,"Settings.xml")
            if os.path.exists(strSettingsPath):
                yield strFile
