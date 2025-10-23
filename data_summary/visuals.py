import os
import matplotlib.pyplot as plt

def draw_bar_chart(labels, values, output_path="bar_chart.png", title="Bar Chart"):
    """Draw a bar chart and save it to output_path. Creates directories if necessary."""
    if not labels or not values or len(labels) != len(values):
        raise ValueError("Labels and values must be non-empty and of same length")
    # Ensure output directory exists
    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    plt.figure()
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return output_path
