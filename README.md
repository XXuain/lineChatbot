# lineChatbot
user >> line server >> web app

## step.1 Register LINE Bot Account

### [LINE Developers](https://developers.line.biz/zh-hant/)
### Product/[Message Api](https://developers.line.biz/en/services/messaging-api/)
- Create a channel


## step.2 Created project (install plugin & sample code)

### GitHub Create a new repository
### Use [LINE SDK](https://github.com/line/line-bot-sdk-python)
- install ` $ pip3 install line-bot-sdk `
- new ` app.py ` and use [Synopsis](https://github.com/line/line-bot-sdk-python#synopsis) sample code
- ` app.py ` change ` YOUR_CHANNEL_ACCESS_TOKEN ` & ` YOUR_CHANNEL_SECRET `

## step.3 Created server

### Register [Heroku](https://id.heroku.com/login) Account

### Install Heroku CLI
- ` $ brew install heroku/brew/heroku `
- ` $ heroku login `

### Created Heroku App & using git
- ur app > deploy
- ur existing git project add the heroku remote
` $ heroku git:remote -a {ur heroku app name} `

### Created setting file
- for Heroku new ` Procfile `
- new ` Requirements.txt ` ( ` $ pip3 freeze > Requirements.txt `)

setting Webhooks



## step.5 LINE Bot setting
