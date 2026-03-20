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
- Game duration rules (evaluated in priority order):
    - If the `leagueType` field contains "2hour" (case-insensitive), the game is 2 hours (120 minutes).
    - If the team's age group (`year` field) is U18 or older — matching values like `18B`, `18G`, `U18B`, `U18G`, `19B`, `19G`, `20B`, `20G`, etc. — the game is 2 hours (120 minutes).
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

#### Rules for overlapping games on the same field
- When two or more games on the same field overlap in time, they are grouped into an overlap cluster.
- The cluster spans from the earliest game start to the latest game end across all overlapping games.
- The cell for that field occupies a single `rowspan` covering the full cluster duration.
- Games within the cluster are displayed **side by side** as vertical panels inside the cell.
- Each panel's **top offset** is proportional to how far into the cluster that game starts (e.g. a game starting 30 minutes into a 90-minute cluster starts 33% down).
- Each panel's **height** is proportional to that game's duration relative to the cluster duration.
- Each panel's **width** is an equal share of the cell width (e.g. two games each get 50%).
- The cell column is widened automatically (`min-width` = number of games × 120px) so games remain readable without a scrollbar.
- Each panel shows the game's start time and team name, and inherits the VEO camera color class, HOLDER border, or CHANGE_REQUEST border as applicable.
- The container background is red (#ff4444) so the overlapping area is visually distinct from normal cells.




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