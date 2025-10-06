import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="FateCode Dashboard", layout="wide")

st.title("🏙️ FateCode Dashboard")
st.caption("한강변 주요 지역별 한강뷰 아파트 및 재건축·재개발 현황 지도")

# ✅ 주요 지역 데이터
data = pd.DataFrame([
    # 서초구
    {"Region": "서초구 반포동", "Name": "한강뷰 아파트 (반포동)", "Status": "재건축 진행중", "Latitude": 37.503, "Longitude": 126.995},
    # 강남구
    {"Region": "강남구 압구정동", "Name": "한강뷰 아파트 (압구정동)", "Status": "재건축 예정", "Latitude": 37.529, "Longitude": 127.028},
    {"Region": "강남구 한강변", "Name": "한강뷰 빌라 / 재개발", "Status": "재개발 추진", "Latitude": 37.522, "Longitude": 127.022},
    # 송파구
    {"Region": "송파구 신천동", "Name": "롯데월드타워몰 시그니엘 레지던스", "Status": "고급 분양 중", "Latitude": 37.5125, "Longitude": 127.101},
    {"Region": "송파구 잠실동", "Name": "한강뷰 아파트 / 재건축", "Status": "재건축 예정", "Latitude": 37.516, "Longitude": 127.087},
    # 성동구
    {"Region": "성동구 옥수동", "Name": "한강뷰 재건축 아파트", "Status": "재건축 중", "Latitude": 37.543, "Longitude": 127.018},
    {"Region": "성동구 금호동", "Name": "재개발 빌라 단지", "Status": "재개발 예정", "Latitude": 37.554, "Longitude": 127.020},
    # 용산구
    {"Region": "용산구 보광동", "Name": "한강뷰 아파트 / 재개발 빌라", "Status": "재개발 추진", "Latitude": 37.523, "Longitude": 126.999},
    {"Region": "용산구 청파동", "Name": "한강뷰 아파트 / 재개발 빌라", "Status": "재건축 예정", "Latitude": 37.545, "Longitude": 126.970},
    # 성북 (참고 추가 가능)
    {"Region": "성북구 만달리빌라", "Name": "만달리 빌라", "Status": "재건축 중단", "Latitude": 37.602, "Longitude": 127.016},
])

# ✅ 상태별 색상 설정
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

# ✅ 한글 지도 생성 (VWorld)
m = folium.Map(
    location=[37.52, 127.02],
    zoom_start=12,
    tiles='http://xdworld.vworld.kr:8080/2d/Base/202002/{z}/{x}/{y}.png',
    attr='VWorld Map (국토지리정보원)'
)

# ✅ 마커 표시
for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=9,
        color=get_color(row["Status"]),
        fill=True,
        fill_color=get_color(row["Status"]),
        fill_opacity=0.7,
        tooltip=f"{row['Name']} — {row['Status']}"
    ).add_to(m)

# ✅ Streamlit 출력
st.subheader("📍 한강변 주요 단지 현황 지도")
st_folium(m, width=1200, height=700)

st.subheader("📊 단지별 상태 데이터")
st.dataframe(data)


## 📦 설치 방법
#```bash
#pip install -r requirements.txt
```

## 🚀 실행 방법
```bash
python -m streamlit run app.py
```

## 🗺️ 기능
- Folium 기반 한국어 지도
- Streamlit 시각화 대시보드
- Matplotlib 그래프 포함
- PDF, PPTX, 이미지 생성 확장 가능
