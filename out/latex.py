import pandas as pd

data = pd.read_csv("results.11022025.csv")

latex_table = """
\\begin{table}[ht]
    \\centering
    \\begin{tabular}{|l|r|rr|}
        \\hline
        \\multicolumn{1}{|c|}{\\multirow{2}{*}{Dataset}} & \\multicolumn{1}{c|}{\\multirow{2}{*}{\\# pairs found}}  & \\multicolumn{2}{c|}{Time} \\TBstrut \\\\ \\cline{3-4}
        \\multicolumn{1}{|c|}{} & \\multicolumn{1}{c|}{} & \\multicolumn{1}{c|}{Efficient} & \\multicolumn{1}{c|}{Naive} \\TBstrut \\\\ \\hline
        \\hline
"""

for _, row in data.iterrows():
    time = f"${row['Time by Naive [s]']}$\\,s" if row['Time by Naive [s]'] != "timeout" else f"timeout"
    latex_table += f"        {row['Dataset']} & ${row['Matches Found']}$ & ${row['Time by Suffix [s]']}$\\,s & {time} \\\\ \n"

# End second LaTeX table
latex_table += """        \\hline
    \\end{tabular}
    \\caption{Detailed experiment summary including search results and times.}
    \\label{tab:experiment_details}
\\end{table}
"""

print(latex_table)
