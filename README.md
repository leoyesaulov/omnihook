# omnihook
A simple API for webhooks, including the scripts

The purpose of this API is to be available for webhooks (such as from GitHub) to do the actions needed.

## Webhooks:
- GitHub: pull the repo on repo commit. Challenge: it has to be able to distinguish the repos and locate them locally. Proposed solutiion: keep all repos in a single directory, distinguish by repo name.
- Telegram: collects webhooks from bot interactions, calls the bot server.

## The plan: 
- This service exposes an API. On an inbound request it calls appropriate functions via rpc

Part of Omniserv
