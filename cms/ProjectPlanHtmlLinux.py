'''
Created on April 11, 2018
Modified on Sep 11, 2023

@author: Mike Herchenroeder
@author: Nate Marti
'''
import ProjectPlanImportGlobalSettingsDirectory as ProjectPlanImport
import sys
import codecs
import os
from ProjectPlanToHtml import writereport


def main():
    if os.name != 'posix':
        sys.stderr.write("Error: This script is for Linux-based systems.\n")
        return

    global TESTMODE
    TESTMODE = False
    sys.stdout = codecs.open(OutputFile, 'w', 'utf-8')
    try:
        aBasePlan = None
        try:
            if len(OptionBasePlan.strip()) > 0:
                strName, strPath = ProjectPlanImport.findBasePlan(OptionBasePlan)
                if not strName:
                    # say("Could not find base plan: %s." % OptionBasePlan)
                    sys.stderr.write("Could not find base plan: %s.\n" % OptionBasePlan)
                    return
            else:
                strName, strPath = ProjectPlanImport.findProjectProgress(Project)
                if not strName:
                    # say("Could not find ProjectProgress for: %s." % Project)
                    sys.stderr.write("Could not find ProjectProgress for: %s.\n" % Project)
                    return
                
            aBasePlan = ProjectPlanImport.ProjectPlan(strName, strPath, OptionLanguage)
            aBasePlan.parseAll()
            writereport(aBasePlan)
        except:
            raise
        finally:
            if aBasePlan: aBasePlan.close()

    except:
        sys.stdout.close()
        raise

    # Show the HTML file.
    try:
        # The "\toHtml" parameter for CMS files attempts to open the generated
        #   file in the default browser. However, this doesn't work correctly on
        #   Linux systems. Instead, an "Access denied" error window is produced.
        #   A workaround is to call the xdg-open command directly here.
        # Also, the browser error is somehow silenced when a different
        #   message is forced by sending text to STDERR.
        os.system('xdg-open ' + OutputFile)
        sys.stderr.write("Successfully converted '%s'.\n" % strPath)
    except Exception as e:
        sys.stderr.write(str(e))


# Run script.
main()
