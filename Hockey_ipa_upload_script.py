#!/usr/local/bin/python3

# Please update hockey app token, It placed in Hockey app.
hockeyapp_token = "XXXXXXXXXXXX"
ipa_build_path = "/Users/rvysyaraju/Documents/Dummy/GridWrapper.ipa" # build path for where build is placed
hockeyAppId =  "" # Each app has individual hockey app id to identify app in Hockey website


hockeyapp_upload_link = "https://rink.hockeyapp.net/api/2/apps/{}/app_versions/upload"

#
# 0 to not notify testers
# 1 to notify all testers that can install this app
# 2 notify all testers
# #notify - optional, notify testers (can only be set with full-access tokens):
notify = "0"
# status - optional, download status (can only be set with full-access tokens):
# 
# 1 to not allow users to download the version
# 2 to make the version available for download

release_notes = "Release notes"

import requests

def upload_build(build_file, hockeyAppId="", notify = "0", release_notes=None):
    params = {}
    build_release_notes = release_notes
    if release_notes is not None and len(release_notes) != 0:
        build_release_notes = release_notes
    #print(release_notes)
    params['notes'] = build_release_notes
    params['status'] = "2"
    params['download'] = True
    params['notify'] = notify
    files = {'ipa': open(build_file, 'rb')}
    headers = {'X-HockeyAppToken' : hockeyapp_token}
    try:
        req = requests.post(url=hockeyapp_upload_link.format(hockeyAppId), data=params, files=files, headers=headers)
        return (req.json(), req.status_code)
    except ConnectionError:
        raise AutoHockeyConnectionError('Connection error. Please try again.')
def main():
	upload_build(ipa_build_path, hockeyAppId, notify, release_notes)

if __name__ == "__main__":
    main()
