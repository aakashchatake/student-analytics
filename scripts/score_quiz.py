import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def score_quiz(file_path):
    df = pd.read_csv(file_path)
    df['Score'] = df.iloc[:, 1:].sum(axis=1)
    df['Grade'] = pd.cut(df['Score'], bins=[0, 2, 4, 5], labels=['F', 'C', 'A'])
    return df

if __name__ == "__main__":
    df = score_quiz("data/quiz_results.csv")
    df.to_csv("reports/scored_results.csv", index=False)
    print("Scoring complete. Results saved to reports/scored_results.csv")

    # Pie Chart
    grade_counts = df['Grade'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Grade Distribution (Pie Chart)")
    plt.savefig("reports/grade_pie_chart.png")
    plt.close()

    # Histogram
    plt.figure(figsize=(8,5))
    plt.hist(df['Score'], bins=5, color='skyblue', edgecolor='black')
    plt.title("Score Distribution (Histogram)")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.savefig("reports/score_histogram.png")
    plt.close()

    # Bell Curve
    plt.figure(figsize=(8,5))
    sns.histplot(df['Score'], kde=True, color='green')
    plt.title("Score Distribution with Bell Curve")
    plt.xlabel("Score")
    plt.ylabel("Density")
    plt.savefig("reports/score_bell_curve.png")
    plt.close()