import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="トレカ検索アプリ", layout="wide")
st.markdown("<h2 style='text-align: center;'>📱 トレカ検索アプリ</h2>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    file_path = "toreka_data.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame(columns=["商品コード", "タイトル", "販売価格（税込）"])

df = load_data()

# 🔍 利用案内を表示（スマホバーコード入力の方法）
with st.expander("🔧 商品コードの読み取り方法（スマホ用）", expanded=True):
    st.markdown("""
- 検索欄をタップしてください  
- バーコード読み取りに対応したキーボードを使うと、カメラが起動します  
- バーコードを読み取ると自動で商品コードが入力されます  

💡 **ヒント**  
- **Android**：Googleレンズやバーコードキーボードなど  
- **iPhone**：カメラでバーコードをスキャン → コピーして貼り付け
    """)

# 商品コード入力
search_code = st.text_input("商品コードで検索（バーコードOK）", "")

# 結果表示（完全一致）
result = df[df["商品コード"].astype(str).str.strip() == search_code.strip()]

if not result.empty:
    row = result.iloc[0]
    price = int(row['販売価格（税込）']) if pd.notna(row['販売価格（税込）']) else 0
    price_str = f"{price:,} 円"

    st.markdown("---")
    st.markdown(f"### 🆔 商品コード：<br><span style='font-size:18px'>{row['商品コード']}</span>", unsafe_allow_html=True)
    st.markdown(f"### 🃏 タイトル：<br><span style='font-size:24px'>{row['タイトル']}</span>", unsafe_allow_html=True)
    st.markdown(f"### 💰 販売価格（税込）：<br><span style='font-size:32px; font-weight:bold;'>{price_str}</span>", unsafe_allow_html=True)
    st.markdown("---")
else:
    st.markdown("🔍 商品コードを入力してください。")
