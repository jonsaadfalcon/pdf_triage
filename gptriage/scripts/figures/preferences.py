import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 14})

# Data
labels = ['GPTriage vs. Page Retrieval vs. Chunk Retrieval', 
          'GPTriage vs. Chunk Retrieval',
          'GPTriage vs. Page Retrieval']

system_names = ['GPTriage', 'Chunk Retrieval', 'Page Retrieval']

scores = [
    [50.7, 27.1, 22.1],
    [64.1, 35.9],
    [69.1, 30.9],
]

labels = labels[::-1]
scores = scores[::-1]

color_mapping = {
    'GPTriage': 'black',
    'Page Retrieval': 'gray',
    'Chunk Retrieval': 'white'
}

# Corresponding text colors
text_color_mapping = {
    'black': 'white',
    'gray': 'black',
    'white': 'black'
}


# New labels for the y-axis
new_labels = ["GPTriage vs. Pages", "GPTriage vs. Chunks", "Overall"]

# Create the figure and the line that we will use to separate the scores with reduced spacing between bars
fig, ax = plt.subplots(figsize=(10, 3))

ax.axhline(y=1.5, color='black', linewidth=1)
ax.axvline(x=100, color='black', linewidth=2)

# To keep track of which labels have been added to the legend
legend_added = []

# Plot each bar, add text, and create legend with thinner bars and reduced padding
for i, (label, score) in enumerate(zip(new_labels, scores)):
    left = 0
    
    # Determine which systems are being compared for each label
    systems_in_label = [sys for sys in system_names if sys in labels[i]]
    
    for sys_name in systems_in_label:
        s = score[systems_in_label.index(sys_name)]
        color = color_mapping[sys_name]
        text_color = text_color_mapping[color]
        
        # Ensure that the legend only contains unique labels
        if sys_name not in legend_added:
            bar = ax.barh(i, s, left=left, height=0.6, align='center', edgecolor='black', color=color, label=sys_name)
            legend_added.append(sys_name)
        else:
            bar = ax.barh(i, s, left=left, height=0.6, align='center', edgecolor='black', color=color)
        
        # Calculate the position for the text
        text_x = left + s/2
        text_y = i
        
        # Add the percentage text
        ax.text(text_x, text_y, f"{s:.1f}%", ha='center', va='center', color=text_color, fontsize=9, fontweight='bold')
        
        left += s

# Remove the y ticks and grid
ax.set_yticks(np.arange(len(new_labels)))
ax.set_yticklabels(new_labels)
ax.grid(False)

# Set the x limits and label
ax.set_xlim(0, 100)
ax.set_xlabel('User Preferences (%)')

# Position the legend outside the plot area to avoid obscuring data
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.4), ncol=3)

# Adjust layout to make space for the legend
plt.tight_layout()
plt.savefig("preferences.pdf")