# chatGPT-discord-bot

> ### This is a project that provides you to build your own Discord bot using ChatGPT
>
> ⭐️ A star would be highly appreciated

## Notice
> #### OpenAI added Cloudflare protections to their API, here are some differences in using it on server and desktop environment

## Features

* `/chat [message]` Chat with ChatGPT!
* `/private` ChatGPT switch to private mode
* `/public`  ChatGPT switch to public  mode
* `/reset`   ChatGPT conversation history will be erased

### Chat

![image](https://user-images.githubusercontent.com/89479282/206497774-47d960cd-1aeb-4fba-9af5-1f9d6ff41f00.gif)

### Mode

* `public mode (default)`  the bot directly reply on the channel

  ![image](https://user-images.githubusercontent.com/89479282/206565977-d7c5d405-fdb4-4202-bbdd-715b7c8e8415.gif)
* `private mode` the bot's reply can only be seen by who use the command

  ![image](https://user-images.githubusercontent.com/89479282/206565873-b181e600-e793-4a94-a978-47f806b986da.gif)

# Setup

## Install

`pip install -r requirements.txt`

dependencies: Reverse Engineered ChatGPT by OpenAI [here](https://github.com/acheong08/ChatGPT) and discord.py

## Step 1: Create a Discord bot

1. Go to https://discord.com/developers/applications create an application
2. Build a Discord bot under the application
3. Get the token from bot setting

   ![image](https://user-images.githubusercontent.com/89479282/205949161-4b508c6d-19a7-49b6-b8ed-7525ddbef430.png)
4. Store the token to `config.json` under the `discord_bot_token`

   ![image](https://user-images.githubusercontent.com/89479282/205949488-f3f2903d-7fb8-4be3-a703-2174535b3cd7.png)
5. Turn MESSAGE CONTENT INTENT `ON`

   ![image](https://user-images.githubusercontent.com/89479282/205949323-4354bd7d-9bb9-4f4b-a87e-deb9933a89b5.png)
   
6. Invite your bot to your server via OAuth2 URL Generator

   ![image](https://user-images.githubusercontent.com/89479282/205949600-0c7ddb40-7e82-47a0-b59a-b089f929d177.png)

## Desktop environments

> You do not need to fill out `session_token` in `config.json`

### Step 2: Run the bot
1. Open a terminal or command prompt
2. Navigate to the directory where you installed the ChatGPT Discord bot
3. Run `python3 main.py` to start the bot
### Step 3: log in
1. Wait for the Cloudflare checks to pass
2. Reload if show `ChatGPT is at capacity right now`
3. Log into OpenAI via the open browser (Your account)
4. It should automatically redirect you to https://chat.openai.com/chat after logging in. If it doesn't, go to this link manually after logging in.
5. The window should close automatically

### Have A Good Chat !

 
## Server & Docker

> You must fill the session token in `config.json`

### Step 2: Session token authentication

Go to https://chat.openai.com/chat log in

1. Open console with `F12`

2. Open `Application` tab > Cookies

    ![image](https://user-images.githubusercontent.com/36258159/206955081-8a8e1ff9-d12c-456c-9a67-5c1a7438f76c.png)

3. Copy the value for `__Secure-next-auth.session-token` from cookies and paste it into `config.json` under `session_token`

> You can use `Xvfb` to emulate a desktop environment. It should automatically get the cf_clearance given no captcha

### Step 3: Run the bot with docker

1. Build the Docker image `docker build -t chatgpt-discord-bot --platform linux/amd64 .`
2. Run the Docker container  `docker run --platform linux/amd64 -d chatgpt-discord-bot`

   ### Stop the bot:

   * `docker ps` to see the list of running services
   * `docker stop <BOT CONTAINER ID>` to stop the running bot

### Have A Good Chat !

## Optional: Setup starting prompt

* A starting prompt would be invoked when the bot is first started or reset
* You can set it up by modifying the content in `starting-prompt.txt`
* All the text in the file will be fired as a prompt to the bot  

