# PROCESS.md — AI use for Assignment 2

**Tools used**: I used DeepSeek as a coding assistant, primarily to check my syntax, suggest structural improvements for the plotting code, and help me debug the specific encoding errors I was facing with the HKO CSV file.

**What I kept (and why it was good)**:
I kept the core structure of the plotting code. Specifically, I kept the AI's suggestion to use `matplotlib.use('Agg')` to prevent the Mac terminal from crashing when trying to open a window. I also kept its recommendation to parse the Year/Month/Day columns into a single `datetime` object, which made the x-axis easier to plot. This saved me time on the initial syntax setup.

**What I rejected (and why it was wrong)**:
The most important part of my process was rejecting the AI's initial approach. When I first asked it to fetch the data, it suggested I use a complex API with an authentication key. I rejected this because the assignment brief explicitly requires downloading a raw CSV file and committing it directly to the `data/` folder. 

Secondly, when I got to the plotting stage, the AI's initial code plotted all 140 years of data. It looked like a dense blue blob and was completely unreadable. I rejected this and manually adjusted the code to only visualize the last 3 years, since recent data is more relevant and easier to read.

**What I did myself (my actual work)**:
The hardest parts of this assignment were not done by AI. 
1. **Data sourcing and network troubleshooting**: I manually downloaded the CSV file from the Hong Kong Observatory website because the `uv run fetch.py` script kept timing out due to network issues. 
2. **Encoding debugging**: I identified that the file was in `utf-8-sig` encoding (not Big5) by trial and error, rewriting the `preview.py` script multiple times to ensure the Chinese headers were read correctly.
3. **Data cleaning**: I manually handled non-numeric values like "Trace" in the rainfall column by writing a `try/except` block to convert them to 0.0. 
4. **Documentation**: I wrote the `README.md` from scratch, including the critical section "What does it hide?", where I analyzed the limitations of compressing 140 years of data into one chart.

**My process and timeline**:
- Manually downloaded and debugged the raw data (30 minutes, no AI)
- Wrote `preview.py` to verify the data (10 minutes, AI helped with `csv` module syntax)
- Designed and iterated the plot in `plot.py` (20 minutes, I manually filtered the date range and edited the visual style)
- Wrote the README and PROCESS files (20 minutes, no AI)

I used AI as a syntax checker and a rubber duck, but the core decisions, data handling, and final visualisation were my own.