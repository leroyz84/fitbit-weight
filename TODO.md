# Fitbit weight to garmin connect
I have a scale that connects to Fitbit, i want to upload the wieght and bodyfat metric to Garmin Connect

I normally weight in the morning, with the app it's synced to online. I need to run the script daily at a certain time to distress the load.

Idea is to get all the data locally (last 7 days, iterate, store in json daily)

### Tasks
- [ ] script to store config data in config.json
- [ ] FitBit
  - [ ] get the token generate script
    - [ [ strip to suit my config.json
  - [ [ check for api refresh token usage
  - [ ] fetch data
    - [ ] Check if data today
    - [ ] Store local (in json)?
- [ ] Carmin Connect
  - [ ] get the token generate script
  - [ ] Store the config
  - [ [ strip to suit my config.json
  - [ ] parse the fitbit local store
    - [ ] if not uploaded, upload?




