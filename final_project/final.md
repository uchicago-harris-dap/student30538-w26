目标：展示 Python 技能，应用于你感兴趣的政策相关数据问题。
关键日期
1月24日：通过未评分的 Canvas 测验提交提案
3月2-5日：上传幻灯片并在课堂上展示
3月9日 5PM：通过公共 GitHub 仓库提交最终报告和代码
提案要求（Proposal）
提案需包含：
小组成员名单（1-3人）
建议与同 section 同学组队
可跨 section，但所有成员需能参加所有成员的讲座和实验课
研究问题（Motivating question(s)）
不必须是因果问题
需与公共政策相关
3个可能的数据集
需公开可用，或在本季度内可获取
数据应尽可能细粒度（disaggregated）
避免使用州级或国家级数据（太简单）
自问："这个项目用 Excel 能轻松完成吗？" 如果答案是"是"，则需更换数据集
4个静态可视化想法（每个 2-3 句话）
评分标准
1. 展示（Presentation）- 30%
随机选择一名成员现场展示
所有到场成员获得相同展示分数，缺席成员为 0 分
展示幻灯片需包含最终版本的所有组件（2个数据集、2个静态图、1个 Streamlit 应用）
组件可以是"进行中"状态，可在展示后根据反馈改进
2. 编程（Coding）- 45%
a) 数据集选择和处理（20%）
至少使用 2 个数据集
所有数据处理（包括合并和重塑）应在 .qmd 代码中完成
b) 可视化（15%）
至少 2 个静态图（使用 altair 或 geopandas）
1 个 Streamlit 应用，包含至少 1 个动态图/组件
可用动态图替代静态图（例如 3 个动态图可满足要求）
至少 1 个可视化必须是空间可视化（spatial visualization）
c) 可重现性（5%）
TA 或 AI 应能直接运行 .qmd 文件并生成报告（HTML 或 PDF）
如果数据集很大，可在 README.md 中提供下载链接
用户不应需要重命名任何文件
.gitignore 应已设置好忽略大文件
d) Git（5%）
为不同分析部分创建多个分支
最终仓库应只有一个 main 分支
提交历史会用于评估个人贡献
3. 报告（Writeup）- 15%
最多 3 页
顶部包含：所有成员姓名、讲座 section 时间、GitHub 用户名
描述研究问题、方法、代码、遇到的困难
展示静态图并简要说明
讨论 Streamlit 应用及其与研究问题的关系
4. 对展示反馈的响应（10%）
根据教授或 head TA 的书面反馈进行改进的程度
公共仓库结构要求
根目录（Root Directory）
文档和元数据：
requirements.txt 或 requirements.yml
.gitignore 文件（忽略不需要的文件，如 venv）
README.md（链接到 Streamlit Community Cloud、记录数据源、描述数据处理流程）
报告：
final_project.qmd
两个渲染版本：一个 HTML 和一个 PDF
子目录
1. data/ 文件夹
包含初始未修改的数据框
包含最终构建的数据框
如果进行预处理：
使用 preprocessing.py 文件
输入：data/raw-data/
输出：data/derived-data/
如果数据集 > 100MB：
可托管在 Drive 或 Dropbox
在 README.md 中提供链接
如果数据集非公开：
在 README.md 中说明如何获取访问权限
2. Writeup dependencies（报告依赖）
渲染 final_project.qmd 所需的任何额外文件（如外部生成的图形）
3. streamlit-app/ 文件夹
包含应用代码和部署所需的所有文件
在 Streamlit Community Cloud 上部署应用
在 README.md 中包含应用 URL
关键要点总结
数据：至少 2 个数据集，需细粒度
可视化：至少 2 个静态图 + 1 个 Streamlit 应用（至少 1 个动态图）
空间可视化：至少 1 个
可重现性：代码应能直接运行
Git：使用分支，最终合并到 main
部署：Streamlit 应用需部署到 Streamlit Community Cloud

"Can Large Language Models (LLMs) effectively quantify the impact of financial news sentiment and regulatory announcements on the volatility of regional banking stocks? Specifically, we aim to analyze whether LLM-derived sentiment scores can predict short-term market instability better than traditional metrics, providing insights for financial regulators regarding market reaction speeds."

Dataset 1: Financial Market Data (Disaggregated)
Source: yfinance API (Yahoo Finance) or Alpha Vantage.
Details: Daily/Hourly stock prices (OHLCV) for a specific sector (e.g., US Regional Banks or Energy Sector). This is disaggregated by company and time.
Dataset 2: Unstructured News/Text Data
Source: Financial News API (e.g., NewsAPI, GDELT) or SEC EDGAR database (8-K filings).
Details: Raw text of news headlines or corporate filings. You will use the LLM to process this text into "Sentiment Scores" (your derived data).
Dataset 3: Geographic/Spatial Data (For the spatial requirement)
Source: FDIC (Federal Deposit Insurance Corporation) database or US Census Bureau.
Details: Location data of bank headquarters or branch densities. This allows you to map financial stress geographically.

Time-Series with Sentiment Overlay (Altair):
A dual-axis line chart showing the stock price of a representative asset (e.g., SPY or a specific bank) overlaid with the LLM-derived "Sentiment Score" moving average to show correlation during a specific crisis event.
Scatter Plot of Volatility vs. Sentiment Divergence (Altair):
Each point represents a trading day. The X-axis is the variance in news sentiment (how conflicting the news was), and the Y-axis is the market volatility (True Range). Purpose: To see if confusing news leads to higher instability.
Spatial Map of Financial Stress (Geopandas - Crucial for requirement):
A US map coloring states or counties by the average stock performance of regional banks headquartered there (aggregated from individual bank data). This visualizes which geographic regions were hit hardest by a specific policy event (e.g., interest rate hike).
Heatmap of Sector Sentiment (Altair):
A matrix where rows are different industry sectors (Tech, Finance, Energy) and columns are dates. The color represents the LLM-calculated aggregate sentiment score. This visualizes how sentiment shifts across sectors over time.