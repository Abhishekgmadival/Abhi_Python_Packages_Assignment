from data_summary import math_ops, visuals
import os

def demo():
    data = [10, 20, 20, 40, 50, 50, 50]
    mean = math_ops.calculate_mean(data)
    median = math_ops.calculate_median(data)
    mode = math_ops.calculate_mode(data)

    print(f"Data: {data}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

    # draw a simple bar chart and save under data_summary/bar_chart.png
    out_path = os.path.join(os.path.dirname(__file__), '..', 'data_summary', 'bar_chart.png')
    out_path = os.path.abspath(out_path)
    visuals.draw_bar_chart(['A','B','C'], [10, 20, 30], output_path=out_path, title='Sample Bar Chart')
    print(f"Bar chart saved to: {out_path}")

if __name__ == '__main__':
    demo()
