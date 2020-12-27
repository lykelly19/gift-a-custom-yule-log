# Gift a Yule Log   
MLH Holiday Hacks 2020    
  
## Inspiration   
The holidays are certainly a bit different this year due to the pandemic. With the pandemic and social distancing measures in place, gifting is a little more difficult this year. Although we may not be able to have large social gatherings, many of us head to YouTube to find Yule Logs, which show a fireplace and play some music. We created this web app: Gift a Yule Log so you can gift your friends and family members something that is unique. You can share your own custom Yule Log with a personalized holiday message. Simply curate or select a Spotify playlist to build your own Yule Log -- all while being environmentally-friendly.   

## What it does   
“Gift a Yule Log” is an app that gives users the option of selecting a Spotify playlist to customize their own Yule Log. A link is then generated, and users can simply share the customized Yule Log with friends by pasting the link to text messages or on social media. or they can send it more personally via email. The app has an option of sending a custom message along with the link to spread some extra holiday cheer.    

If you simply want to enjoy a traditional holiday Yule Log, check out the “My Yule Log” option on the home page, which is set and ready to go with some peaceful holiday instrumentals for the background music.    

## How we built it  
We built the web app using Flask which involved Python, HTML, CSS, and JavaScript, and deployed the application with the help of Heroku. The app uses a lot of forms in order to get the user’s input in the back-end, which is needed to create the custom Yule Log links and the webpage logic. We used smtplib to send the emails, did a lot of styling with CSS to make it as user-friendly as possible, and added a snow falling animation effect using JavaScript to bring in the excitement of the holidays.   

## Challenges we ran into     
We had to figure out how to parse links in Flask so that the Yule Log could be customized for any Spotify playlist that was selected. We also had to find out how to use smtplib for creating and sending a custom email, and this involved learning how to connect to the server, format the email message properly, and grant access for emailing.   

## Accomplishments that we’re proud of   
We are proud of building a fully functioning web app and having it deploy successfully with Heroku. We also hope that our app will help spread the holiday spirit this season especially.   

## What we learned   
We learned a lot more about how to use Flask, how to incorporate JavaScript, and how to send emails through code.    

## What’s next for Gift a Yule Log   
We hope to incorporate more stylized emails in the near-future. In the meantime, we’ll be sharing some great custom Yule Logs with friends and family members :)   


