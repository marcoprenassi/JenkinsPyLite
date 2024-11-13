from JenkinsPyLite.JenkinsPyLite import Server

if __name__ == '__main__':
    host = ('http://localhost:8081/')
    credentials = ('mprenassi', '116f56cefde85d21acc3193f4356463e2b')
    server = Server(host, credentials)
    folder_list = server.get_job_folders()
    print(server.get_jobs(folder_list[2])[0]['name'])
    print(f"{folder_list[2]}/job/{server.get_jobs(folder_list[2])[0]['name']}")
    path_info = f"{folder_list[2]}/job/{server.get_jobs(folder_list[2])[0]['name']}"
    build_list = server.get_builds(path_info)
    for build in build_list:
        print(f"{build['fullDisplayName']} - result: {build['result']}")
    print(server.get_latest_build(path_info,server.LAST_SUCCESSFUL_BUILD))
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
