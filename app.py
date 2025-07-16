import streamlit as st
from algorithms import *

st.title("💻 Algorithm Lab")

st.sidebar.title("Choose an Algorithm")
algorithm = st.sidebar.selectbox(
    "Select an algorithm to run:",
    [
        "Two Sum",
        "Best Time to Buy and Sell Stock",
        "Binary Search",
        "Flood Fill",
        "Maximum Subarray",
        "Merge Intervals",
        "Coin Change",
        "Word Search",
        "Subsets",
        "Find Median from Data Stream",
        "Longest Increasing Subsequence",
    ]
)

if algorithm == "Two Sum":
    st.header("Two Sum")
    nums = st.text_input("Enter numbers (comma-separated):", "2,7,11,15")
    target = st.number_input("Enter target:", value=9)
    if st.button("Run Algorithm"):
        nums = list(map(int, nums.split(',')))
        result = two_sum(nums, target)
        st.write("Result:", result)

elif algorithm == "Best Time to Buy and Sell Stock":
    st.header("Best Time to Buy and Sell Stock")
    prices = st.text_input("Enter stock prices (comma-separated):", "7,1,5,3,6,4")
    if st.button("Run Algorithm"):
        prices = list(map(int, prices.split(',')))
        result = max_profit(prices)
        st.write("Maximum Profit:", result)

elif algorithm == "Binary Search":
    st.header("Binary Search")
    nums = st.text_input("Enter sorted numbers (comma-separated):", "1,2,3,4,5,6")
    target = st.number_input("Enter target:", value=4)
    if st.button("Run Algorithm"):
        nums = list(map(int, nums.split(',')))
        result = binary_search(nums, target)
        st.write("Index of Target:", result)

elif algorithm == "Flood Fill":
    st.header("Flood Fill")
    image = st.text_area("Enter image as a 2D list:", "[[1,1,1],[1,1,0],[1,0,1]]")
    sr = st.number_input("Enter starting row:", value=1)
    sc = st.number_input("Enter starting column:", value=1)
    new_color = st.number_input("Enter new color:", value=2)
    if st.button("Run Algorithm"):
        image = eval(image)
        result = flood_fill(image, sr, sc, new_color)
        st.write("Updated Image:", result)

elif algorithm == "Maximum Subarray":
    st.header("Maximum Subarray")
    nums = st.text_input("Enter numbers (comma-separated):", "-2,1,-3,4,-1,2,1,-5,4")
    if st.button("Run Algorithm"):
        nums = list(map(int, nums.split(',')))
        result = max_subarray(nums)
        st.write("Maximum Subarray Sum:", result)

elif algorithm == "Merge Intervals":
    st.header("Merge Intervals")
    intervals = st.text_area("Enter intervals as a list of lists:", "[[1,3],[2,6],[8,10],[15,18]]")
    if st.button("Run Algorithm"):
        intervals = eval(intervals)
        result = merge_intervals(intervals)
        st.write("Merged Intervals:", result)

elif algorithm == "Coin Change":
    st.header("Coin Change")
    coins = st.text_input("Enter coin denominations (comma-separated):", "1,2,5")
    amount = st.number_input("Enter amount:", value=11)
    if st.button("Run Algorithm"):
        coins = list(map(int, coins.split(',')))
        result = coin_change(coins, amount)
        st.write("Minimum Coins Needed:", result)

elif algorithm == "Word Search":
    st.header("Word Search")
    board = st.text_area("Enter board as a 2D list:", "[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]")
    word = st.text_input("Enter word to search:", "ABCCED")
    if st.button("Run Algorithm"):
        board = eval(board)
        result = word_search(board, word)
        st.write("Word Found:", result)

elif algorithm == "Subsets":
    st.header("Subsets")
    nums = st.text_input("Enter numbers (comma-separated):", "1,2,3")
    if st.button("Run Algorithm"):
        nums = list(map(int, nums.split(',')))
        result = subsets(nums)
        st.write("Subsets:", result)

elif algorithm == "Find Median from Data Stream":
    st.header("Find Median from Data Stream")
    st.write("This algorithm requires interactive input.")
    median_finder = MedianFinder()
    num = st.number_input("Enter a number to add to the stream:", value=0)
    if st.button("Add Number"):
        median_finder.add_num(num)
        st.write("Median:", median_finder.find_median())

elif algorithm == "Longest Increasing Subsequence":
    st.header("Longest Increasing Subsequence")
    nums = st.text_input("Enter numbers (comma-separated):", "10,9,2,5,3,7,101,18")
    if st.button("Run Algorithm"):
        nums = list(map(int, nums.split(',')))
        result = length_of_lis(nums)
        st.write("Length of LIS:", result)
