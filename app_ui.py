import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def show_dashboard():
    st.title("🏙️ FateCode Dashboard")
    st.caption("한강변 주요 단지 재건축·재개발 현황 지도")

    # ✅ 데이터셋
    data = pd.DataFrame([
        {"Region": "서초구 반포동", "Name": "한강뷰 아파트 (반포동)", "Status": "재건축 진행중", "Latitude": 37.503, "Longitude": 126.995},
        {"Region": "강남구 압구정동", "Name": "한강뷰 아파트 (압구정동)", "Status": "재건축 예정", "Latitude": 37.529, "Longitude": 127.028},
        {"Region": "송파구 신천동", "Name": "롯데월드타워 시그니엘", "Status": "고급 분양 중", "Latitude": 37.5125, "Longitude": 127.101},
        {"Region": "용산구 보광동", "Name": "한강뷰 재개발 빌라", "Status": "재개발 추진", "Latitude": 37.523, "Longitude": 126.999},
        {"Region": "성동구 옥수동", "Name": "한강뷰 재건축 아파트", "Status": "재건축 중", "Latitude": 37.543, "Longitude": 127.018},
        {"Region": "성북구 만달리빌라", "Name": "만달리 빌라", "Status": "재건축 중단", "Latitude": 37.602, "Longitude": 127.016},
    ])

    # ✅ UI 필터 영역
    st.sidebar.header("🔍 필터")
    region_filter = st.sidebar.multiselect(
        "지역 선택", data["Region"].unique(), default=data["Region"].unique()
    )
    status_filter = st.sidebar.multiselect(
        "진행 상태 선택", data["Status"].unique(), default=data["Status"].unique()
    )

    # ✅ 필터 적용
    filtered_data = data[data["Region"].isin(region_filter) & data["Status"].isin(status_filter)]

    # ✅ 상태별 색상
    def get_color(status):
        if "중단" in status:
            return "gray"
        elif "진행" in status:
            return "red"
        elif "예정" in status:
            return "orange"
        elif "분양" in status:
            return "blue"
        else:
            return "green"

    # ✅ 지도 생성
    m = folium.Map(
        location=[37.52, 127.02],
        zoom_start=12,
        tiles='http://xdworld.vworld.kr:8080/2d/Base/202002/{z}/{x}/{y}.png',
        attr='VWorld Map (국토지리정보원)'
    )

    for _, row in filtered_data.iterrows():
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=9,
            color=get_color(row["Status"]),
            fill=True,
            fill_color=get_color(row["Status"]),
            fill_opacity=0.7,
            tooltip=f"{row['Name']} — {row['Status']}"
        ).add_to(m)

    # ✅ 지도와 표 출력
    st.subheader("📍 한강변 단지 현황 지도")
    st_folium(m, width=1200, height=700)

    st.subheader("📊 단지별 현황 데이터")
    st.dataframe(filtered_data)
