# FSL-schedule

This repository contains simple browser-based schedule views for FSL. Each page is a standalone HTML file that uses jQuery to load schedule data from Google Sheets, with local mock JavaScript files available for testing.

# Data
- The response_games.json is an example of a response that has all games that all teams play. 

## HTML pages

### home_schedule.html

Displays the league game schedule, focused on home games. The page:

- Loads league schedule data from Google Sheets.
- Groups games by date and sorts them by start time.
- Shows upcoming home games by default, with an option to include past games.
- Combines game data with camera and dedicated camera sheet data.

#### Rules how the table should be shown
- only Show HOME games
- Columns are the Fields
- Rows are the times
- For the time, show increaments of 15 minutes
- When ordering fields, always order them Jackson Mills (FIelds that start with JM), then Opatut (fields that start with OP), Then MJT, then WFS.
- If a game start before or after the times being displayed, update the table rounds up to the hour before the game and after the game ends, so if a game were to start at 7:45 then the times would start at 7. Similarly if a game ends at 7:15pm the table would end at 8.
- Game duration rules:
    - Games on JM1 are 1 hour 30 minutes.
    - Games on Opatut fields are 1 hour 30 minutes only when the field name is the base field with no letter suffix, such as OP4, OP5, or OP6.
    - Games on Opatut lettered sub-fields, such as OP6A, OP6C, OP5A, or any field in the format OP#X where X is a letter, are 1 hour 15 minutes.
    - All other fields are 1 hour 15 minutes.
- Rules for games that fall on a Saturday or Sunday
    - Time starts at 8am and typically runs until 6pm
    - Show all fields at Jackson Mills (JM1, JM2, JM3, JM4, JM5, JM6)
    - If there are games being played at home on another field include that field
- Rules for games Monday though Friday
    - Show only the field where there is a game, but follow the same order as already outlined
    - Start the time on the table at 5pm and end at 10pm




### practice_schedule.html

Displays the weekly practice schedule in a field-by-field calendar layout. The page:

- Loads practice schedule data and league game data from Google Sheets.
- Builds weekly tables for the current and next week.
- Splits the schedule into separate field groups for OP fields and WF/MJT fields.
- Uses game data to support identifying game conflicts while rendering practice availability.

### capelli_schedule.html

Displays Capelli training or field reservation slots and supports submitting requests. The page:

- Loads the Capelli schedule from Google Sheets.
- Groups available slots by date and time.
- Lets users select unreserved slots from the table.
- Sends selected requests to a Google Form-backed workflow for submission.

## Supporting files

- Mock data files such as `mock_league_schedule.js` and `mock_weekly_practice_schedule.js` let the HTML pages run without live sheet data.
- `survey_results.html` is a separate reporting page for survey output and is not one of the three main schedule pages.
- `reviewSurveyResults.py` is a Python helper script used alongside the survey workflow.