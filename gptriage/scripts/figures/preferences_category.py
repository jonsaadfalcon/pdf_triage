import io
import matplotlib.pyplot as plt
import pandas as pd

# Given CSV data
data = """
Category,PDFTriage,Page Retrieval,Chunk Retrieval
Overall,50.8,27.1,22.1
" ",0.0,0.0,0.0
Structure Questions,75.0,5.0,20.0
Table Reasoning,62.5,12.5,25.0
Rewrite,57.14,14.29,28.57
Outside Questions,52.38,33.33,14.29
Figure Questions,51.43,22.86,25.71
Cross-page Tasks,50.0,33.33,16.67
Summarization,47.73,34.09,18.18
Text Questions,46.81,19.15,34.04
Extraction,45.61,24.56,29.82
Classification,45.0,25.0,30.0
"""

# Convert the CSV string to a DataFrame using io.StringIO
df = pd.read_csv(io.StringIO(data))
df[df.columns[1:]] = df[df.columns[1:]].round(1)
df = df.iloc[::-1]
df = df.reset_index(drop=True)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Set the colors
colors = ['black', 'gray', 'white']

# For each row in the DataFrame, plot a stacked bar
bottom = [0] * len(df)
for column, color in zip(df.columns[1:], colors):
    ax.barh(df['Category'], df[column], left=bottom, color=color, edgecolor='black', label=column)
    bottom += df[column]

# Add the percentages as text on the bars
for idx, row in df.iterrows():
    width = 0
    for col_ix, column in enumerate(df.columns[1:]):
        if row[column] == 0: continue
        if row[column] > 5:
            ax.text(width + row[column]/2, idx, f'{row[column]:.1f}%', ha='center', va='center',
                color='black' if colors[col_ix] == 'white' else 'white', fontsize=10, fontweight='bold')
        width += row[column]

# Remove the y-axis label
ax.set_ylabel('')
ax.set_xlim(0, 100)

# Set the x-axis label
ax.set_xlabel('Annotator Preferences (%)')

# # Add a vertical line at 100%
# ax.axvline(100, color='black')
ax.axhline(10, color='black', linewidth=1)
# Remove the grid
ax.grid(False)

# Add the legend at the top
ax.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.15))

# Display the plot
plt.tight_layout()
# plt.show()
plt.savefig("preferences_by_type.pdf")
