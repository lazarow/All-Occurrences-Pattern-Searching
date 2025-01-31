import pandas as pd

data = pd.read_csv("results.310120225.csv")

latex_table = """
\\begin{table}[ht]
    \\centering
    \\begin{tabular}{lrrrl}
        \\toprule
        Dataset & $ | \\Sigma | $ & $ | t | $ & $ | q | $ & $ q $ \\\\
        \\midrule
"""

for _, row in data.iterrows():
    latex_table += f"        {row['Dataset']} & {row['Size of an alphabet']} & {row['Size of a generated input text']} & {row['Size of RE']} & {row['RE']} \\\\\n"

latex_table += """        \\bottomrule
    \\end{tabular}
    \\caption{Summary of datasets with corresponding regular expressions.}
    \\label{tab:dataset_summary}
\\end{table}
"""

print(latex_table)

latex_table = """
\\begin{table}[ht]
    \\centering
    \\begin{tabular}{|l|rr|rr|}
        \\hline
        \\multicolumn{1}{|c|}{\\multirow{2}{*}{Dataset}} & \\multicolumn{2}{c|}{\\# pairs found}  & \\multicolumn{2}{c|}{Time} \\TBstrut \\\\ \\cline{2-5}
        \\multicolumn{1}{|c|}{} & \\multicolumn{1}{c|}{Efficient} & \\multicolumn{1}{c|}{Naive} & \\multicolumn{1}{c|}{Efficient} & \\multicolumn{1}{c|}{Naive} \\TBstrut \\\\ \\hline
        \\hline
"""

for _, row in data.iterrows():
    time = f"${row['Time by Naive [s]']}$\\,s" if row['Time by Naive [s]'] != "timeout" else f"timeout"
    latex_table += f"        {row['Dataset']} & ${row['Found by Suffix']}$ & ${row['Found by Naive']}$ & ${row['Time by Suffix [s]']}$\\,s & {time} \\\\ \n"

# End second LaTeX table
latex_table += """        \\hline
    \\end{tabular}
    \\caption{Detailed experiment summary including search results and times. Timeout was set to 300 seconds.}
    \\label{tab:experiment_details}
\\end{table}
"""


print(latex_table)
