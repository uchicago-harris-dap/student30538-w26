"""
Decorator demo: caching a slow function.

Run this script twice:
  1. As-is, to see the function called repeatedly with no caching.
  2. Use a decorator to cache the results from compute_passengers, so that repeated calls with the same arguments are fast.

https://uchicago-harris-dap-dashboards-dps-2app-dps-2-agrx7x.streamlit.app/
"""

import time
import streamlit as st

@st.cache_data # 缓存函数结果 相同参数（route, cut_pct）重复调用直接返回缓存
def compute_passengers(route, cut_pct):
    """Simulate a slow computation (e.g. loading data, running a model)."""
    time.sleep(1)  # stand-in for expensive work
    return round((100 - cut_pct) * 1.2345, 2)

# --- main script --------------------------------------------------------

scenarios = [
    ("Red Line",  10),
    ("Blue Line", 20),
    ("Red Line",  10),  # repeat
    ("Blue Line", 20),  # repeat
    ("Red Line",  10),  # repeat again
]

overall_start = time.time()
st.write("Running 5 scenarios:\n")
for route, cut_pct in scenarios:
    start = time.time()
    result = compute_passengers(route, cut_pct)
    elapsed = time.time() - start
    st.write(f"  compute_passengers{(route, cut_pct)} took {elapsed:.3f}s")
    st.write(f"  -> {route}, {cut_pct}% cut: {result} expected passengers\n")

total = time.time() - overall_start
st.write(f"Total time: {total:.3f}s")

# 无缓存	~5.000s	每次调用都执行 time.sleep(1)
# 有缓存	~2.003s	前 2 次计算，后 3 次命中缓存