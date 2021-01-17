# Machaao Wit Template

## Getting Started

1. Clone this repo
```bash
git clone https://github.com/machaao/machaao-wit-template.git

cd machaao-wit-template
```

2. Installing Dependencies
```bash
pip install -r requirements.txt
```

3. Environment Variable  
Create file with name ```.env```
```bash
WIT_ACCESS_TOKEN=<YOU-WIT-ACCESS-TOKEN>
MESSENGERX_API_TOKEN=<YOU-MESSENGERX-API-KEY>
MESSENGERX_BASE_URL=https://ganglia-dev.machaao.com
```

4. Running Server
```bash
flask run
```

5. Running Tunnel (For Debugging)
```bash
machaao tunnel -p 5000 -t <YOU-MESSENGERX-API-KEY>
```

6. Updating Webhook Url

Your Webhook Url: ```https://<chatbot-name>.tunnel.messengerx.io/machaao/incoming```

### Contact Us

Email: <a href="mailto:support@messengerx.io">support@messengerx.io</a>  
Gitter: https://gitter.im/messengerx-io/community