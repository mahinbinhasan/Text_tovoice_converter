import pyttsx3

fig = """
    __  ___      __    _          _    __      _              ______         
   /  |/  /___ _/ /_  (_)___     | |  / /___  (_)_______     / ____/__  ____ 
  / /|_/ / __ `/ __ \/ / __ \    | | / / __ \/ / ___/ _ \   / / __/ _ \/ __ )
 / /  / / /_/ / / / / / / / /    | |/ / /_/ / / /__/  __/  / /_/ /  __/ / / /
/_/  /_/\__,_/_/ /_/_/_/ /_/     |___/\____/_/\___/\___/   \____/\___/_/ /_/    OFFLINE VERSION -- ONLY ENGLISH --
                                       """
print(fig)
rate = 145
engine = pyttsx3.init()
mytext = input("Enter your text:" )
engine.setProperty('rate',rate)
engine.save_to_file(mytext,'offlint.mp4')

engine.runAndWait()
