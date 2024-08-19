import sys
import os
import requests
import data

__version__: int = 1.0
InstallDir: str = ""

fileSep = '\\' if os.name == 'nt' else '/'

def clearscrn():
    os.system('cls' if os.name == 'nt' else 'clear')

def TitleBar():
    print(f"Objection.lol patcher ---- v{__version__} by Home")

def error(message: str):
    clearscrn()
    TitleBar()
    print("""
       __     ______                     
  _   / /    |  ____|                    
 (_) | |     | |__   _ __ _ __ ___  _ __ 
     | |     |  __| | '__| '__/ _ \\| '__|
  _  | |     | |____| |  | | | (_) | |   
 (_) | |     |______|_|  |_|  \\___/|_|   
      \\_\\                                
                                         
          """)
    print(message)
    print("Closing...")
    exit()

def downloader(repo, installDir):
    clearscrn()
    TitleBar()
    if installDir == ".":
        installDir = os.getcwd()
    if installDir[len(installDir) - 1] == "/" or installDir[len(installDir) - 1] == "\\":
        error("Install Directory is invald (separator at the end)")
    print("Directory is valid")
    print(f"{installDir}")
    print("Grabbing...")
    for i in repo:
        currMajDir: str = installDir + fileSep + i["dir"]
        for j in range(0,len(i["content"])):
            clearscrn()
            TitleBar()
            print("=== Downloader ===")
            print("Downloading...")
            currMinDir: str = currMajDir + fileSep.join(i["content"][j]["writeto"]["dir"])
            currFile: str = currMinDir + fileSep + i["content"][j]["writeto"]["file"]
            
            if os.path.exists(currMinDir) != True:
                os.makedirs(currMinDir)
            if os.path.isfile(currFile) != True:
                temp_wrtr = open(currFile, "x")
                temp_wrtr.close()

            print(f"Progress: {j} / {len(i['content'])} in {i["dir"]}")
            print(f"Writing {currFile} at {i["content"][j]["grab"]}")

            resp = requests.get(i["content"][j]["grab"])
            if resp.ok != True:
                error(f"Request to: {i["content"][j]["grab"]} failed with code {resp.status_code} reason: {resp.reason}")

            with open(currFile,"wb") as file:
                file.write(resp.content)
        
            print(f"Done {i["content"][j]["grab"]}")
    
    

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
    print(f"v{__version__} by Home")
    print(f"Running at {os.getcwd()}")

    print("\n Welcome, Type the number of what action you would like to do, or any other key to exit.")
    print("1) Download and Patch files from Objection.lol")

    match input("Type here: "):
        case "1":
            downloader(data.Assets, input("Install Directory (. for this directory): "))
            clearscrn()
            TitleBar()
            print("+--+ FINISH +--+")
            print("All Done now.")
            print("Exiting...")
            exit()
        case _:
            print("Working...")
            exit()


if __name__ == "__main__":
    main(sys.argv)