# Wordwall-hack
**Setup**
1. Open Microsoft Edge and go to your desired Wordwall quiz.
2. Press CTRL + SHIFT + I to open Developer Tools.
3. Click on the Network tab at the top.
4. Complete the quiz and click "View Leaderboard" on Wordwall.
5. Look for "getentryrank" or "leaderboard" in the network requests.
6. Click on one of them.
7. Scroll down and find the URL that looks like:
   <br>
   htps://wordwall.net/leaderboardajax/getentryrank?score=2&time=25775&**activityId=73328238**&**templateId=3**
8. Data looks like this(extracted from the link):
   - activityId (e.g., 73328238)
   - templateId (e.g., 3)
   
Quite a cool script for wordwall 
