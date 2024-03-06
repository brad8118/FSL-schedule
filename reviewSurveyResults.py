import pandas as pd
import plotly.graph_objects as go
import plotly.offline as offline
import io
import base64

# https://chat.openai.com/c/6fe126bb-81ec-4083-86ce-0cf0e3c1d659
# Function to generate pie charts
def generate_pie_chart(data):
    labels = list(data.keys())
    values = list(data.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    # fig.update_layout(title=chart_title)    
    return offline.plot(fig, include_plotlyjs=False, output_type='div')

html_content = '<!DOCTYPE html>'
html_content += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>'

# Load Excel file
survey_data = pd.read_excel('Freehold Soccer Survey Fall 2023.xlsx')

# Generate HTML table
html_content += '<table border="1"><tr>'

# Create table headers
for column in survey_data.columns:
    html_content += f'<th>{column}</th>'    
html_content += '</tr>'

# Populate table with data
# for index, row in survey_data.iterrows():
#     html_content += '<tr>'
#     for value in row:
#         html_content += f'<td>{value}</td>'
#     html_content += '</tr>'

# Group data by 'Category' column
column_name_grouped_by = 'Which Team does your child play for'
grouped_data = survey_data.groupby(column_name_grouped_by)

for category, group in grouped_data:
    print(f"Category: {category}")
    print(group)  # This will print each group (data related to that category)
    
    # ordered & group by team name
    # html_content += '<tr>'
    # for index, row in group.iterrows():
    #     html_content += '<tr>'
    #     for value in row:
    #         html_content += f'<td>{value}</td>'
    #     html_content += '</tr>'

    html_content += '<tr>'    
    for column in survey_data.columns:
        grouped__by_team_by_column_data = group.groupby(column) #group the results by team then by column
        print(f"    +++++++++++++++++++++++++++")

        print(f"column NAME: {column}")
        print(grouped__by_team_by_column_data[column].describe())
        total_counts= {"Strongly Agree":0, "Agree": 0,"Neutral": 0,"Disagree": 0,"Strongly Disagree": 0}
        
        for row in grouped__by_team_by_column_data[column].describe():
            print("value", row) 

            # for value in row:
                # print("value", value) 
            # print("c",c)
            # print("g",g)


        print(f"    --------------------------")
        # print(grouped__by_team_by_column_data[column].describe().unstack(1).reset_index())
        print(f"-----------------row end----------------------------")

        
        # for category_by_team, group_by_team in grouped_data:
            # print(f"category_by_team: {category_by_team}")
            # print(group_by_team)  # This will print each group (data related to that category)

            # html_content += '<tr>'
            # for value in row:
            #     html_content += f'<td>{value}</td>'
            # html_content += '</tr>'
        html_content += '<td style="display: flex; justify-content: space-around;">'
        # html_content += generate_pie_chart()
        html_content += '</td>'

    html_content += '</tr>'
    print(f"==============================================")
    exit()

html_content += '</table>'

with open('survey_results.html', 'w') as file:
    file.write(html_content)
