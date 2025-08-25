import streamlit as st
import datetime

# ==============================
# データ（例: 西新井駅前 → 池袋駅東口）
# 実際の時刻表を入れ替え可能
# ==============================
bus_stops = [
    "西新井駅前", "本木新道", "熊野前", "王子駅前", "池袋駅東口"
]

# 簡単な時刻表データ（平日ダイヤ例）
# key: 出発地, value: 出発時刻のリスト
# 本番ではもっと詳細データを入れるとよい
timetable = {
    "西新井駅前": ["07:00", "07:30", "08:00", "08:30", "09:00", "10:00"],
    "本木新道":   ["07:10", "07:40", "08:10", "08:40", "09:10", "10:10"],
    "熊野前":     ["07:20", "07:50", "08:20", "08:50", "09:20", "10:20"],
    "王子駅前":   ["07:35", "08:05", "08:35", "09:05", "09:35", "10:35"],
    "池袋駅東口": ["07:55", "08:25", "08:55", "09:25", "09:55", "10:55"],
}

# ==============================
# Streamlit アプリ本体
# ==============================
st.set_page_config(page_title="バス時刻検索", page_icon="🚌", layout="centered")

st.title("🚌 バス時刻検索アプリ")
st.write("西新井駅前 → 池袋駅東口 のバス時刻を検索できます。")

# 出発停留所 & 到着停留所
departure = st.selectbox("出発停留所を選択してください", bus_stops, index=0)
arrival = st.selectbox("到着停留所を選択してください", bus_stops, index=len(bus_stops)-1)

# 出発希望時刻
selected_time = st.time_input("出発希望時刻を入力してください", datetime.time(7, 0))

# 検索ボタン
if st.button("検索"):
    # 出発停留所の時刻表を取得
    times = timetable.get(departure, [])

    # 入力時刻以降の便を検索
    target = None
    for t in times:
        hh, mm = map(int, t.split(":"))
        if datetime.time(hh, mm) >= selected_time:
            target = t
            break

    if target:
        st.success(f"✅ {departure} 発 {target} の便が見つかりました！")

        # 全停留所の時刻を一覧表示
        st.write("### この便の停車駅と時刻")
        for stop in bus_stops:
            idx = timetable[departure].index(target)
            stop_time = timetable[stop][idx]
            st.write(f"- {stop} : {stop_time}")
    else:
        st.error("該当する便がありませんでした。")
