import requests
import os
import random
import time
os.system("cls")

print("""
 __       __                            __                          __  __ 
/  |  _  /  |                          /  |                        /  |/  |
$$ | / \ $$ |  ______    ______    ____$$ | __   __   __   ______  $$ |$$ |
$$ |/$  \$$ | /      \  /      \  /    $$ |/  | /  | /  | /      \ $$ |$$ |
$$ /$$$  $$ |/$$$$$$  |/$$$$$$  |/$$$$$$$ |$$ | $$ | $$ | $$$$$$  |$$ |$$ |
$$ $$/$$ $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |$$ | $$ | $$ | /    $$ |$$ |$$ |
$$$$/  $$$$ |$$ \__$$ |$$ |      $$ \__$$ |$$ \_$$ \_$$ |/$$$$$$$ |$$ |$$ |
$$$/    $$$ |$$    $$/ $$ |      $$    $$ |$$   $$   $$/ $$    $$ |$$ |$$ |
$$/      $$/  $$$$$$/  $$/        $$$$$$$/  $$$$$/$$$$/   $$$$$$$/ $$/ $$/ 
                                                                           
                                                                           
                                                                           
 __                    __           discord.gg/FgM4zAw4qP                                       
/  |                  /  |                                                 
$$ |____    ______   _$$ |_                                                
$$      \  /      \ / $$   |                                               
$$$$$$$  |/$$$$$$  |$$$$$$/                                                
$$ |  $$ |$$ |  $$ |  $$ | __                                              
$$ |__$$ |$$ \__$$ |  $$ |/  |                                             
$$    $$/ $$    $$/   $$  $$/                                              
$$$$$$$/   $$$$$$/     $$$$/                                               

       made by Ohno                         
                                
""")

score = int(input("Enter your desired score 💯: "))
time_ms = int(input("Enter your desired time ⌛ (ms): "))
bot_name = input("Enter the name of your bot 🏷️(s): ")
bot_count = int(input("Enter amount of bots 🔟: "))
activity_id = int(input("Enter the activity ID(type 'help' if you don't know what this is)🆔: "))
template_id = int(input("Enter the template ID(type 'help' if you don't know what this is)🆔: "))

print("\n🚀================================================================🚀\n")

for x in range(bot_count):
    payload = {
        "score": score,
        "time": time_ms,
        # If the bot required is 1 it will not add a random number 
        "name": bot_name if bot_count == 1 else f"{bot_name}{random.randint(1, 1000)}",
        "mode": bot_count,
        "activityId": activity_id,
        "templateId": template_id,
}
               
    print("Creating...")
    print("...")
    time.sleep(1)
    print("...")
    # Request and posts ☠️
    response = requests.post("https://wordwall.net/leaderboardajax/addentry", data=payload)

    if response.status_code != 200:
        print(f"Bot {x+1}: Something went wrong.")
    else:
        print(f"🤖 Bot {x+1}: Successfully made a bot called {payload['name']}🤖")
        
print("\nThank you for using this tool and feel free to support me on my GitHub and Discord ツ")
print("                           👇👇👇👇")
print("")
time.sleep(1)
print("💪 =======> https://github.com/OhnoMain <======= 💪")
print("🎮 =======> https://discord.gg/FgM4zAw4qP <======= 🎮")
time.sleep(2)
input("Press enter to exit❌: ")
