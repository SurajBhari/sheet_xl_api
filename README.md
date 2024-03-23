# sheet xl api

Basic goal is to allow one to view a sheet data using just API. 

to run this follow [this](https://github.com/xflr6/gsheets/?tab=readme-ov-file#quickstart) to obtain the client_secrets.json and run the program to validate a login request. and then just use this. 

Base Url - http://surajbhari.info:54321
# Arguments
- `id`* (important) - ID of the sheet. you can find this ID in URL if link is `https://docs.google.com/spreadsheets/d/1SX6MH1wH9ic1_9pZozH63DaL0Y6mpvYvpb31dOUMyY/edit` than id is `1SX6MH1wH9ic1_9pZozH63DaL0Y6mpvYvpb31dOUMyY` 
- `sheet_id` (optional) - index for the sheet to be used. 0 for first one. and so on


# Routes
`/` - gives back json in Row wise. 
`/rf` - same as `/`
`/cf` - gives back json in Column wise.
`/c/<number>` - gives column at that number. starts at 0.
`/r/<number>` - gives row at that number. starts at 0.

This is one of those project that I just made for someone else. and is not actively maintaining it. still if you find it not working. DM me on discord.
