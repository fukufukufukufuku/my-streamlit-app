import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("2変数を選んで散布図を表示するアプリ")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("データプレビュー")
    st.dataframe(df)

    # 数値列のみ抽出
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # 数値列が2つ以上ない場合
    if len(numeric_columns) < 2:
        st.error("数値列が2列以上含まれているCSVをアップロードしてください。")
    else:
        # 変数選択
        x_var = st.selectbox("X軸の変数を選択してください", numeric_columns)
        y_var = st.selectbox("Y軸の変数を選択してください", numeric_columns)

        # 散布図の作成
        fig, ax = plt.subplots()
        ax.scatter(df[x_var], df[y_var])
        ax.set_xlabel(x_var)
        ax.set_ylabel(y_var)
        ax.set_title(f"{x_var} vs {y_var} の散布図")

        st.pyplot(fig)


