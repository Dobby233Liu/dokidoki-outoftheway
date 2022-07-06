init python:
    # Limits the engine to only use one save location (user savedir)
    # See init function of savelocation.py in Ren'Py.
    if not config.developer and len(renpy.loadsave.location.locations) > 1:
        renpy.loadsave.location.locations = renpy.loadsave.location.locations[:1]

# This python statement checks that 'audio.rpa', 'fonts.rpa' and 'images.rpa'
# are in the game folder and if the project is in a cloud folder (OneDrive).
# Note: For building a mod for PC/Android, you must keep the DDLC RPAs 
# and decompile them for the builds to work.
init -100 python:
    if not renpy.android:
        for archive in ['audio','images','fonts']:
            if archive not in config.archives:
                raise DDLCRPAsMissing(archive)

        if renpy.windows:
            onedrive_path = os.environ.get("OneDrive")
            if onedrive_path is not None:
                if onedrive_path in config.basedir:
                    raise IllegalModLocation