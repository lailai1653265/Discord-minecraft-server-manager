
# Discord Bot for Managing Minecraft Server

This project is a Discord bot that can manage a Fabric Minecraft server. The bot can start the server, execute RCON commands, and check the server status.

## Prerequisites

- Python 3.8 or higher
- Discord bot token
- Fabric Minecraft server
- RCON enabled on your Minecraft server
- Java installed on your system
- `.env` file with the necessary environment variables
## Ensure RCON is enabled in your Minecraft server’s server.properties file:

```
enable-rcon=true
rcon.port=25575
rcon.password=your_rcon_password
```
## Bot Commands

- **Start Minecraft server**:
    ```plaintext
    !s
    ```
    Starts the Fabric Minecraft server if it's not already running.

- **Execute Minecraft command**:
    ```plaintext
    !c <command>
    ```
    Executes an RCON command on the Minecraft server.

- **Check Minecraft server status**:
    ```plaintext
    !sta
    ```
    Checks if the Minecraft server is running.

## Logging

The bot uses Python's built-in logging module to log information, warnings, and errors. Logs are displayed in the console with timestamps and log levels.

## Notes

- Ensure that your Minecraft server is configured to allow RCON connections.
- The RCON password and port must match the settings in your `server.properties` file.

## Troubleshooting

- If the bot fails to start, check that all required environment variables are set correctly in the `.env` file.
- If the bot cannot connect to the Minecraft server via RCON, verify that the server is running and that RCON is enabled and properly configured.

This README provides instructions on how to set up and use the Discord bot for managing a Fabric Minecraft server.
