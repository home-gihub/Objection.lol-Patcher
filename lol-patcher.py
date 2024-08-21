import sys
import os
import requests
import data
import cli

__version__: int = 1.0
InstallDir: str = ""

fileSep = '\\' if os.name == 'nt' else '/'

def clearscrn():
    os.system('cls' if os.name == 'nt' else 'clear')

def downloader(repo, installDir):
    clearscrn()
    if installDir == ".":
        installDir = os.getcwd()
    if installDir[len(installDir) - 1] == "/" or installDir[len(installDir) - 1] == "\\":
        cli.msgbox(" Error ", ["Install Directory is invald (separator at the end)"])
        exit()
    print("Directory is valid")
    print(f"{installDir}")
    print("Grabbing...")
    for i in repo:
        currMajDir: str = installDir + fileSep + i["dir"]
        for j in range(0,len(i["contents"])):
            currMinDir: str = currMajDir + fileSep.join(i["contents"][j]["writeto"]["dir"])
            currFile: str = currMinDir + fileSep + i["contents"][j]["writeto"]["file"]
            
            if os.path.exists(currMinDir) != True:
                os.makedirs(currMinDir)
            if os.path.isfile(currFile) != True:
                temp_wrtr = open(currFile, "x")
                temp_wrtr.close()

            clearscrn()
            cli.msgbox(" Downloader ", ["Downloading...", f"Progress: {j} / {len(i['contents'])} in {i["dir"]}", f"Writing {currFile} at {i["contents"][j]["grab"]}"])

            resp = requests.get(i["contents"][j]["grab"])
            if resp.ok != True:
                cli.msgbox(" Error ", [f"Request to: {i["content"][j]["grab"]}", f"failed with code {resp.status_code}", f"reason: {resp.reason}"])
                exit()

            with open(currFile,"wb") as file:
                file.write(resp.content)
    
    

def main(argv: list[str]):
    print(""" 
   ____  _     _           _   _                   _       _      _____      _       _               
  / __ \\| |   (_)         | | (_)                 | |     | |    |  __ \\    | |     | |              
 | |  | | |__  _  ___  ___| |_ _  ___  _ __       | | ___ | |    | |__) |_ _| |_ ___| |__   ___ _ __ 
 | |  | | '_ \\| |/ _ \\/ __| __| |/ _ \\| '_ \\      | |/ _ \\| |    |  ___/ _` | __/ __| '_ \\ / _ \\ '__|
 | |__| | |_) | |  __/ (__| |_| | (_) | | | |  _  | | (_) | |    | |  | (_| | || (__| | | |  __/ |   
  \\____/|_.__/| |\\___|\\___|\\__|_|\\___/|_| |_| (_) |_|\\___/|_|    |_|   \\__,_|\\__\\___|_| |_|\\___|_|   
             _/ |                                                                                    
            |__/      
                                                                                         
""")
    print(f"by Home")
    print(f"Running at {os.getcwd()}")

    match cli.entry(" Welcome ", ["Type the number of what action you would like to do, or any other key to exit.", "1) Download and Patch files from Objection.lol"]):
        case "1":
            downloader(data.Assets, input("Install Directory (. for this directory): "))
            clearscrn()
            cli.msgbox(" Finished ", ["All done!", "Exiting"])
            exit()
        case _:
            print("Working...")
            exit()


if __name__ == "__main__":
    main(sys.argv)