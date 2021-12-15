# **NukeIt**
## Installing Python
To install pytohn you need to head to [this page](https://www.python.org/downloads/release/python-3101/)

## Necessary requirements
I am glad you asked, you can run a simple file I've created that automatically installs the requirements for you, run `Installer.py`
## Configuration
After installing Python, and installing all the required modules, you may now start editing the `config.json` file provided
## Usage
After configuring the main `config.json` file and setting it up, you may now run the `Main.py` file which is the actual nuker
## Actual usage
If you don't have enough knowledge about Python or specifically `discord.py`, then here's a quick example
```py
@client.command() # this is just definging whether your code is an event or a command
async def definingTheCommand(ctx): # "definingTheCommand" is what you need to send so the bot can be called
    await ctx.send("definingTheCommand is the actual user input to get this message") # the bot sends this
```
What I'm trying to say, you need to read the actual code so you know how to use it
## Oh my god! this shit is so slow!
What did you expect? there's no threading, and also is using `discord.py` which is extremely slow, use [repl.it](https://repl.it) instead of self-hosting it.

## Image & banner configuration
You can also add an server-icon or banner, just name them `banner.png` for banner, and `icon.png` for an server-icon

## Quick note
You have to use a `#` before a hexadecimal color or else the `colored` module would just scream and yell errors at you

## This wasn't made for educational purposes
Honestly I don't give a shit, It's not even made for educational purposes at all, have fun nuking servers